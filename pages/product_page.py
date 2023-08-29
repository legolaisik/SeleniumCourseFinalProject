from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def open(self):
        super().open()
        self.name_product = self.get_name_product()
        self.price_product = self.get_price_product()

    def get_name_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button add product to basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_match_name_added_product(self):
        assert self.is_alert_match(ProductPageLocators.NAME_PRODUCT_IN_SUCCESS_MESSAGE, self.name_product),\
            "Name of added product in alert is not match"

    def should_match_price_added_product(self):
        assert self.is_alert_match(ProductPageLocators.PRICE_IN_INFO_MESSAGE, self.price_product),\
            "Price of added product in alert is not match"

    def should_match_added_product(self):
        self.should_match_name_added_product()
        self.should_match_price_added_product()
