from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.basepage import BasePage
from Locators.locators import Locators


class Menu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def go_to_home(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.HOME_ICON)).click()
        self.loader()

    def go_to_profile(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.PROFILE_ICON)).click()
        self.loader()

    def go_to_dashboard(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.DASHBOARD_ICON)).click()
        self.loader()

    def go_to_catalog(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.CATALOG_ICON)).click()
        self.time_out()

    def go_to_inventory(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.INVENTORY_ICON)).click()
        self.time_out()

    def go_to_cart(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.CART_ICON)).click()

    def go_to_orders(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.ORDERS_ICON)).click()

    def go_to_transactions(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.TRANSACTIONS_ICON)).click()

    def go_to_store_list(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.STORES_LIST_ICON)).click()
