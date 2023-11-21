import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    try:
        driver = webdriver.Chrome()
        yield driver
    finally:
        driver.quit()

