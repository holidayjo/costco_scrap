# this repository is based on the website of https://www.blog.datahut.co/post/scrape-product-information-from-costco-using-python

# Importing necessary libraries
import platform
import json
import pandas as pd
from lxml import etree as et
from bs4 import BeautifulSoup
pd.options.mode.chained_assignment = None
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver.get('http://www.google.com')
def url_reader(): # (menu_name='whats_new'):
    if platform.system() == "Windows":
        with open(r'D:\Github\Python\webscr\costco_scrap-2\urls.json') as f:
            data = json.load(f)
    else:
        with open('/media/holidayj/My Documents/Github/Python/webscr/costco_scrap-2/urls.json') as f:
            data = json.load(f)
    f.close()
    return data #[menu_name]

def extract_content(url):
    # Function to extract content from page.
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup

def click_url(driver, click_path):
    # Function to click
    driver.find_element(By.XPATH, click_path).click()
    driver.find_element(By.XPATH, click_path).click()

def get_content(driver):
    # to extract content from the page.
    html_content = driver.page_source
    soup         = BeautifulSoup(html_content, 'html.parser')
    return soup
    
def category_link(soup):
    # Function to get the urls of sub categories under Audio/Video
    category_link = []
    for div in soup.find_all('div', attrs = {"class": "col=-xs-12 col-lg-6 con-cl-3"}):
        print(div)
        break
        
        
    
        
# Reading urls and html links.
urls            = url_reader()        # root is costco home page.
click_category  = urls["BuyersPick"]["page1"]  # buyerspick - page1 category.
root_url        = urls["root"]

chrome_options = webdriver.ChromeOptions()
driver         = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(root_url)
click_url(driver, click_category) # in the bs4 shape.
url_content = get_content(driver)
# going through all pages.
for i in range(2,5):
    print(i)
    click_url(driver, urls["BuyersPick"]["page{}".format(i)])
    url_content = get_content(driver)
    product_name = url_content.find_all('a', class_='lister-name')
    print("product_name in page {} =".format(i), product_name)
    
# so far, the code clicks each pages in the buyers pick category.
# but clicking pages are hard coded. 
# it doesn't know how many pages are in the category.
# then we need to extract detailed information of each item.