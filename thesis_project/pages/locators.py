from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():

    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '.basket-items')
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class MainPageLocators():

    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group > a')


class ProductPageLocators():

    BUTTON_ADD_INTO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    MESSAGE_PRODUCT_ADD = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')
