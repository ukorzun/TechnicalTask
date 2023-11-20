from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
from dataclasses import dataclass

from task1.pages.base_page import BasePage


@dataclass
class WebsiteInfo:
    name: str
    languages: str
    popularity: int


logger = logging.getLogger(__name__)


class WikipediaProgrammingLanguagesPage(BasePage):

    PROGRAMMING_TABLE_XPATH = (By.XPATH, "//table[.//caption[contains(text(), 'Programming languages used')]]")
    POPULARITY_THRESHOLD = 500000

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Navigate to Wikipedia page")
    def navigate_to_page(self):
        logger.info("Navigating to Wikipedia page")
        self.driver.get(self.BASE_URL)

    @allure.step("Wait for table to be present")
    def wait_for_table(self):
        logger.info("Waiting for the programming languages table to be present")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PROGRAMMING_TABLE_XPATH)
        )

    @allure.step("Extract table data")
    def extract_table_data(self):
        logger.info("Extracting data from the programming languages table")
        table = self.driver.find_element(*self.PROGRAMMING_TABLE_XPATH)
        rows = table.find_elements(By.XPATH, ".//tr[position() > 1]")

        data = []
        for index, row in enumerate(rows, start=2):
            try:
                website_info = self._process_table_row(row)
                if website_info:
                    data.append(website_info)
            except Exception as e:
                logger.error(f"Error processing row {index}: {str(e)}")

        return data

    @allure.step("Process table row")
    def _process_table_row(self, row):
        logger.info("Processing a row from the programming languages table")

        columns = row.find_elements(By.XPATH, "td")

        if not columns or len(columns) < 3 or not columns[2].text.replace(",", "").isdigit():
            self._log_skipped_row(columns)
            return None

        company_name = columns[0].text.strip()
        country = columns[1].text.strip()
        popularity = int(columns[2].text.strip().replace(",", ""))
        frontend_backend_info = self._get_frontend_backend_info(columns)

        if popularity < self.POPULARITY_THRESHOLD:
            error_message = f"{company_name} {frontend_backend_info} has {popularity} unique visitors per month. (Expected more than {self.POPULARITY_THRESHOLD})"
            logger.warning(f"Error: {error_message}")

        logger.info(f"Processed row {index}: Company Name - {company_name}, Country - {country}, Popularity - {popularity}, Languages - {frontend_backend_info}")

        return WebsiteInfo(
            name=company_name,
            languages=frontend_backend_info,
            popularity=popularity
        )

    @allure.step("Log skipped row")
    def _log_skipped_row(self, columns):
        logger.warning("Skipping a row from the programming languages table")

        if len(columns) >= 3:
            logger.warning(f"Invalid popularity value: {columns[2].text.strip()}")
        else:
            logger.warning("Insufficient columns")

    @allure.step("Get frontend and backend info")
    def _get_frontend_backend_info(self, columns):
        logger.info("Getting frontend and backend information")

        if len(columns) >= 5:
            frontend_info = columns[3].text.strip()
            backend_info = columns[4].text.strip()
            return f"(Frontend:{frontend_info}|Backend:{backend_info})"
        else:
            return ""