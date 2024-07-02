from datetime import datetime

import pytest
import os

from config.config_reader import config_reader
from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome')
    parser.addoption("--headless", action='store', default='True')


@pytest.fixture(scope='class')
def setUp(request):
    # Retrieve browser and headless options from command line
    browser = request.config.getoption("--browser")  # Retrieve browser option
    headless = request.config.getoption("--headless")  # Retrieve headless option
    base_url = config_reader.get('Settings', 'BASE_URL')

    # Initialize WebDriver based on the browser configuration
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless.lower() == 'true':
            options.add_argument('--headless')
        driver = webdriver.Chrome(options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless.lower() == 'true':
            options.add_argument('--headless')
        driver = webdriver.Firefox(options)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        if headless.lower() == 'true':
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


@pytest.fixture(scope='function')
def login_fixture(setUp):
    driver = setUp
    homePage = HomePage(driver)
    homePage.click_login_button_on_header()
    loginPage = LoginPage(driver)
    email = os.getenv('MYPUSTAK_EMAIL')
    password = os.getenv('MYPUSTAK_PASSWORD')
    loginPage.do_login(email, password)
    assert homePage.get_profile_text() == "Hi! Reader"
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('setUp')
        if driver:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')

            class_name = item.cls.__name__ if item.cls else "NoClass"
            function_name = item.name
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

            screenshot_name = f"{class_name}.{function_name}--{timestamp}.png"
            screenshot_path = os.path.join('screenshots', screenshot_name)

            driver.save_screenshot(screenshot_path)
