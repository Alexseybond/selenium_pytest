from dataclasses import dataclass
from typing import List

import pytest
from selenium.webdriver.common.by import By


@dataclass(init=False, frozen=True)
class MainPageLocators:
    URL: str = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK: tuple = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK: tuple = (By.CSS_SELECTOR, ".btn-group>a.btn")


@dataclass(init=False, frozen=True)
class LoginPageLocators:
    URL: str = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    PAGE_TITLE: str = "Login or register | Oscar - Sandbox"
    LOGIN_FORM: tuple = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM: tuple = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON: tuple = (By.CSS_SELECTOR, "#register_form>button.btn.btn-lg.btn-primary")


@dataclass(init=False, frozen=True)
class ProductPageLocators:
    URL: str = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PAGE_TITLE: str = "The shellcoder's handbook | Oscar - Sandbox"
    BUTTON_ADD_TO_BASKET: tuple = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_WITH_ADDED_BOOK: tuple = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    ALERT_SUCCESS: tuple = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_PRICE: tuple = (By.CSS_SELECTOR, ".product_main>.price_color")
    NAME_PRODUCT: tuple = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')
    ADDED_PRICE_IN_ALERT: tuple = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner>p>strong")
    ADDED_NAME_IN_ALERT: tuple = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    ADD_TO_BASKET_BUTTON: tuple = (By.CSS_SELECTOR, '.btn-add-to-basket')


@dataclass(init=False, frozen=True)
class PromoLinks:
    LINK: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    LINK_WITHOUT_PROMO: str = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    ENDPOINTS: list = List["0", "1", "2", "3", "4", "5", "6", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]


@dataclass(init=False, frozen=True)
class BasePageLocators:
    LOGIN_LINK: tuple = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID: tuple = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON: tuple = (By.CSS_SELECTOR, ".icon-user")


@dataclass(init=False, frozen=True)
class BasketPageLocators:
    PAGE_TITLE: str = "Basket | Oscar - Sandbox"
    TEXT_BASKET_IS_EMPTY: tuple = (By.CSS_SELECTOR, "#content_inner>p")
