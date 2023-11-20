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

    def wait_for_table(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PROGRAMMING_TABLE_XPATH)
        )


    def extract_table_data(self):
        table = self.driver.find_element(*self.PROGRAMMING_TABLE_XPATH)
        rows = table.find_elements(By.XPATH, "//tr[position() > 1]")

        data = []

        for index, row in enumerate(rows, start=1):
            columns = row.find_elements(By.XPATH, "td")

            if len(columns) < 4:
                logger.warning(f"Skipping row {index}: {columns[0].text.strip()} - Insufficient columns")
                continue

            websites = columns[0].text.strip()

            match = re.search(r'\d{1,3}(?:[.,]\d{3})*(?:\.\d*)?(?:\D|$)', columns[1].text.strip())

            if not match:
                logger.warning(f"Skipping row {index}: {websites} - No valid popularity value found")
                continue

            popularity_text = re.sub(r'[.,]', '', match.group())

            frontend = columns[2].text.strip()
            backend = columns[3].text.strip()

            try:
                popularity = int(popularity_text)
                data.append(WebsiteInfo(websites, popularity, frontend, backend))
                logger.warning(f"Added: {websites}, {popularity}, {frontend}, {backend}")
            except ValueError:
                logger.warning(f"Skipping row {index}: {websites} - Invalid popularity value: {popularity_text}")

        else:
            logger.warning("Table data extraction completed.")

        return data