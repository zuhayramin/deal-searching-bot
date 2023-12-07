from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="/usr/local/bin/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__(executable_path=driver_path)
        self.implicitly_wait(15)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        print(self)

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