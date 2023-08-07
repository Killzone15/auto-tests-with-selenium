from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()

