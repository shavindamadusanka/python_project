from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os

# URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

def scrape_with_selenium(output_file="./src/data_collection/data/raw_tablets.csv"):
    driver = webdriver.Chrome()  # requires ChromeDriver installed
    driver.get(URL)
    time.sleep(3)  # wait for JS to load

    products = driver.find_elements(By.CLASS_NAME, "thumbnail")
    
    data = []
    for p in products:
        title = p.find_element(By.CLASS_NAME, "title").text
        price = p.find_element(By.CLASS_NAME, "price").text.strip("$")
        description = p.find_element(By.CLASS_NAME, "description").text
        reviews = p.find_element(By.CLASS_NAME, "ratings").text

        data.append([title, price, description, reviews])

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Description", "Reviews"])
        writer.writerows(data)

    driver.quit()
    print(f"✅ Saved {len(data)} products to {output_file}")

def main():
    scrape_with_selenium()

if __name__ == "__main__":
    main()
