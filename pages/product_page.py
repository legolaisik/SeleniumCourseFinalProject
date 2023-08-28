import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button add product to basket is not presented"

    def add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_match_name_added_product(self):
        assert self.is_alert_match(ProductPageLocators.ALERT_MAIN_INFO, "The shellcoder's handbook"),\
            "Name of added product in alert is not match"

    def should_match_price_added_product(self):
        assert self.is_alert_match(ProductPageLocators.ALERT_MAIN_INFO, "£9.99"),\
            "Price of added product in alert is not match"

    def should_match_added_product(self):
        self.should_match_name_added_product()
        self.should_match_price_added_product()
