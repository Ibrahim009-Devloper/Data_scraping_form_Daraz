from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import pytest


@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximize")
    options.add_argument("--disable-notification")
    proxis = {
        "proxy": {
           'http':'http://ubjspuvp:e647p61568pg@23.95.150.145:6114',
            'https':'https://ubjspuvp:e647p61568pg@23.95.150.145:6114'
        }
    }

    driver = uc.Chrome(seleniumwire_options=proxis,options=options)
    yield driver

    driver.quit()