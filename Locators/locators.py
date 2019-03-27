# noinspection SpellCheckingInspection
from typing import Tuple

from selenium.webdriver.common.by import By


class Locators(object):

    # loginPage
    LOGIN = (By.LINK_TEXT, 'LOGIN')
    LOGIN_FRAME = (By.ID, 'fancybox-frame')
    USERNAME = (By.ID, 'login-username')
    PASSWORD = (By.ID, 'login-password')
    LOGIN_SUBMIT_BOTTON = (By.XPATH, '//*[@id="login_form"]/input')
    INCORECT_USER_PASS = (By.XPATH, '/html/body/div[2]')

    # menu
    HOME_ICON = (By.XPATH, '//*[@id="wrapper"]/header/div/div/a/img')
    PROFILE_ICON = (By.XPATH, '//*[@id="nav"]/ul/li[1]/a')
    DASHBOARD_ICON = (By.CSS_SELECTOR, 'a.icon-speed')
    CATALOG_ICON = (By.CSS_SELECTOR, "a.icon-sale")
    INVENTORY_ICON = (By.CSS_SELECTOR, 'a.icon-heart')
    CART_ICON = (By.CSS_SELECTOR, 'a.icon-basket')
    ORDERS_ICON = (By.CSS_SELECTOR, 'a.icon-box')
    TRANSACTIONS_ICON = (By.CSS_SELECTOR, 'a.icon-bank')
    STORES_LIST_ICON = (By.CSS_SELECTOR, 'a.icon-shop-a ')

    # profile

    SIGN_OUT = (By.LINK_TEXT, 'Sign Out')

    # catalogPage
    SELECT_CATEGORY = (By.XPATH, '//div/div/form/fieldset/span[1]/span[1]')
    CATEGORY_ITEMS = (By.XPATH, '//div/span/span/ul/li/span')
    SELECT_SUB_CATEGORY = (By.XPATH, '//div/div/form/fieldset/span[2]/span[1]')
    SUB_CATEGORY_ITEMS = (By.XPATH, '//span/ul/li/span')
    SELECT_ALL = (By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/span[1]/div')
    SELECT_ALL_FILTER = (By.XPATH, '//*[@id="nav"]/ul/li[3]/div/div/form/fieldset/div[2]/div/span/span/div')
    ADD_TO_INV = (By.LINK_TEXT, 'ADD TO MY INVENTORY')
    ADD_TO_CART = (By.LINK_TEXT, 'ADD TO SHOPPING CART')
    QUANTITY_OF_SELECTED_ITEMS = (By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/a')
    TOTAL_ITEM = (By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/em')
    POP_UP_BUTTON_SYNCED = (By.CSS_SELECTOR, 'button[class="sync-button sync_complete"]')
    ALL_SELECTED = (By.CSS_SELECTOR, 'a.check')


    # inventoryPage
    REMOVE_FROM_INVENTORY = (By.LINK_TEXT, 'REMOVE FROM MY INVENTORY')
    CONFIRM_REMOVE_BOTTOM = (By.LINK_TEXT, 'CONFIRM')

    # cartPage
    REMOVE_FROM_CART = (By.XPATH, '//*[@id="cart"]/tbody/tr/td[1]/div[2]/div[3]/a')
    EMPTY_ALERT = (By.CSS_SELECTOR, 'div.error-alert-box')
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    CITY = (By.ID, 'city')
    STREET = (By.ID, 'street')
    ZIP = (By.ID, 'manual_order_zip_input')
    EMAIL = (By.ID, 'email')
    PHONE = (By.ID, 'phone')
    COUNTRY = (By.ID, 'country_id_select')
    SHIP_METHOD = (By.CSS_SELECTOR, 'select[class="shipping_price_select jcf-hidden"]')
    CHECKOUT = (By.CSS_SELECTOR, 'button.checkout-button')
    CANCEL_POP_UP = (By.ID, 'cancel_info_dialog')



    # product_details
    ADD_TO_CART_PD = (By.LINK_TEXT, 'ADD TO CART')
    ADD_TO_INV_PD = (By.LINK_TEXT, 'ADD TO MY INVENTORY')
    SKU = (By.XPATH, '//*[@id="popup1"]/div/div/div[1]/h2')

    # storeListPage
    SYNC_NOW_BOTTON = (By.LINK_TEXT, 'SYNC NOW')
    ADD_REMOTE_STORE = (By.LINK_TEXT, 'Add Remote Store')
