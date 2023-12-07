from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import booking.constants as const
import time

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="/usr/local/bin/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__(executable_path=driver_path)
        self.implicitly_wait(100)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def remove_banner(self):
        try:
            close_button = self.find_element(By.XPATH, "//*[contains(@aria-label, 'Dismiss sign in information')]")
            close_button.click()
        except:
            return self

    def change_currency(self, currency = None):
        try:
            currency_element = self.find_element(By.XPATH, "//*[@data-testid='header-currency-picker-trigger']")
            currency_element.click()

            selected_currency_element = self.find_element(By.XPATH, f"//div[contains(text(), '{currency}')]")
            selected_currency_element.click()

        except Exception as e:
            print(f"Error: {e}")

    def set_destination(self, place_to_go) : 
        search_field = self.find_element(By.ID, ':re:')
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(1)

        first_result = self.find_element(By.ID, 'autocomplete-result-0')
        first_result.click()

    def travel_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.XPATH, f"//*[@aria-label='{check_in_date}']")
        check_in_element.click()

        check_out_element = self.find_element(By.XPATH, f"//*[@aria-label='{check_out_date}']")
        check_out_element.click()

    def set_travellers(self, number_of_adults = 1): 
        traveller_element = self.find_element(By.XPATH, "//*[@data-testid='occupancy-config']")
        traveller_element.click()

        while True:
            decrease_adults_button = self.find_element(By.XPATH, "//input[@id='group_adults']/following-sibling::div[@class='f4878764f1']/following-sibling::div[@class='bfb38641b0']/descendant::button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 e91c91fa93']")
            decrease_adults_button.click()

            # Get the input field wihch contains number of adults
            adults_value_element = self.find_element(By.ID, "group_adults")
            # Get the explicit number of adults
            adults_value = adults_value_element.get_attribute('value')

            # Exit loop if number of adults reaches 1
            if int(adults_value) == 1:
                break

        increase_adults_button = self.find_element(By.XPATH, "//input[@id='group_adults']/following-sibling::div[@class='f4878764f1']/following-sibling::div[@class='bfb38641b0']/descendant::button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a']")

        # The _ just means that the iterator is not being used in the loop
        for _ in range(number_of_adults - 1):
            increase_adults_button.click()