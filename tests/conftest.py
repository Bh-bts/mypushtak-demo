from config.config_reader import config_reader
from selenium import webdriver

import pytest


@pytest.fixture(scope='class')
def setUp(request):
    # Read browser configuration and base URL from the settings file
    browser = config_reader.get('Settings', 'BROWSER')
    headless = config_reader.getboolean('Settings', 'HEADLESS')
    base_url = config_reader.get('Settings', 'BASE_URL')

    # Initialize WebDriver based on the browser configuration
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Chrome(options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Edge(options)
    else:
        raise ValueError(f"Browser{browser} is not supported")

    # Maximize window and navigate to the base URL
    driver.maximize_window()
    driver.get(base_url)

    # Pass the WebDriver instance to the test class
    request.cls.driver = driver
    yield driver

    # Quit the WebDriver instance after test class execution
    driver.quit()
