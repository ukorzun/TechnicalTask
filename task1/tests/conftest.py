import pytest
from selenium import webdriver

from task1.pages.wikipedia_page import WikipediaProgrammingLanguagesPage


@pytest.fixture
def chrome_driver_fixture():
    try:
        driver = webdriver.Chrome()
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def go_to_wikipedia_page(chrome_driver_fixture):
    wikipedia_page = WikipediaProgrammingLanguagesPage(chrome_driver_fixture)
    wikipedia_page.navigate_to_page()
    wikipedia_page.wait_for_table()
    return wikipedia_page
