from Locators.locators import Locators
from Pages.loginPage import BasePage


class ProfilePage(BasePage):

    def _validate_page(self, driver):
        pass

    def sign_out(self):
        self.driver.find_element(*Locators.SIGN_OUT).click()
