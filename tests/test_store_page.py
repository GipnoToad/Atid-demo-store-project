import pytest
from pages.store_page import StorePage

url = "https://atid.store/store/"

@pytest.mark.smoke
def test_user_can_access_store_page(browser):
    store_page = StorePage(browser, url)
    store_page.open()
    store_page.is_store_page()