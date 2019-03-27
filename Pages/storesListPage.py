from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import Locators
from Pages.basepage import BasePage


class Stores(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def sync_now(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.SELECT_CATEGORY)).click()
