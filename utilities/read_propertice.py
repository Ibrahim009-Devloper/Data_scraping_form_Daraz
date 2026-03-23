import configparser
import os


config = configparser.RawConfigParser()
base_page = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_page)
config_path = os.path.join(project_root,"configrations","config.ini")
config.read(config_path)

class read_config():
    @staticmethod
    def get_url():
        url = config.get("page url","url")
        return url
    
    @staticmethod
    def get_product_name():
        name = config.get("product name","name")
        return name
    
    @staticmethod
    def get_total_page():
        page = config.get("total scrape page","page")
        return page
    