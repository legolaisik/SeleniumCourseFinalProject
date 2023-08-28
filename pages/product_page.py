import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def open(self):
        super().open()
        self.name_product = self.get_name_product()
        self.price_product = self.get_price_product()

    def get_name_product(self):
        el_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return el_product_name.text

    def get_price_product(self):
        el_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = el_product_price.text.split("&")[0]
        return product_price

    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button add product to basket is not presented"

    def add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_match_name_added_product(self):
        assert self.is_alert_match(ProductPageLocators.ALERT_MAIN_INFO, self.name_product),\
            "Name of added product in alert is not match"

    def should_match_price_added_product(self):
        assert self.is_alert_match(ProductPageLocators.ALERT_MAIN_INFO, self.price_product),\
            "Price of added product in alert is not match"

    def should_match_added_product(self):
        self.should_match_name_added_product()
        self.should_match_price_added_product()
