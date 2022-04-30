from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import io
import requests
from PIL import Image
import pytesseract
import easyocr

opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)

web = 'https://www.amazon.com/errors/validateCaptcha'

driver.get(web)

def captcha_solver():

    image_url = driver.find_element(By.TAG_NAME,"img")
    image_src = image_url.get_attribute("src")

    response = requests.get(image_src).content

    img = Image.open(io.BytesIO(response))

    # text = pytesseract.image_to_string(img)

    lang = easyocr.Reader(['en'])
    text_list = lang.readtext(img)
    text = text_list[0][1]

    # print(text)

    captcha_box = driver.find_element(By.ID,"captchacharacters")
    captcha_box.send_keys(text+Keys.ENTER)

captcha_solver()



# time.sleep(5)
# driver.close()
driver.quit()