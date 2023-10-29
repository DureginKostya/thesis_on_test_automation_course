from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def go_to_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_INTO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        return name_product, price_product

    def should_be_button_add_into_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_INTO_BASKET), \
            'Error: not found button add product into basket'

    def should_be_messages_product(self, name, price):
        self.should_be_message_product_add()
        self.validation_name_product_into_message(name)
        self.should_be_total_price()
        self.validation_total_price(price)

    def should_be_message_product_add(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD), \
            'Error: product not add into basket'

    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            'Error: not found element'

    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            'Error: not found element'

    def should_be_product_page(self):
        self.should_be_name_product()
        self.should_be_price_product()
        self.should_be_button_add_into_basket()

    def should_be_total_price(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_BASKET), \
            'Error: not total price basket'

    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_ADD), \
            'Success message is presented, but should not be'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD), \
            'Success message is presented, but should not be'

    def validation_name_product_into_message(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADD).text, \
            f'Error: should be name {name}'

    def validation_total_price(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_BASKET).text, \
            f'Error: should be price {price}'
