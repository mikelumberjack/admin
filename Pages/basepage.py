from abc import abstractmethod
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import Locators


class BasePage(object):
    """ All page objects inherit from this """

    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return

    def time_out(self):
        if self.driver.execute_script('return Catalog.LOADING_STATUS'):
            time.sleep(3)
            self.time_out()

    def loader(self):
        time.sleep(1)
        WebDriverWait(self.driver, 180) \
            .until(lambda s: s.find_element_by_id('loading-mask')
                   .get_attribute('style') == 'display: none;')

    def loader_v2(self):
        time.sleep(1)
        WebDriverWait(self.driver, 180) \
            .until(lambda s: s.find_element_by_id('loading-mask-v2')
                   .get_attribute('style') != 'display: block;')

    def select_category(self, category_name):
        if category_name:
            WebDriverWait(self.driver, 60) \
                .until(expected_conditions.element_to_be_clickable(Locators.SELECT_CATEGORY)).click()
            category_items = self.driver.find_elements(*Locators.CATEGORY_ITEMS)
            for elem in category_items:
                if elem.text == category_name:
                    elem.click()
                    break
            self.time_out()
        # implementation by index
        # select = self.driver.find_element_by_id('root_categories_select')
        # print(select.text)
        # self.driver.execute_script('arguments[0].selectedIndex=' + str(category_name) +
        #                            '; arguments[0].dispatchEvent(new Event("change"))', select)
        # self.time_out()

    def select_sub_category(self, sub_category_name):
        if sub_category_name:
            WebDriverWait(self.driver, 60) \
                .until(expected_conditions.element_to_be_clickable(Locators.SELECT_SUB_CATEGORY)).click()
            sub_category_items = self.driver.find_elements(*Locators.SUB_CATEGORY_ITEMS)
            for elem in sub_category_items:
                if elem.text == sub_category_name:
                    elem.click()
                    break
            self.time_out()

    def select_all(self):
        WebDriverWait(self.driver, 60) \
            .until(expected_conditions.element_to_be_clickable(Locators.SELECT_ALL)).click()
        self.loader_v2()

    def get_quantity_selected_items(self):
        return self.driver.find_element(*Locators.QUANTITY_OF_SELECTED_ITEMS).text
