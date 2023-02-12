from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert ("basket" in current_url), "wrong url link"

    def should_be_product_title(self):
        title = self.browser.title
        assert (BasketPageLocators.PAGE_TITLE == title), "wrong title at link"

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "Basket is not empty"


