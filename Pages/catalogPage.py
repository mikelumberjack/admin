import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.basepage import BasePage
from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


class Catalog(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def check_product(self, product_id):
        product_link = \
            self.driver.find_element(By.CSS_SELECTOR, 'a.item-link[data-product-id="' + product_id + '"]')
        product_check = \
            self.driver.find_element(By.CSS_SELECTOR, 'a.check[data-check-product-id="' + product_id + '"]')
        ActionChains(self.driver).move_to_element(product_link).move_to_element(product_check).click().perform()

    def get_selected_items(self):       # to finish
        return [i.get_attribute('data_check_product_id') for i in self.driver.find_elements(*Locators.ALL_SELECTED)
            if i.is_displayed()]

    def add_to_inv_main(self):
        self.driver.find_element(*Locators.ADD_TO_INV).click()
        self.loader_v2()

    def add_to_shopping_cart(self):
        self.driver.find_element(*Locators.ADD_TO_CART).click()
        self.loader_v2()

    def get_total_on_page(self):  # quantity of total item on page
        total = self.driver.find_element(*Locators.TOTAL_ITEM).text
        return total.split(' ')[3]

    def open_product(self, product_id):
        self.driver.find_element(By.CSS_SELECTOR, 'a.item-link[data-product-id="' + product_id + '"]').click()
        self.loader_v2()

    def all_products_sync_to_inv(self):
        WebDriverWait(self.driver, 500) \
            .until(expected_conditions.visibility_of_element_located(Locators.POP_UP_BUTTON_SYNCED)).click()
        self.loader_v2()
