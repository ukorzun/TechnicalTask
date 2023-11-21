from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import re
from dataclasses import dataclass

from task1.pages.base_page import BasePage


@dataclass
class WebsiteInfo:
    websites: str
    popularity: int
    frontend: str
    backend: str


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class WikipediaProgrammingLanguagesPage(BasePage):
    PROGRAMMING_TABLE_XPATH = (By.XPATH, "//table[.//caption[contains(text(), 'Programming languages used')]]")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_elements(self, parent_element, locator, timeout=10):
        return WebDriverWait(parent_element, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )


    def extract_table_data(self):
        column_names = {
            "websites": 0,
            "popularity": 1,
            "frontend": 2,
            "backend": 3
        }

        def extract_valid_popularity_text(popularity_column):
            match = re.search(r'[\d,.\[\]]+', popularity_column.text.strip())
            popularity_value = match.group() if match else ""
            popularity_value = re.sub(r'\.', '', popularity_value)
            return popularity_value

        table = self.wait_for_element(self.PROGRAMMING_TABLE_XPATH)
        rows = self.wait_for_elements(table, (By.XPATH, ".//tr[position() > 1]"))

        data = []

        for row in rows:
            columns = self.wait_for_elements(row, (By.XPATH, "td"))

            if len(columns) < len(column_names):
                logger.warning(f"Skipping row: {columns[0].text.strip()} - Insufficient columns")
                continue

            websites, popularity_text, frontend, backend = (
                columns[column_names["websites"]].text.strip(),
                extract_valid_popularity_text(columns[column_names["popularity"]]),
                columns[column_names["frontend"]].text.strip(),
                columns[column_names["backend"]].text.strip()
            )

            if not websites or not popularity_text:
                continue

            try:
                popularity = int(popularity_text.replace(",", "").replace("[", "").replace("]", ""))
            except ValueError:
                logger.warning(f"Skipping row: {websites} - Invalid popularity value: {popularity_text}")
                continue

            data.append({
                "websites": websites,
                "popularity": popularity,
                "frontend": frontend,
                "backend": backend
            })

        return data