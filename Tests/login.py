import unittest
import csv
from ddt import ddt, data, unpack
from Tests.basetestcase import BaseTestCase
from Pages.loginPage import LoginPage


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name)
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


@ddt
class LoginAdminTest(BaseTestCase):

    @data(*get_data('C:/Users/Admin/Documents/Admin/CSV/login_credentials.csv'))
    @unpack
    def test_login(self, username, password, result):
        driver = self.driver
        driver.get('http://www.staging.365dropship.com/')

        if result == 'pass':
            login = LoginPage(driver)
            login.click_on_login()
            login.switch_to_login_frame()
            login.enter_username(username)
            login.enter_password(password)
            login.click_submit_botton()
            driver.refresh()
            self.assertEqual("365Dropship - Home - Overview", driver.title)

        elif result == 'fail':
            login = LoginPage(driver)
            login.click_on_login()
            login.switch_to_login_frame()
            login.enter_username(username)
            login.enter_password(password)
            login.click_submit_botton()
            self.assertTrue(login.is_incorrect_displayed())


if __name__ == "__main__":
    unittest.main()

