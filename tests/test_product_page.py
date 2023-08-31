import time
import pytest
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


@pytest.mark.need_review
@pytest.mark.parametrize('link_num', [0, 1, 2, 3, 4, 5, 6,
                                      pytest.param(7, marks=pytest.mark.skip(reason="Название товара не соответствует "
                                                                                    "наименованию товара в сообщении "
                                                                                    "об успешном добавлении товара в "
                                                                                    "корзину")),
                                      8, 9])
def test_guest_can_add_product_to_basket(browser, link_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_num}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    BasePage.solve_quiz_and_get_code(product_page)
    product_page.the_product_name_matches_the_name_in_the_message()
    product_page.the_cost_of_the_basket_coincides_with_the_price_of_the_goods()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_no_products_in_the_basket()
    basket_page.should_be_the_text_your_basket_is_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + 'abcdfg'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        BasePage.solve_quiz_and_get_code(product_page)
        product_page.the_product_name_matches_the_name_in_the_message()
        product_page.the_cost_of_the_basket_coincides_with_the_price_of_the_goods()
