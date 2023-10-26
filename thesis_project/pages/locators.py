from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():

    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BUTTON_ADD_INTO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    MESSAGE_PRODUCT_ADD = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')
