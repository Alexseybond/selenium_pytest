from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
