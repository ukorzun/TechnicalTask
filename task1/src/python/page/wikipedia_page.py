import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataclasses import dataclass

from task1.src.python.page.base_page import BasePage


@dataclass
class WebsiteInfo:
    name: str
    languages: str
    popularity: int


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WikipediaPage(BasePage):
    PROGRAMMING_TABLE_XPATH = (By.XPATH, "//table[.//caption[contains(text(), 'Programming languages used')]]")

    @allure.step("Navigate to Wikipedia page")
    def navigate_to_page(self):
        self.driver.get(self.url)

    def wait_for_table(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PROGRAMMING_TABLE_XPATH)
        )

    @allure.step("Extract table data")
    def extract_table_data(self):
        table = self.driver.find_element(*self.PROGRAMMING_TABLE_XPATH)
        rows = table.find_elements(By.XPATH, "//tr[position() > 1]")

        data = []
        for row in rows:
            columns = row.find_elements(By.XPATH, "td")

            if columns and len(columns) >= 3 and columns[2].text.replace(",", "").isdigit():
                company_name = columns[0].text.strip()
                country = columns[1].text.strip()
                popularity = int(columns[2].text.strip().replace(",", ""))
                data.append({"company_name": company_name, "country": country, "popularity": popularity})
            else:
                if len(columns) >= 3:
                    logger.warning(
                        f"Skipping row: {columns[0].text.strip()} - Invalid popularity value: {columns[2].text.strip()}")
                else:
                    logger.warning(f"Skipping row: {columns[0].text.strip()} - Insufficient columns")

        return data
