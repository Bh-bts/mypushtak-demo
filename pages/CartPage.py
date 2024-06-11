from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


# Page class representing the Cart Page
class CartPage(BasePage):
    # Locators
    total_price_text = (By.CSS_SELECTOR, "span[id='BookPricediv']")

    # Get the total price of items in the cart
    def get_total_price(self):
        price_text = self.get_element_text(self.total_price_text)
        price_number = price_text.replace('₹', '').replace(',', '').strip()
        return float(price_number)
