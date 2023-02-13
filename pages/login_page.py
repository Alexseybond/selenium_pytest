from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert ("login" in current_url), "wrong url link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email_to_register: str, password_to_register: str):
        email = WebDriverWait(self.browser, timeout=5) \
            .until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        email.send_keys(email_to_register)
        password = WebDriverWait(self.browser, timeout=5) \
            .until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        password.send_keys(password_to_register)
        confirm_password = WebDriverWait(self.browser, timeout=5) \
            .until(EC.presence_of_element_located(LoginPageLocators.CONFIRM_PASSWORD_FIELD))
        confirm_password.send_keys(password_to_register)
        register_button = WebDriverWait(self.browser, timeout=5) \
            .until(EC.presence_of_element_located(LoginPageLocators.REGISTER_BUTTON))
        register_button.click()

    def delete_registered_user(self):
        pass  # На обучающем сайте не реализован способ удаление пользователя, по этому просто заглушка
