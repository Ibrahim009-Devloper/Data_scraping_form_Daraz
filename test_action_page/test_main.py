from base_pages.daraz_product_info_scrape import Daraz_product_info_scraper
from utilities.read_propertice import read_config
from utilities.custom_loger import log_maker



class Test_Daraz_product_scraper():
    logger = log_maker.log_gen()
    def test_scrape_product(self,setup):
        self.logger.info("******Daraz product info scraper has been run********")
        self.driver = setup
        self.driver.get(read_config.get_url())
        self.logger.info("******sucessfully lounch the browser********")
        product_page = Daraz_product_info_scraper(self.driver)
        product_page.enter_product_name(read_config.get_product_name())
        product_page.click_scarch_btn()
        self.logger.info("******entered the product name and scarching the product********")
        product_page.get_product_info(int(read_config.get_total_page()))
        self.logger.info("******all the page has been scraped sucessfully********")
        


    








