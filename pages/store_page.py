from ._locators import StorePageLocators
from .base_page import BasePage

class StorePage(BasePage):
    def is_store_page(self):
        self.element_is_visible(StorePageLocators.CATEGORIES_TITLE)
        self.text_as_expected_text(StorePageLocators.CATEGORIES_TITLE, "Categories")
        self.element_is_clickable(StorePageLocators.CATEGORIES_TITLE)

    def choose_products(self):
        self.element_is_clickable(StorePageLocators.PRODUCTS_TABLE)
        self.click_all_elements_in_list(StorePageLocators.PRODUCTS_TABLE)

    def choose_product(self):
        self.element_is_clickable(StorePageLocators.PRODUCT)
        product_name = self.get_element_name(StorePageLocators.PRODUCT_NAME_IN_CATALOG)
        self.click_element(StorePageLocators.PRODUCT)
        return product_name