from Pages.basepage import BasePage
from Locators.locators import Locators


class ProductDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def add_to_inventory(self):
        self.driver.find_element(*Locators.ADD_TO_INV_PD).click()

    def add_to_cart(self):
        self.driver.find_element(*Locators.ADD_TO_CART_PD).click()

    def get_sku(self):
        sku = self.driver.find_element(*Locators.SKU).text
        return sku[6:]
