from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        field_email = WebDriverWait(self.browser, 4).until(
                EC.presence_of_element_located((By.NAME, 'registration-email'))
            )
        field_email.send_keys(email)
        field_password = WebDriverWait(self.browser, 4).until(
                EC.presence_of_element_located((By.NAME, 'registration-password1'))
            )
        field_password.send_keys(password)
        field_confirm_password = WebDriverWait(self.browser, 4).until(
                EC.presence_of_element_located((By.NAME, 'registration-password2'))
            )
        field_confirm_password.send_keys(password)
        button_registration = WebDriverWait(self.browser, 4).until(
                EC.element_to_be_clickable((By.NAME, 'registration_submit'))
            )
        button_registration.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Error: Invalid link'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
