from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Locators
    email_text_field = (By.CSS_SELECTOR, "input[id=':r2:']")
    password_text_field = (By.CSS_SELECTOR, "input[type='password']")
    proceed_button = (By.XPATH, "//button[text()='Proceed']")
    login_button_in_form = (By.CSS_SELECTOR, "button[class*='WLoginNavbar_loginButton']")

    # Perform login with provided email and password
    def do_login(self, email, password):
        self.send_keys(self.email_text_field, email)
        self.do_click(self.proceed_button)
        self.send_keys(self.password_text_field, password)
        self.do_click(self.login_button_in_form)
