class BasePage:
    BASE_URL = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.BASE_URL
