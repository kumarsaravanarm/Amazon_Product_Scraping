# Amazon_Product_Scraping

**Language** : Python

**Modules** : Selenium, Pandas, Webdriver-Manager, time

Web Scraping using Selenium is easy & understandable and compatible to JavaScript based webpage.

Webdriver-Mangaer module is used for borwser settings.

Pandas module is used for to manipulate the csv file for big data projects easily.

## Scraping the data by WebElements

The driver object is created to open up the web browser with the help of webdriver-manager module. But using the Google Colab we can only open browser as backgroun running program.

To scrape the data from the web page using the tag attribute from the web html code into the find_element object which get that data from web page.

If the element is not found, Selenium through NoSuchElementExists error we can catch that error by using try & except to resolve that error.

Looping the data from the csv file to scrape the product details for all the webpages

Using the pandas module converting the output into .CSV & .JSON file

10min. time taken to Scrape all the data from the web page.

# Bonus Task: Amazon Captcha Solver

**Language** : Python

**Modules** : Selenium, Pandas, Webdriver-Manager, PIL, EasyOCR

The driver object is created to open up the web browser with the help of webdriver-manager module. But using the Google Colab we can only open browser as backgroun running program.

The Amazon Captcha Image is extracted by using Pillow, requests, io modules. With that image using EasyOCR we can extract the text from the image with great accuracy ( we can also use pytesseract to extract text from image but it medium accuray than EasyOCR )

Then passing the text into the amazon captcha box followed by Keys.ENTER which solves the captcha.
