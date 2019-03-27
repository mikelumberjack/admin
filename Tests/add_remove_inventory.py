import time

from Tests.basetestcase import BaseTestCase
from Pages.loginPage import LoginPage
from Pages.catalogPage import Catalog
from Pages.inventoryPage import Inventory
from Pages.menu import Menu
from ddt import ddt, data, unpack


@ddt
class AddToInventoryTest(BaseTestCase):
    """Adding from catalog to inventory and removing"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        login = LoginPage(cls.driver)
        login.logging_in()

    @data(*BaseTestCase.get_data('C:/Users/Admin/Documents/Admin/CSV/add_to_inventory.csv'))
    @unpack
    def test_add_remove_inventory(self, category, sub_category, *id_product):
        driver = self.driver
        menu = Menu(driver)
        inventory = Inventory(driver)
        catalog = Catalog(driver)

        menu.go_to_catalog()
        catalog.select_category(category)
        catalog.select_sub_category(sub_category)
        for i in id_product:
            catalog.check_product(i)
        selected_items = catalog.get_selected_items()
        self.assertEqual(len(selected_items), catalog.get_quantity_selected_items())
        catalog.add_to_inv_main()

        menu.go_to_inventory()
        inventory.select_category(category)
        inventory.select_sub_category(sub_category)
        total = inventory.get_total_items()
        self.assertEqual(len(selected_items), total)
        for i in id_product:
            inventory.check_product(i)
        inventory.remove_from_inventory()
        inventory.confirm()
        driver.refresh()

    def test_add_more_than_100(self):
        driver = self.driver
        menu = Menu(driver)
        catalog = Catalog(driver)
        inventory = Inventory(driver)

        menu.go_to_catalog()
        catalog.select_category('FASHION')
        catalog.select_sub_category('UNDERWEAR')
        catalog.select_all()
        total_items = catalog.get_total_on_page()
        selected_items = catalog.get_quantity_selected_items()
        self.assertEqual(total_items, selected_items, '{},{}'.format(total_items, selected_items))
        catalog.add_to_inv_main()
        catalog.all_products_sync_to_inv()

        menu.go_to_inventory()
        inventory.select_category('FASHION')
        inventory.select_category('UNDERWEAR')
        inventory.select_all()
        inv_total_items = catalog.get_total_on_page()
        inv_selected_items = catalog.get_quantity_selected_items()
        self.assertEqual(inv_total_items, inv_selected_items, '{},{}'.format(inv_total_items, inv_selected_items))
        self.assertEqual(inv_total_items, total_items, '{},{}'.format(inv_total_items, total_items))
        inventory.remove_from_inventory()
        inventory.confirm()



