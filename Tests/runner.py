if __name__ == "__main__":
    import unittest
    from Tests.login import LoginAdminTest
    from Tests.add_remove_inventory import AddToInventoryTest
    from Tests.add_remove_cart import CartTest
    from Tests.magento_proc import Checkout
    import HtmlTestRunner
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(LoginAdminTest),
                                loader.loadTestsFromTestCase(AddToInventoryTest),
                                loader.loadTestsFromTestCase(CartTest),
                                loader.loadTestsFromTestCase(Checkout)))
    # loader_v2.loadTestsFromTestCase(LoginAdminTest)
    # loader_v2.loadTestsFromTestCase(AddToInventory)
    # loader_v2.loadTestsFromTestCase(CartTest)
    # unittest.TextTestRunner().run(suite)
    # suite = unittest.TestSuite()
    # suite.addTest(AddToInventoryTest('test_add_remove_inventory'))
    runner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/Admin/Documents/Admin/reports")
    runner.run(suite)
