from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WishlistPage(BasePage):
    # Locators
    book_title_text = (By.XPATH, "")

    def get_book_on_wishlist(self, book_title):
        self.find_element((By.XPATH, f"f//div[@title='{book_title}']"))
