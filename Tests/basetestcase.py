import csv
import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Admin/Documents/Admin/Drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @staticmethod
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
