from pages.login_page import LoginPage
from pages.locators import LoginPageLocators


def test_login_url(browser):
    link = LoginPageLocators.URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
