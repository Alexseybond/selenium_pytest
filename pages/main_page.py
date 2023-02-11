from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def go_to_login_page(self):
        # login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link = WebDriverWait(self.browser, timeout=5)\
            .until(EC.presence_of_element_located(MainPageLocators.LOGIN_LINK))
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

