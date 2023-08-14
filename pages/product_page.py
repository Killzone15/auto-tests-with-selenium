from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()

    def the_product_name_matches_the_name_in_the_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_MAIN)
        message_product_name = self.browser.find_element(*ProductPageLocators.NAME_MESSAGE_PRODUCT)
        assert product_name.text == message_product_name.text, 'Название товара не соотвествует ' \
                                                     'наименованию товара в сообщении ' \
                                                     'об успешном добавлении товара в корзину'

    def the_cost_of_the_basket_coincides_with_the_price_of_the_goods(self):
        price_product_main = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_MAIN)
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        assert price_product_main.text == price_in_message.text, 'Цена товара не соотвествует цене товара в сообщении'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
