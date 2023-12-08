from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, driver, hotel_boxes:WebElement):
        self.driver = driver
        self.hotel_boxes = hotel_boxes

    def pull_deals(self) :
        return self.hotel_boxes.find_elements(By.XPATH, '//div[@data-testid="property-card"]')
    
    def pull_deal_attributes(self):
        deals = self.pull_deals()
        collections = []
        for deal in deals:
            hotel_title = deal.find_element(By.XPATH, './/div[@data-testid="title"]').get_attribute("innerHTML").strip()
            hotel_price = deal.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]').get_attribute("innerHTML").strip()

            collections.append([hotel_title, hotel_price])

        return collections