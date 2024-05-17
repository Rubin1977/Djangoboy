import requests
import lxml
from bs4 import BeautifulSoup

def get_reality_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "sk",
    }
   
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    #print(soup.prettify())

    name = soup.select_one(selector="h1").getText()
    
    price = soup.find('p', class_='MuiTypography-root MuiTypography-h3 css-wupcfx').getText()
    price = int(price.replace('\xa0', '').replace(' €', ''))
   
    return name, price