from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class BasePage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_clickable(self, locator: tuple, wait=5):
        try:
            elem = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable(locator))
            elem.click()
        except exceptions.TimeoutException:
            raise AssertionError(f'Element: {locator} is not clickable.')
        except exceptions.ElementClickInterceptedException as click:
            raise AssertionError(f"Element: {locator} was not cliked due {click}")

    # def click_element(self, locator: tuple):
    #     try:
    #         elem = self.element_is_clickable(locator)
    #         elem.click()
    #     except:
    #         raise AssertionError(f'Failed to click element: {locator}.')

    def element_is_visible(self, locator: tuple, wait=5):
        try:
            WebDriverWait(self.browser, wait).until(EC.visibility_of_element_located(locator))
            return True
        except:
            raise AssertionError(f'Element: {locator} is not visible.')

    def text_as_expected_text(self, locator:tuple, text: str):
        try:
            elem = self.browser.find_element(*locator)
            assert elem.text == text, f"Expected text: {text}. Actual text: {elem.text}"
        except exceptions.NoSuchElementException:
            raise AssertionError(f'Element: {locator} is not found.')

