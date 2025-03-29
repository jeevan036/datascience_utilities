import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrapes the given URL and extracts the page title and first paragraph."""
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No Title Found"
        paragraph = soup.p.find(text=True) if soup.p else "No Paragraph Found"
        return {"title": title, "paragraph": paragraph}
    else:
        return {"error": f"Failed to fetch page, status code: {response.status_code}"}

# Example usage
if __name__ == "__main__":
    url = "https://www.wikipedia.org/"
    result = scrape_website(url)
    print(result)
