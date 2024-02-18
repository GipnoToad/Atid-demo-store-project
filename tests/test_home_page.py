import pytest
from pages.home_page import HomePage
from pages.store_page import StorePage

url = "https://atid.store/"

@pytest.mark.smoke
def test_user_can_access_home_page(browser):
    home_page = HomePage(browser, url)
    home_page.open()
    home_page.is_home_page()

def test_user_can_access_store(browser):
    home_page = HomePage(browser, url)
    home_page.open()
    home_page.is_home_page()
    home_page.click_store_page_button()
    store_page = StorePage(browser, browser.current_url)
    store_page.is_store_page()


# test_user_can_access_to_cart()
    # открыть страницу
    # проверить, что она открыта
    # нажать на кнопку корзины
    # проверить, что корзина открыта

# test_cart_icon_can_change_values()
    # открыть страницу товара
    # проверить что она открыта
    # изменить количество товара
    # нажать кнопку "добавить"
    # проверить сумму корзины
    # проверить количество товара на иконке корзины

# test_user_can_add_product_to_cart()
    # открыть страницу товара
    # проверить что она открыта
    # изменить количество товара
    # нажать кнопку "добавить"
    # нажать на корзину
    # проверить, что корзина открыта
    # проверить, что товар отображается

# test_user_can_remove_product_from_cart()
    # открыть страницу товара
    # проверить что она открыта
    # изменить количество товара
    # нажать кнопку "добавить"
    # нажать на корзину
    # проверить, что корзина открыта
    # проверить, что товар отображается
    # нажать remove кнопку
    # проверить, что товара больше нет

