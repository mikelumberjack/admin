import time

from Tests.basetestcase import BaseTestCase
from Pages.loginPage import LoginPage
from Pages.catalogPage import Catalog
from Pages.cartPage import Cart
from Pages.menu import Menu
from ddt import ddt, data, unpack


@ddt
class CartTest(BaseTestCase):
    """Adding from catalog to inventory and removing"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        login = LoginPage(cls.driver)
        login.logging_in()

    @data(*BaseTestCase.get_data('C:/Users/Admin/Documents/Admin/CSV/add_to_cart.csv'))
    @unpack
    def test_add_remove_cart(self, category, sub_category, *id_product):
        """This method receive data from add_to_cart.csv - category, sub_category and list of product"""

        driver = self.driver
        menu = Menu(driver)
        catalog = Catalog(driver)
        cart = Cart(driver)

        menu.go_to_catalog()
        catalog.select_category(category)
        catalog.select_sub_category(sub_category)
        for i in id_product:
            catalog.check_product(i)
        selected_items = catalog.get_selected_items()
        catalog.add_to_shopping_cart()
        items_in_cart = cart.get_items_in_cart()
        self.assertEqual(len(selected_items), len(items_in_cart), 
                         "selected {}, added {}".format(len(selected_items), len(items_in_cart)))
        cart.remove_all_from_cart()
        self.assertTrue(cart.is_cart_empty())
