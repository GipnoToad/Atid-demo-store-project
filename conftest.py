import pytest
from selenium import webdriver

def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--headless", action="store_true", 
                     help="Start browser in headless mode")


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest):
    options = webdriver.ChromeOptions()
    headless = request.config.getoption("headless")
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()









# import pytest
# from pytest import Parser
# from pytest import FixtureRequest
# from selenium import webdriver

# def pytest_addoption(parser: Parser):
#     parser.addoption("--headless", action="store_true",
#                      help="Run browser in headless mode")
#     parser.addoption("--lang", action="store", default="en-US",
#                      help="Define a language of the browser")

# @pytest.fixture(scope="function")
# def browser(request: FixtureRequest):
#     options = webdriver.ChromeOptions()
#     headless = request.config.getoption("headless")
#     if headless:
#         options.add_argument("--headless")
#         options.add_argument("--disable-gpu")
#     lang = request.config.getoption("lang")
#     options.add_argument(f"--lang={lang}")
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     browser.quit()