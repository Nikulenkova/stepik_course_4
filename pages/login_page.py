from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Неверный URL для входа в систему"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма входа в систему не представлена"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Регистрационная форма не представлена"
        assert True

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.NAME, "registration-email")
        password_input1 = self.browser.find_element(By.NAME, "registration-password1")
        password_input2 = self.browser.find_element(By.NAME, "registration-password2")
        register_button = self.browser.find_element(By.NAME, "registration_submit")

        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        register_button.click()
