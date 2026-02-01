from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/Zillow-Clone/"

chrome_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Sec-Ch-Ua": '\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"', 
    "Sec-Ch-Ua-Platform": '\"macOS\"', 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36", 
  }

class ZillowData:
    def __init__(self) -> None:
        response = requests.get(URL, headers=chrome_headers)
        zillow_data = response.text
        self.soup = BeautifulSoup(zillow_data, "html.parser")
        self.property_addrs = []
        self.property_prices = []
        self.property_links = []
        self.get_listing_address()
        self.get_listing_price()
        self.get_listing_links()

    def get_listing_address(self):
        address_list = self.soup.select(selector="a address")
        self.property_addrs = [(item.getText().strip()).replace(" |",",") for item in address_list]

    def get_listing_price(self):
        prices_list = self.soup.find_all(class_='PropertyCardWrapper__StyledPriceLine')
        self.property_prices = [(item.getText().split("+", 1)[0]).split("/")[0] for item in prices_list]

    def get_listing_links(self):
        links_list = self.soup.select(selector=".StyledPropertyCardDataWrapper a")
        self.property_links = [item.get("href") for item in links_list]
