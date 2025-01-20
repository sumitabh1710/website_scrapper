import requests
from bs4 import BeautifulSoup
from .models import WebsiteDetails

def scrape_website(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Could not access the website or invalid URL")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    raw_text = soup.get_text()

    return raw_text
