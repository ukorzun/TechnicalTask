import pytest

from task1.pages.wikipedia_page import WikipediaProgrammingLanguagesPage


class TestUniqueVisitors:

    @pytest.mark.parametrize("popularity_threshold",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_popularity_threshold(self, popularity_threshold, chrome_driver):
        with chrome_driver:
            wikipedia_page = WikipediaProgrammingLanguagesPage(chrome_driver)
            wikipedia_page.navigate_to_page()

            websites_info = wikipedia_page.extract_table_data()
            errors = self.check_popularity_threshold(websites_info, popularity_threshold)
            # 3 out of 7 will fail and display an error because they do not meet the "unique visitors per month condition. Expected more than"
            if errors:
                for error in errors:
                    print(error)
                raise AssertionError(f"Test failed with the following errors:\n{', '.join(errors)}")

    def check_popularity_threshold(self, websites_info, popularity_threshold):
        formatted_errors = []

        for website_info in websites_info:
            website_name = website_info.get('websites')
            frontend = website_info.get('frontend')
            backend = website_info.get('backend')
            popularity = self.clean_numeric_string(website_info.get('popularity'))
            if popularity is not None and popularity < popularity_threshold:
                error_message = f"{website_name} (Frontend:{frontend}|Backend:{backend}) has {popularity} unique visitors per month. (Expected more than {popularity_threshold})"
                formatted_errors.append(error_message)

        return formatted_errors

    def clean_numeric_string(self, value):
        try:
            return int(float(str(value).replace(',', '')))
        except ValueError:
            return None
