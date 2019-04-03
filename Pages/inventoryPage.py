import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.basepage import BasePage
from Locators.locators import Locators


class Inventory(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def get_total_items(self):
        total = self.driver.find_element(*Locators.TOTAL_ITEM).text
        return total.split(' ')[3]

    def check_product(self, product_id):
        product_link = \
            self.driver.find_element(By.CSS_SELECTOR, 'a.item-link[data-product-id="' + product_id + '"]')
        product_check = \
            self.driver.find_element(By.CSS_SELECTOR, 'a.check[data-check-product-id="' + product_id + '"]')
        ActionChains(self.driver).move_to_element(product_link).move_to_element(product_check).click().perform()

    def remove_from_inventory(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.REMOVE_FROM_INVENTORY)).click()

    def confirm(self):
        self.driver.switch_to.frame(self.driver.find_element(*Locators.REMOVE_FRAME))
        self.driver.find_element(*Locators.CONFIRM_REMOVE_BOTTOM).click()
        self.loader_v2()
