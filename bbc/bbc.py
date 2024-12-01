import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_rss_feed(url):
    """
    Fetches the RSS feed content from the given URL.
    
    Parameters:
        url (str): The URL of the RSS feed.
    
    Returns:
        BeautifulSoup: Parsed XML content of the RSS feed.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BeautifulSoup(response.content, 'xml')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the RSS feed: {e}")
        return None


def parse_articles(soup):
    """
    Parses articles from the RSS feed's BeautifulSoup object.
    
    Parameters:
        soup (BeautifulSoup): Parsed XML content of the RSS feed.
    
    Returns:
        list: A list of dictionaries containing article details.
    """
    articles = []
    if soup:
        for item in soup.find_all('item'):
            articles.append({
                'title': item.find('title').text.strip() if item.find('title') else 'No title available',
                'link': item.find('link').text.strip() if item.find('link') else 'No link available',
                'pub_date': item.find('pubDate').text.strip() if item.find('pubDate') else 'No publication date available',
                'description': item.find('description').text.strip() if item.find('description') else 'No description available'
            })
    return articles


def save_to_csv(articles, filename):
    """
    Saves the list of articles to a CSV file.
    
    Parameters:
        articles (list): List of article dictionaries.
        filename (str): Name of the output CSV file.
    """
    try:
        df = pd.DataFrame(articles)
        df.to_csv(filename, index=False)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


def main():
    """
    Main function to fetch, parse, preprocess, and save articles.
    """
    # Define the RSS feed URL and output CSV file name
    rss_url = "https://feeds.bbci.co.uk/news/rss.xml"
    output_file = "bbc_dataset.csv"

    # Fetch and parse the RSS feed
    print("Fetching the RSS feed...")
    soup = fetch_rss_feed(rss_url)

    # Parse articles from the RSS feed
    print("Parsing articles...")
    articles = parse_articles(soup)

    # Save articles to a CSV file
    print("Saving articles to CSV...")
    save_to_csv(articles, output_file)


if __name__ == "__main__":
    main()
