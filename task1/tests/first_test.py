import pytest


class TestUniqueVisitors:

    @pytest.mark.parametrize("popularity_threshold",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_popularity_threshold(self, popularity_threshold, go_to_wikipedia_page):
        websites_info = go_to_wikipedia_page.extract_table_data()

        errors = self.check_popularity_threshold(websites_info, popularity_threshold)

        assert not errors, f"Test failed with the following errors:\n{', '.join(errors)}"

    def check_popularity_threshold(self, websites_info, popularity_threshold):
        errors = []

        for website in websites_info:
            try:
                popularity = int(website.popularity)
                if popularity < popularity_threshold:
                    error_message = (
                        f"{website.websites} "
                        f"(Frontend:{website.frontend}|Backend:{website.backend}) "
                        f"has {popularity} unique visitors per month. (Expected more than {popularity_threshold})"
                    )
                    errors.append(error_message)
            except ValueError:
                error_message = (
                    f"Skipping row: {website.websites} - Invalid popularity value: {website.popularity}"
                )
                errors.append(error_message)

        return errors
