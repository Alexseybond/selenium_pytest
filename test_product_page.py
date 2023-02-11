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

