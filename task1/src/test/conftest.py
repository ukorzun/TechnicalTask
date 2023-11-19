from task1.src.python.page.wikipedia_page import WikipediaPage
import pytest
from selenium import webdriver


@pytest.fixture
def setup_chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def go_to_wikipedia_page(setup_chrome_driver):
    wikipedia_page = WikipediaPage(setup_chrome_driver)
    wikipedia_page.navigate_to_page()
    wikipedia_page.wait_for_table()
    return wikipedia_page
