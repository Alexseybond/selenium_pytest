import dataclasses

import pytest
from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a.btn")


class LoginPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    PAGE_TITLE = "Login or register | Oscar - Sandbox"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PAGE_TITLE = "The shellcoder's handbook | Oscar - Sandbox"
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_WITH_ADDED_BOOK = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    NAME_PRODUCT = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')
    ADDED_PRICE_IN_ALERT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner>p>strong")
    ADDED_NAME_IN_ALERT = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')


class PromoLinks:
    LINK: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    LINK_WITHOUT_PROMO: str = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    ENDPOINTS: list = ["0", "1", "2", "3", "4", "5", "6", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
    # ENDPOINTS: list = ["0"]


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    PAGE_TITLE = "Basket | Oscar - Sandbox"
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
