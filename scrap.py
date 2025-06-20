from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    print("sync_playwright() Begin!")
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()
    
    # Load the page (relax wait condition)
    page.goto("https://www.costco.co.kr/c/whatsnew", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)  # Adjust as needed
    
    for _ in range(5):
        page.mouse.wheel(0, 2000)
        page.wait_for_timeout(1000)
        
    html = page.content()
    with open("debug_page.html", "w", encoding="utf-8") as f:
        f.write(html)
        

    # Extract product items
    products = page.query_selector_all("div.product-tile-set")
    print(products)

    items = []
    for product in products:
        name_el = product.query_selector("div.name")
        price_el = product.query_selector("div.price")
        link_el = product.query_selector("a")

        items.append({
            "Item Name": name_el.inner_text() if name_el else "N/A",
            "Price": price_el.inner_text() if price_el else "N/A",
            "URL": "https://www.costco.co.kr" + link_el.get_attribute("href") if link_el else "N/A"
        })

    browser.close()

# Export results
df = pd.DataFrame(items)
df.to_csv("costco_whatsnew.csv", index=False, encoding="utf-8-sig")
