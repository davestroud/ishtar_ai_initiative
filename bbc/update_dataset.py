import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_bbc(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')  # Ensure lxml is installed
    articles = []
    for item in soup.find_all('item'):
        title = item.find('title').text if item.find('title') else 'No title available'
        link = item.find('link').text if item.find('link') else 'No link available'
        pub_date = item.find('pubDate').text if item.find('pubDate') else 'No publication date available'
        description = item.find('description').text if item.find('description') else 'No description available'
        articles.append({
            'title': title,
            'link': link,
            'pub_date': pub_date,
            'description': description
        })
    return articles

def save_dataset(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")

def increment_version(version_file="VERSION"):
    with open(version_file, "r") as f:
        version = f.read().strip()
    major, minor = map(int, version.split("."))
    new_version = f"{major}.{minor + 1}"
    with open(version_file, "w") as f:
        f.write(new_version)
    return new_version

if __name__ == "__main__":
    url = "https://feeds.bbci.co.uk/news/rss.xml"
    scraped_data = scrape_bbc(url)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dataset_path = f"/Users/davidstroud/Desktop/ISHTAR_AI_INITIATIVE/BBC/bbc_dataset_{timestamp}.csv"
    save_dataset(scraped_data, dataset_path)
    version = increment_version(version_file="/Users/davidstroud/Desktop/ISHTAR_AI_INITIATIVE/BBC/VERSION")
    print(f"Dataset version updated to {version}")
