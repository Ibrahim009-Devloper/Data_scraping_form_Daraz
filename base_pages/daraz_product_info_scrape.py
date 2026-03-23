from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import pandas as pd
import os




class Daraz_product_info_scraper():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)
        self.enter_product_name_el = (By.XPATH,"//input[contains(@placeholder,'Search in Daraz')]")
        self.click_scarch_btn_el = (By.XPATH,"//a[contains(text(),'SEARCH')]")
        self.click_products_detels_el = (By.XPATH,"//div[contains(@data-tracking,'product-card')]")
        self.product_name_el = (By.XPATH,"//h1[contains(@class,'product-badge-title')]")
        self.product_price_el = (By.XPATH,"(//div[contains(@class,'product-price')]//span)[1]")
        self.product_reating_el = (By.XPATH,"//a[contains(@class,'pdp-review-summary__l')]")
        self.click_next_page_el = (By.XPATH,"//li[contains(@title,'Next Page')]")

    def enter_product_name(self,product_name:str):
        name = self.wait.until(EC.visibility_of_element_located(self.enter_product_name_el))
        name.clear()
        name.send_keys(product_name)

    def click_scarch_btn(self):
        scarch_btn = self.wait.until(EC.element_to_be_clickable(self.click_scarch_btn_el))
        self.driver.execute_script("arguments[0].click();",scarch_btn)


    def get_product_info(self,total_page:int):
        folder_name = "test_data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_path = os.path.join(folder_name,"product_info.xlsx")
        add_number = 0
        product_info = []
        try:
            for page in range(total_page):
                print(f"currently scraping {page + 1} no. page")
                self.wait.until(EC.visibility_of_all_elements_located(self.click_products_detels_el))
                count = len(self.driver.find_elements(*self.click_products_detels_el))
                
                print(f"found {count} products")
                for i in range(count):
                    products = self.wait.until(EC.visibility_of_all_elements_located(self.click_products_detels_el))
                    current_products = products[i]
                    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",current_products)
                    current_products.click()
                    add_number += 1
                    product_name = self.wait.until(EC.visibility_of_element_located(self.product_name_el)).text
                    product_price = self.wait.until(EC.visibility_of_element_located(self.product_price_el)).text
                    product_rating = self.wait.until(EC.visibility_of_element_located(self.product_reating_el)).text
                    
                    product_info.append({
                        "SL NO.": add_number,
                        "Product Name": product_name,
                        "Product Price": product_price,
                        "Product Rating": product_rating
                    })
                    with open("product_info.txt","a",encoding="utf-8") as f:
                        f.write(f"{add_number}:    product name: {product_name}\n\tproduct price: {product_price}\n\tproduct rating: {product_rating}")
                    
                    self.driver.back()

                if page < total_page - 1:
                    try:
                        next_btn = self.wait.until(EC.element_to_be_clickable(self.click_next_page_el))
                        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",next_btn)
                        self.driver.execute_script("arguments[0].click();",next_btn)
                        time.sleep(2)
                        print("moving the next page.....")
                    except Exception as e:
                        print(e)
                        print("no next page found or all page has been scraped")
        except KeyboardInterrupt:
            print("you stoped the scraper")
        finally:

            if product_info:
                df = pd.DataFrame(product_info)
                df.to_excel(file_path,index=False)
                print(f"Success! 'products_list.xlsx' created with {len(product_info)} items.")
            else:
                print("Data not save to products_list.slsx file")

        
            
            
            

        



        
