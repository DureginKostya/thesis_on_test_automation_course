from selenium.webdriver.common.by import By


class MainPageLocators():

    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group > a')


class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():

    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BUTTON_ADD_INTO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    MESSAGE_PRODUCT_ADD = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():

    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '.basket-items')

