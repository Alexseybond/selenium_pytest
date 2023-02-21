from faker import Faker
import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators, LoginPageLocators
from pages.locators import PromoLinks


@pytest.mark.need_review
@pytest.mark.parametrize("endpoint", PromoLinks.ENDPOINTS)
def test_login_url(browser, endpoint):
    link = f"{PromoLinks.LINK}{endpoint}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


@pytest.mark.need_review
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = PromoLinks.LINK_WITHOUT_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.should_be_guest_add_product_to_basket()
    page.is_not_element_present(*ProductPageLocators.ALERT_WITH_ADDED_BOOK)


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = PromoLinks.LINK_WITHOUT_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.should_be_guest_add_product_to_basket()
    page.is_disappeared(*ProductPageLocators.ALERT_WITH_ADDED_BOOK)


    @pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = PromoLinks.LINK_WITHOUT_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_basket_is_empty()


@pytest.mark.login_as_register_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LoginPageLocators.URL
        page = LoginPage(browser, link)
        page.open()
        fake = Faker()
        page.register_new_user(fake.email(), fake.password())
        page.should_be_authorized_user()
        yield
        page.delete_registered_user()

    @pytest.mark.xfail(reason="Negative checks")
    def test_user_cant_see_success_message(self, browser):
        link = PromoLinks.LINK_WITHOUT_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.ALERT_WITH_ADDED_BOOK)

    def test_user_can_add_product_to_basket(self, browser):
        link = PromoLinks.LINK_WITHOUT_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.should_be_guest_add_product_to_basket()

