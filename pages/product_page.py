import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.test_guest_can_add_product_to_basket()
        self.test_to_equal_price_after_add_to_basket()
        self.test_to_equal_name_product_after_add_to_basket()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        # Поиск название продукта на странице
        # current_product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        current_product_name = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(ProductPageLocators.NAME_PRODUCT))\
            .text
        # Форматирование название продукта со страницы, под проверку в URL
        formatted_current_product_name = current_product_name.lower().replace(" ", "-").replace("'", "")
        assert (formatted_current_product_name in current_url), "wrong url link"

    def test_guest_can_add_product_to_basket(self):
        # login_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        login_link = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(ProductPageLocators.BUTTON_ADD_TO_BASKET))
        login_link.click()
        BasePage.solve_quiz_and_get_code(self)
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "Product is not added to basket"

    def test_to_equal_price_after_add_to_basket(self):
        # product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_PRICE))\
            .text
        #price_at_alert = self.browser.find_element(*ProductPageLocators.ADDED_PRICE_IN_ALERT).text
        price_at_alert = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(ProductPageLocators.ADDED_PRICE_IN_ALERT))\
            .text
        assert product_price == price_at_alert, "Product price in alert not equal to price in cart"

    def test_to_equal_name_product_after_add_to_basket(self):
        # product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        product_name = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(ProductPageLocators.NAME_PRODUCT))\
            .text
        # name_at_alert = self.browser.find_element(*ProductPageLocators.ADDED_NAME_IN_ALERT).text
        name_at_alert = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(ProductPageLocators.ADDED_NAME_IN_ALERT))\
            .text
        assert product_name == name_at_alert, "Product name in alert not equal to price in cart"
