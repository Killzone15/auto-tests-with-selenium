from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    WRITE_REVIEW = (By.CSS_SELECTOR, '#write_review')
    PRICE_PRODUCT_MAIN = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in '
                                         '> .alertinner strong')
    NAME_PRODUCT_MAIN = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    NAME_MESSAGE_PRODUCT = (By.CSS_SELECTOR, '#messages > '
                                             '.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) '
                                             '.alertinner strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > .alertinner')