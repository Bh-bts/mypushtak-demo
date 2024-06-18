from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WishlistPage(BasePage):
    # Locators
    book_title_text = (By.XPATH, "")

    def get_book_on_wishlist(self, book_title):
        book_title = self.is_element_is_present((By.XPATH, f"//div[@title='{book_title}']"))
        return book_title.get_attribute("title")
