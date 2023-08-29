from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"

    def should_not_be_basket_link(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LINK), "Basket link is presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LINK), "Items is presented in basket"
