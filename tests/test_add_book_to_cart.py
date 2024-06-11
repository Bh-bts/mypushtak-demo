import os

from tests.test_base_page import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


# Test class for add book to cart functionality
class TestAddBookToCart(BaseTest):

    # Verify total cart value calculation after adding three books
    def test_verify_total_cart_value_calculation_after_adding_three_books(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_login_button_on_header()

        # login to mypushtak site
        self.loginPage = LoginPage(self.driver)
        email = os.getenv('MYPUSTAK_EMAIL')
        password = os.getenv('MYPUSTAK_PASSWORD')
        self.loginPage.do_login(email, password)
        assert self.homePage.get_profile_text() == "Hi! Reader"

        # Store books title in list variable
        books_title = ['CRACK IMU-CET Entrance Exam', 'Mastering Yoga',
                       'The Yoga of Spiritual Devotion']

        total_price = 0

        # Add books to cart
        for book_title in books_title:
            self.homePage.clear_search_field()
            self.homePage.enter_book_on_search_button(book_title)
            self.homePage.click_on_search_button()
            price = self.homePage.get_book_price_from_home_page(book_title)
            total_price += price
            if self.homePage.get_text_of_add_to_cart_button(book_title) == ' Add To Cart':
                self.homePage.add_book_to_cart(book_title)
                # Get book price from Home Page and calculate total price
                self.homePage.click_on_cart_on_popup()
                assert self.homePage.get_books_added_to_cart_text() == 'Book added to cart!'

        # Go to the cart page and verify total price
        self.cartPage = CartPage(self.driver)
        self.homePage.click_on_cart()
        cart_price = self.cartPage.get_total_price()

        assert total_price == cart_price
