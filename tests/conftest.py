from config.config_reader import config_reader
from selenium import webdriver

import pytest


@pytest.fixture(scope='class')
def setUp(request):
    browser = config_reader.get('Settings', 'BROWSER')
    headless = config_reader.get('Settings', 'HEADLESS')
    base_url = config_reader.get('Settings', 'BASE_URL')

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Chrome()
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

    driver.maximize_window()
    driver.get(base_url)

    request.cls.driver = driver
    yield driver
    driver.quit()
