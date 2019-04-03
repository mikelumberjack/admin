from Pages.basepage import BasePage
from Locators.locators import Locators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self, driver):
        pass

    def logging_in(self):
        self.driver.get('http://www.staging.365dropship.com/')
        self.click_on_login()
        self.switch_to_login_frame()
        self.enter_username()
        self.enter_password()
        self.click_submit_botton()
        self.loader()

    def click_on_login(self):
        self.driver.find_element(*Locators.LOGIN).click()

    def switch_to_login_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*Locators.LOGIN_FRAME))

    def enter_username(self, username='yarivluts@gmail.com'):
        self.driver.find_element(*Locators.USERNAME).clear()
        self.driver.find_element(*Locators.USERNAME).send_keys(username)

    def enter_password(self, password='1234567'):
        self.driver.find_element(*Locators.PASSWORD).clear()
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_submit_botton(self):
        self.driver.find_element(*Locators.LOGIN_SUBMIT_BOTTON).click()

    def is_incorrect_displayed(self):
        return self.driver.find_element(*Locators.INCORECT_USER_PASS).is_displayed()
