from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

import time
from datetime import timedelta

# Open the browser as maximized 
opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

# Creating a driver object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)

# reading the csv file 
df = pd.read_csv('Credicxo/Amazon_Scraping_Sheet1.csv')
asins = df["Asin"]
countries = df["country"]
Product_list = []
web_404 = []

class Amazon:

    def title(self):

        # Scraping the Title of the product
        product_title = driver.find_element(By.ID,"productTitle").text
        return product_title

    def price(self):

      # Scraping the Product Price
        try:
            product_price = driver.find_element(By.XPATH,".//span[@class='a-color-base']").text
        except NoSuchElementException:
            product_price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[11]/div[1]/div[1]/span[1]/span[2]").text
        except Exception as e:
            print(e)
        return product_price

    def image(self):

      # Scraping the Product Image Url
        image_container = driver.find_element(By.ID,"main-image-container")
        product_img = image_container.find_element(By.TAG_NAME,"img").get_attribute("src")
        return product_img

    def details(self):

      # Scraping the Product Details
        try:
            product_details = driver.find_element(By.ID,"detailBullets_feature_div").text
        except NoSuchElementException:
            product_details = driver.find_element(By.ID,"productDetails_techSpec_section_1").text
        except Exception as e:
            print(e)
        return product_details


# start recording the time
start_time = round(time.time(),10)

# Looping the full csv data
for country,asin in zip(countries,asins):
    try:
      # Creating the webpage url
        web = f'https://www.amazon.{country}/dp/{asin}'

        # opening the webpage
        driver.get(web)
        website = Amazon()

        Product = {"Web_pageurl":web,"Product_Title":website.title(),"Product_price":website.price(),"Product_imagelink":website.image(),"Product_Details":website.details()}
        Product_list.append(Product)
        # print(Product_list)

    except:
        web_404.append(web)
        print(f"The {web} is not avaliable")

# Final time Recorded of Scraping
end_time = round(time.time(),10)
time_taken = (end_time - start_time)
print(f"The time {timedelta(seconds=time_taken)} taken to complete scraping")

file_json = pd.DataFrame(Product_list)
file_json.to_json("Amazon_scrape.json")

file_csv = pd.DataFrame(Product_list)
file_csv.to_csv("Amazon_scrape.csv",encoding='utf-8',index=False)

file_404 = pd.DataFrame(web_404)
file_404.to_csv("web_404.csv",encoding='utf-8',index=False)

driver.implicitly_wait(10)
driver.quit()