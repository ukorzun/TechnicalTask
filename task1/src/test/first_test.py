import pytest


class TestUniqueVisitors:

    @pytest.mark.parametrize("popularity_threshold",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_popularity_threshold(self, popularity_threshold, go_to_wikipedia_page):
        websites_info = go_to_wikipedia_page.extract_table_data()

        errors = [
            f"{website.name} has {website.popularity} unique visitors per month. "
            f"(Expected more than {popularity_threshold})"
            for website in websites_info if website.popularity < popularity_threshold
        ]

        assert not errors, f"Test failed with the following errors:\n{', '.join(errors)}"
