from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """ Basic methods of working with WebDriver. """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def find_element(self, locator, time=10):
        """ Find element on the page. """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        """ Find elements on the page. """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def go_to_site(self):
        """ Go to the base url. """
        return self.driver.get(self.base_url)
