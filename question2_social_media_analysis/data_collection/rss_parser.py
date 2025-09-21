import requests
import xml.etree.ElementTree as ET
import csv
import os

RSS_URL = "https://www.reddit.com/r/python/.rss"  # Atom feed

def parse_rss(output_file="./src/data_collection/data/rss_feed.csv"):
    headers = {"User-Agent": "Mozilla/5.0"}  # Reddit blocks no-header requests
    response = requests.get(RSS_URL, headers=headers)
    if response.status_code != 200:
        print("⚠️ Failed to fetch RSS feed")
        return

    root = ET.fromstring(response.content)

    # Namespaces for Atom (Reddit uses this)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    data = []

    # Try Atom first (<entry>)
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text if entry.find("atom:title", ns) is not None else ""
        link = entry.find("atom:link", ns).attrib.get("href", "") if entry.find("atom:link", ns) is not None else ""
        updated = entry.find("atom:updated", ns).text if entry.find("atom:updated", ns) is not None else ""
        data.append([title, link, updated])

    # Fallback: try RSS (<item>)
    if not data:
        for item in root.findall(".//item"):
            title = item.find("title").text if item.find("title") is not None else ""
            link = item.find("link").text if item.find("link") is not None else ""
            pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""
            data.append([title, link, pub_date])

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Link", "Published"])
        writer.writerows(data)

    print(f"✅ Saved {len(data)} RSS/Atom entries to {output_file}")

def main():
    parse_rss()

if __name__ == "__main__":
    main()
