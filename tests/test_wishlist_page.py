import pytest

from tests.test_base_page import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.wishlist_page import WishlistPage


class TestWishListPage(BaseTest):

    @pytest.mark.usefixtures("setUp", "login_fixture")
    def test_verify_user_can_add_any_book_to_wishlist(self):
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)

        # Store books title in list variable
        books_title = ['CRACK IMU-CET Entrance Exam', 'Mastering Yoga',
                       'The Yoga of Spiritual Devotion']

        for book_title in books_title:
            self.homePage.clear_search_field()
            self.homePage.enter_book_on_search_button(book_title)
            self.homePage.click_on_search_button()
            self.homePage.add_to_wishlist(book_title)

        self.homePage.click_on_profile()
        self.homePage.click_on_wishlist_button()
        self.wishlistPage = WishlistPage(self.driver)
        for book_title in books_title:
            assert self.wishlistPage.get_book_on_wishlist(book_title) == book_title
