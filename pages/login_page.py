from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        if "login" in self.browser.current_url:
            assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), \
                "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
       self.browser.find_element(*LoginPageLocators.REGISTER_EMAIl).send_keys(email)
       self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
       self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
       self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTER).click()
