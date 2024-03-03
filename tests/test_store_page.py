import pytest
from pages.store_page import StorePage
from pages.product_page import ProductPage

url = "https://atid.store/store/"

@pytest.mark.smoke
def test_user_can_access_store_page(browser):
    store_page = StorePage(browser, url)
    store_page.open()
    store_page.is_store_page()


def test_user_can_choose_products(browser):
    store_page = StorePage(browser, url)
    store_page.open()
    store_page.is_store_page()
    store_page.choose_products()


def test_product_chosen_by_user_is_correct(browser):
    store_page = StorePage(browser, url)
    store_page.open()
    store_page.is_store_page()
    store_product_name = store_page.choose_product()
    product_page = ProductPage(browser, browser.current_url)
    product_page.is_product_page()
    product_title = product_page.is_chosen_product_correct()
    assert store_product_name == product_title, "Product names do not match."
