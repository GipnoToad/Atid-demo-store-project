from selenium.webdriver.common.by import By

class HomePageLocators:
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, "h1.elementor-heading-title")
    STORE_PAGE_BUTTON = (By.CSS_SELECTOR, "#menu-item-45 a")

class StorePageLocators:
    CATEGORIES_TITLE = (By.CSS_SELECTOR, "#woocommerce_product_categories-2 h2")