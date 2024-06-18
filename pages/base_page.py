from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Base Page class to provide common methods for page objects.
class BasePage:

    # Constructor to initialize BasePage with WebDriver instance
    def __init__(self, driver):
        self.driver = driver

    # Perform a click action on the element located by the given locator
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()

    # Send text input to the element located by the given locator
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Get the text value of the element located by the given locator
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Check if the element located by the given locator is visible
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # Clear the text input of the element located by the given locator
    def clear(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).clear()

    # Scroll to the element located by the given locator
    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    # Navigate to the previous page in the browser history
    def navigate_to_previous_page(self):
        self.driver.execute_script("window.history.go(-1)")

    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def is_element_is_present(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element
