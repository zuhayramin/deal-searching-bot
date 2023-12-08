from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.report import BookingReport
import booking.constants as const
import time
from prettytable import PrettyTable

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

    def set_adults(self, number_of_adults = 1):
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

    def click_search_button(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()


    def apply_filtration(self, *star_values):
        print("Start filtration...")
        star_filtration_box = self.find_element(By.XPATH, '//*[@data-filters-group="class"]')
        print("Got the group ready...")
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")
        print("Getting Serious")
        for star_value in star_values:
            for star in star_child_elements:
                if str(star.get_attribute("innerHTML")).strip() == f"{star_value} stars" :
                    star.click()

    def sort_results(self):
        sort_menu = self.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
        sort_menu.click()

        try:
            sort_lowest_price = self.find_element(By.XPATH, '//button[@data-id="price"]')
            sort_lowest_price.click()
        except:
            sort_highest_ratings = self.find_element(By.XPATH, '//button[@data-id="class"]')
            sort_highest_ratings.click()

    def report(self):
        parent_element = self.find_element(By.CLASS_NAME, 'd4924c9e74')
        report = BookingReport(self, parent_element)
        table = PrettyTable(
            field_names=['Hotel Name', 'Hotel Price']
        )
        table.add_rows(report.pull_deal_attributes())
        print(table)
