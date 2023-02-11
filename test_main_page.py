from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators


def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.URL
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

