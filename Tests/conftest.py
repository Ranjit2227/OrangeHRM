import pytest
from selenium import webdriver
from Utilities.config_reader import get_browser,get_base_url


@pytest.fixture
def setup():
    browser= get_browser()

    if browser.lower()=="chrome":
        driver= webdriver.Chrome()
    elif browser.lower()=="firefox":
        driver= webdriver.Firefox()
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.get(get_base_url())

    yield driver
    driver.quit()