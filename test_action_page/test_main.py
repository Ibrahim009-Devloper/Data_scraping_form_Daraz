from base_pages.daraz_product_info_scrape import Daraz_product_info_scraper
from utilities.read_propertice import read_config



class Test_Daraz_product_scraper():
    def test_scrape_product(self,setup):
        self.driver = setup
        self.driver.get(read_config.get_url())
        product_page = Daraz_product_info_scraper(self.driver)
        product_page.enter_product_name(read_config.get_product_name())
        product_page.click_scarch_btn()
        product_page.get_product_info(int(read_config.get_total_page()))


    








