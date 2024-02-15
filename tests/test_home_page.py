import pytest
from pages.home_page import HomePage

url = "https://atid.store/"

@pytest.mark.smoke
def test_user_can_access_home_page(browser):
    home_page = HomePage(browser, url)
    home_page.open()
    home_page.is_home_page()
