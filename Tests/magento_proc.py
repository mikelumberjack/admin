import time

from Locators.locators import Locators
from Pages.cartPage import Cart
from Pages.catalogPage import Catalog
from Pages.loginPage import LoginPage
from Pages.menu import Menu
from Tests.basetestcase import BaseTestCase


class Checkout(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        login = LoginPage(cls.driver)
        login.logging_in()

    def test_order_process(self):
        driver = self.driver
        menu = Menu(driver)
        catalog = Catalog(driver)
        cart = Cart(driver)

        menu.go_to_catalog()
        catalog.select_category('HEALTH')
        catalog.select_sub_category('HERBALS')
        catalog.check_product('175845')
        catalog.check_product('175844')
        catalog.add_to_shopping_cart()

        cart.firstname('Mike')
        cart.lastname('Test')
        cart.city('Tbilisi')
        cart.street('Char')
        cart.zip('25345')
        cart.country(52)
        cart.shipping(1)
        cart.checkout()
        cart.low_balance()


