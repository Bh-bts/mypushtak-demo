from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    login_button = (By.XPATH, "//button[text()='Login']")
    search_field = (By.CSS_SELECTOR, "div[class*='text-sm'] input")
    search_button = (By.CSS_SELECTOR, "div[class*='text-sm'] button[aria-label='searchButton']")
    profile_text = (By.CSS_SELECTOR, "button[class='undefined icon'] span:nth-child(1)")
    wishlist_button = (By.XPATH, "//div[text()=' My Wishlist']")
    wishlist_toast_message_text = (By.XPATH, "//div[@id='notistack-snackbar']/div/span")
    cart_button = (By.CSS_SELECTOR, "div[class*=' d-none'] span:nth-child(3)")
    add_to_cart_button_on_popup = (By.CSS_SELECTOR, "div[class*='MuiDialog'] button[value='Add to Cart 1955']")
    books_added_to_cart_text = (By.XPATH, "//span[text()='Book added to cart!']")

    # Click the login button on the header
    def click_login_button_on_header(self):
        self.do_click(self.login_button)

    # Get the profile text after login
    def get_profile_text(self):
        return self.get_element_text(self.profile_text)

    # Clear the search field
    def clear_search_field(self):
        self.clear(self.search_field)

    # Enter book title on the search field
    def enter_book_on_search_button(self, book_title):
        self.send_keys(self.search_field, book_title)

    # Click on the search button
    def click_on_search_button(self):
        self.do_click(self.search_button)

    # Add a book to the cart
    def add_book_to_cart(self, book_title):
        add_to_cart_button_element = f"//h3[@title='{book_title}']//ancestor::div[contains(@class, 'BookCard_main')]//button"
        self.do_click((By.XPATH, add_to_cart_button_element))

    # Click on the cart button
    def click_on_cart(self):
        self.do_click(self.cart_button)

    # Get the text indicating that books have been added to the cart
    def get_books_added_to_cart_text(self):
        return self.get_element_text(self.books_added_to_cart_text)

    # Click on the cart button on the popup
    def click_on_cart_on_popup(self):
        self.do_click(self.add_to_cart_button_on_popup)

    # Get the price of a book from the Home Page
    def get_book_price_from_home_page(self, book_title):
        price_xpath = f"//h3[@title='{book_title}']//ancestor::div[contains(@class, 'BookCard_text')]//span[contains(@class, 'BookCard_priceS')]"
        price_text = self.get_element_text((By.XPATH, price_xpath))
        price_number = price_text.replace('₹', '').replace(',', '').strip()
        return float(price_number)

    def get_text_of_add_to_cart_button(self, book_title):
        add_to_cart_button_element = f"//h3[@title='{book_title}']//ancestor::div[contains(@class, 'BookCard_main')]//button"
        return self.get_element_text((By.XPATH, add_to_cart_button_element))

    def click_on_profile(self):
        self.do_click(self.profile_text)

    def click_on_wishlist_button(self):
        self.do_click(self.wishlist_button)

    def is_book_in_wishlist(self, book_title):
        book_title_element = (By.XPATH, f"//h3[@title='{book_title}']//ancestor::div[contains(@class, 'BookCard_main')]//div[contains(@class, 'heart')]")
        wishlist_button = self.is_element_is_present(book_title_element)
        classes = wishlist_button.get_attribute('class')
        return 'Product_click_wishlist__dkS5L' in classes

    def add_to_wishlist(self, book_title):
        if not self.is_book_in_wishlist(book_title):
            book_title_element = (By.XPATH, f"//h3[@title='{book_title}']//ancestor::div[contains(@class, 'BookCard_main')]//div[contains(@class, 'heart')]")
            self.do_click(book_title_element)

    def wishlist_text_message(self):
        return self.get_element_text(self.wishlist_toast_message_text)
