from Pages.catalogPage import Catalog
from Pages.inventoryPage import Inventory
from Pages.loginPage import LoginPage
from Pages.menu import Menu
from Pages.storesListPage import Stores
from Tests.basetestcase import BaseTestCase


class SyncTest(BaseTestCase):
    """Sync"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        login = LoginPage(cls.driver)
        login.logging_in()

    def test_store_sync(self):
        driver = self.driver
        menu = Menu(driver)
        catalog = Catalog(driver)
        inventory = Inventory(driver)
        stores = Stores(driver)

        menu.go_to_catalog()
        catalog.select_category("FASHION")
        catalog.select_sub_category("SHIRTS")
        catalog.select_all()
        selected_items = catalog.get_selected_items()
        catalog.add_to_inv_main()
        menu.go_to_inventory()
        inventory.get_total_items()
        menu.go_to_store_list()
        stores.sync_now()
