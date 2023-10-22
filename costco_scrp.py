# this repository is based on the website of https://www.blog.datahut.co/post/scrape-product-information-from-costco-using-python

# Importing necessary libraries

import pandas as pd
from lxml import etree as et
from bs4 import BeautifulSoup
import selenium
import webdriver_manager

pd.options.mode.chained_assignment = None
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
driver         = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('http://www.google.com')

def extract_content(url):
    # Function to extract content from page.
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup

def click_url(driver):
    # Function to click e electronic category 'Audio/Video' and extract content from the page.
    driver.find_element(By.XPATH, '//*[@id="navpills-sizing/a[3]').click()
    html_content = driver.page_source
    soup         = BeautifulSoup(html_content, 'html.parser')
    return soup

def category_link(soup):
    # Function to get the urls of sub categories under Audio/Video
    category_link = []
    for div in soup.find_all('div', attrs = {"class": "col=-xs-12 col-lg-6 con-cl-3"}):
        break
        
