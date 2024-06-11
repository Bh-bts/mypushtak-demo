import os

from tests.test_BasePage import BaseTest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


# Test class for verifying user login functionality
class TestLogin(BaseTest):

    # Test method to verify successful login with valid email and password
    def test_verify_the_user_can_successfully_login_with_valid_email_and_password(self):
        # login to mypushtak site
        self.homePage = HomePage(self.driver)
        self.homePage.click_login_button_on_header()
        self.loginPage = LoginPage(self.driver)
        email = os.getenv('MYPUSTAK_EMAIL')
        password = os.getenv('MYPUSTAK_PASSWORD')
        self.loginPage.do_login(email, password)
        assert self.homePage.get_profile_text() == "Hi! Reader"
