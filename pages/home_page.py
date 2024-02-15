from ._locators import HomePageLocators
from .base_page import BasePage

class HomePage(BasePage):
    def is_home_page(self):
        self.element_is_visible(HomePageLocators.HOME_PAGE_TITLE)
        self.text_as_expected_text(HomePageLocators.HOME_PAGE_TITLE, "ATID Demo Store")
        
