import time

import pytest

from pages.base_page import BasePage
from pages.product_page import ProductPage


@pytest.mark.parametrize(
    'link',
    [
        (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
         if i != 7
         else pytest.param(
             f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}",
             marks=pytest.mark.xfail(reason='Ошибка: Название товара не соответствует наименованию товара '
                                            'в сообщении об успешном добавлении товара в корзину')
         ))
        for i in range(10)
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    BasePage.solve_quiz_and_get_code(product_page)
    product_page.the_product_name_matches_the_name_in_the_message()
    product_page.the_cost_of_the_basket_coincides_with_the_price_of_the_goods()
