import types
import typing
from selenium import webdriver
import os
import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/usr/local/bin/chromedriver", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        # os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if(self.teardown):
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

   