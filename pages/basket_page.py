from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_the_text_your_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'Текст -Ваша корзина пуста- отсутствует!'

    def should_not_be_no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), 'В корзине есть товар!'
