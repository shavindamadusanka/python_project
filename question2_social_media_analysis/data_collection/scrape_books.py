import requests
from bs4 import BeautifulSoup
import time
import csv
import os

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=5, output_file="./src/data_collection/data/raw_books.csv"):
    all_books = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        print(f"Scraping {url}...")
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"⚠️ Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip("£")
            rating = book.p["class"][1]
            availability = book.find("p", class_="instock availability").text.strip()
            
            all_books.append([title, price, rating, availability])

        time.sleep(1)  # delay between requests

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Rating", "Availability"])
        writer.writerows(all_books)

    print(f"Saved {len(all_books)} books to {output_file}")


def main():
    scrape_books(pages=50)

if __name__ == "__main__":
    main()
