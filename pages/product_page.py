from ._locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def is_product_page(self):
        self.element_is_visible(ProductPageLocators.ADD_TO_CART)
        self.text_as_expected_text(ProductPageLocators.ADD_TO_CART, "ADD TO CART")

    def is_chosen_product_correct(self):
        self.element_is_visible(ProductPageLocators.PRODUCT_NAME)
        product_title = self.get_element_name(ProductPageLocators.PRODUCT_NAME)
        return product_title