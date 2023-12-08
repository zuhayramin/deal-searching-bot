from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, hotel_boxes:WebElement):
        self.hotel_boxes = hotel_boxes

    def pull_deals(self) :
        return self.hotel_boxes.find_elements(By.XPATH, '//div[@data-testid="property-card"]')
    
    def pull_titles(self):
        deals = self.pull_deals()
        print("Starting....")

        for deal in deals:
            hotel_title = deal.find_element(By.XPATH, './/div[@data-testid="title"]').get_attribute("innerHTML").strip()
            hotel_price = deal.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]').get_attribute("innerHTML").strip()
            # hotel_rating = deal.find_element(By.XPATH, './/div[@class="a3b8729ab1 d86cee9b25"]').get_attribute("innerHTML").strip()

            print(hotel_title)
            print(hotel_price)
            # print(hotel_rating)

        # for deal in deals:
        #     title_element = deal.find_element(By.XPATH, '//div[@data-testid="title"]')
        #     price_element = deal.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]')

        #     rating_elements = deal.find_elements(By.CLASS_NAME, 'a3b8729ab1.d86cee9b25')

        #     for rating_element in rating_elements:
        #         print(title_element.get_attribute('innerText').strip())
        #         print(price_element.get_attribute('innerText').strip())
        #         print(rating_element.get_attribute('innerText').strip())
