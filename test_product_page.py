import time

import pytest

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import PromoLinks


@pytest.mark.parametrize("endpoint", PromoLinks.ENDPOINTS)
def test_login_url(browser, endpoint):
    link = f"{PromoLinks.LINK}{endpoint}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = PromoLinks.LINK_WITHOUT_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_add_product_to_basket()
    page.is_not_element_present(*ProductPageLocators.ALERT_WITH_ADDED_BOOK)


@pytest.mark.xfail(reason="Negative checks")
def test_guest_cant_see_success_message(browser):
    link = PromoLinks.LINK_WITHOUT_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.ALERT_WITH_ADDED_BOOK)


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = PromoLinks.LINK_WITHOUT_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_add_product_to_basket()
    page.is_disappeared(*ProductPageLocators.ALERT_WITH_ADDED_BOOK)

