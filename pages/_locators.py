from selenium.webdriver.common.by import By

class HomePageLocators:
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, "h1.elementor-heading-title")
    STORE_PAGE_BUTTON = (By.CSS_SELECTOR, "#menu-item-45 a")

class StorePageLocators:
    CATEGORIES_TITLE = (By.CSS_SELECTOR, "#woocommerce_product_categories-2 h2")
    PRODUCTS_TABLE = (By.CSS_SELECTOR, ".astra-shop-thumbnail-wrap")
    PRODUCT = (By.CSS_SELECTOR, ".products li:nth-child(1)")
    PRODUCT_NAME_IN_CATALOG = (By.CSS_SELECTOR, ".products li:nth-child(1) h2")
    
class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, '[name="add-to-cart"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_title")