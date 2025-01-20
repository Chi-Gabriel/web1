def convert_query_to_google_url(query: str) -> str:
    import urllib.parse

    base_url = "https://www.google.com/search"
    query_params = {"q": query}
    encoded_params = urllib.parse.urlencode(query_params)

    return f"{base_url}?{encoded_params}"

import requests
from bs4 import BeautifulSoup
import re

def extract_text_and_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract text
        text = soup.get_text(strip=True)

        # Extract URLs
        urls = []
        for link in soup.find_all('a', href=True):
            urls.append(link['href'])

        return text, urls

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


if __name__ == "__main__":
    search_query = "Python function to convert query to URL"
    google_url = convert_query_to_google_url(search_query)

    target_url = google_url # Get URL from the user
    text, urls = extract_text_and_urls(target_url)

    if text and urls:
        print("Extracted Text:\n", text)
        print("\nExtracted URLs:\n", urls)



# Example usage:
