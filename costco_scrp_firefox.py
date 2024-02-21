# this repository is based on the website of https://www.blog.datahut.co/post/scrape-product-information-from-costco-using-python

import pandas as pd
import lxml
import bs4
from selenium import webdriver
pd.options.mode.chained_assignment = None
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()



def extract_content(url):
    driver.get(url)
    page_content = driver.page_source
    soup = bs4.BeautifulSoup(page_content, 'html.parser')
    return soup

