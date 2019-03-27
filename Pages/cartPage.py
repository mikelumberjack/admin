import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Pages.basepage import BasePage
from Locators.locators import Locators


class Cart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def remove_elem_from_cart(self, sku):
        elements = self.driver.find_elements(*Locators.REMOVE_FROM_CART)
        for item in elements:
            if item.get_attribute('data-remove-from-cart') == sku:
                item.click()

    def remove_all_from_cart(self):
        elements = self.driver.find_elements(*Locators.REMOVE_FROM_CART)
        for elem in elements:
            WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of(elem)).click()

    def get_items_in_cart(self):
        elements = WebDriverWait(self.driver, 120)\
            .until(expected_conditions.presence_of_all_elements_located(Locators.REMOVE_FROM_CART))
        return [i.get_attribute('data-remove-from-cart') for i in elements]

    def is_cart_empty(self):
        return \
            WebDriverWait(self.driver, 120).until(expected_conditions.presence_of_element_located(Locators.EMPTY_ALERT))\
            and True or False

    def firstname(self, firstname):
        self.driver.find_element(*Locators.FIRST_NAME).clear()
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(firstname)

    def lastname(self, lastname):
        self.driver.find_element(*Locators.LAST_NAME).clear()
        self.driver.find_element(*Locators.LAST_NAME).send_keys(lastname)

    def city(self, city):
        self.driver.find_element(*Locators.CITY).clear()
        self.driver.find_element(*Locators.CITY).send_keys(city)

    def street(self, street):
        self.driver.find_element(*Locators.STREET).clear()
        self.driver.find_element(*Locators.STREET).send_keys(street)

    def zip(self, zip_code):
        self.driver.find_element(*Locators.ZIP).clear()
        self.driver.find_element(*Locators.ZIP).send_keys(zip_code)

    def email(self, email):
        self.driver.find_element(*Locators.EMAIL).clear()
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def phone(self, phone):
        self.driver.find_element(*Locators.PHONE).clear()
        self.driver.find_element(*Locators.PHONE).send_keys(phone)

    def country(self, country_index):
        select = self.driver.find_element(*Locators.COUNTRY)
        self.driver.execute_script('arguments[0].selectedIndex=' + str(country_index) +
                                   '; arguments[0].dispatchEvent(new Event("change"))', select)
        # self.driver.execute_script('arguments[0].style.opacity=1', select)
        # select = Select(select)
        # select.select_by_value('GE')
        self.loader_v2()

    def shipping(self, shipping_type=1):
        select = self.driver.find_element(*Locators.SHIP_METHOD)
        self.driver.execute_script('arguments[0].selectedIndex=' + str(shipping_type) +
                                   '; arguments[0].dispatchEvent(new Event("change"))', select)
        self.loader_v2()

    def checkout(self):
        self.driver.find_element(*Locators.CHECKOUT).click()

    def low_balance(self):
        self.driver.find_element(*Locators.CANCEL_POP_UP).click()
