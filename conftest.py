import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """ Initializing the WebDriver. """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
