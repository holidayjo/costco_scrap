import requests
from bs4 import BeautifulSoup

url = "https://www.costco.co.kr/c/whatsnew?itm_source=homepage&itm_medium=blueNav&itm_campaign=whatsnew&itm_term=whatsnew&itm_content=InternalCATwhatsnew"
# url = "https://www.costco.co.kr/c/whatsnew?itm_source=homepage&itm_medium=blueNav&itm_campaign=whatsnew&itm_term=whatsnew&itm_content=InternalCATwhatsnew&page=1"
# url = "https://www.costco.co.kr/BabyKidsToysPets/Toys/c/cos_3.5?sort=price-asc"
# url = "https://www.costco.co.kr/c/whatsnew?itm_source=homepage&itm_medium=blueNav&itm_campaign=whatsnew&itm_term=whatsnew&itm_content=InternalCATwhatsnew&page=1"
# url = "https://www.costco.co.kr/c/whatsnew?itm_source=homepage&itm_medium=blueNav&itm_campaign=whatsnew&itm_term=whatsnew&itm_content=InternalCATwhatsnew&sort=price-asc"
# url = "https://www.costco.co.kr/HomeKitchen/Kitchen-Accessories/c/cos_15.2?page=1"
# page = ""
# full_url = f"{url}{page}"

response     = requests.get(url)
response_txt = response.text
# print(response_txt)
soup = BeautifulSoup(response.content, 'html.parser')  # Make sure to use the appropriate parser
print("soup =", soup)


# Find all the elements containing the product names
product_names = soup.find_all('a', class_='lister-name')
# print(product_names)

# Extract and print all the product names
for element in product_names:
    # print(name)
    product_name = element.find('span', class_='notranslate').get_text(strip=True)
    # print(product_name)
