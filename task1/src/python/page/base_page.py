from task1.src.utils.config import Config


class BasePage:
    config_instance = Config()

    BASE_URL = config_instance.config.get('Settings', 'BASE_URL')

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.BASE_URL

    def open_url(self, path):
        self.driver.get(f"{self.BASE_URL}{path}")
