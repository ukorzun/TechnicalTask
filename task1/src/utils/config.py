import os
from configparser import ConfigParser


class Config:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        config = ConfigParser()
        config_path = self.find_config_file()
        config.read(config_path)
        return config

    def find_config_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.join(current_dir, "../../")

        # Ищем файл config.ini в проекте
        for root, dirs, files in os.walk(project_root):
            if "config.ini" in files:
                return os.path.join(root, "config.ini")

        raise FileNotFoundError("File 'config.ini' not found in the project.")
