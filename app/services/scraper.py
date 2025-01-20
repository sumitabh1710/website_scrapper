import requests
from bs4 import BeautifulSoup

def scrape_website(url: str):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        body = soup.find('body')
        print(body)
        if body:
            return body.get_text()
        return None
    except Exception as e:
        return None
