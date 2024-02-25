from ._locators import StorePageLocators
from .base_page import BasePage

class StorePage(BasePage):
    def is_store_page(self):
        self.element_is_visible(StorePageLocators.CATEGORIES_TITLE)
        self.text_as_expected_text(StorePageLocators.CATEGORIES_TITLE, "Categories")

    def choose_product(self):
        self.element_is_visible(StorePageLocators.PRODUCTS_TABLE)
        self.elements_are_clickable(StorePageLocators.PRODUCTS_TABLE)
