from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), 'Error: basket not empty'

    def should_be_basket_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), 'Error: basket empty'

    def should_not_be_disappeared_content_basket(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_NOT_EMPTY), \
            'Error: basket not empty'

    def should_be_messages_basket_empty(self):
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text, \
            'Error: message not found'
