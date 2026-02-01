import requests, smtplib, os
from bs4 import BeautifulSoup
import lxml

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.de/-/en/dp/B0B7CQ2CHH/?coliid=I1HM1XKBV51B6&colid=20854P5NY1AMF&ref_=list_c_wl_lv_ov_lig_dp_it&th=1"

DESIRED_PRICE = 200

my_email = os.environ.get("MY_EMAIL")
email_password = os.environ.get("MY_EMAIL_PASSWD")


# Set up your headers by using https://myhttpheader.com
headers = { 
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'sec-fetch-mode': "navigate",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
    'Accept-Language': "en-US,en;q=0.9",
    'sec-fetch-dest': "document",
    'x-forwarded-proto': "https",
    'x-https': "on",
}

# Scrape the URL for product name and price value
response = requests.get(URL, headers=headers)
response.raise_for_status()

html_data = response.content

soup = BeautifulSoup(html_data, "lxml")

price_data = soup.find(name="span", class_="aok-offscreen")
price_unformatted = (price_data.text).split("€")[1]
price = float(price_unformatted.split()[0])

product_name_data = soup.find(id="productTitle")
product_name = ((product_name_data.text).split(" (")[0]).strip()


#Send an email when price is below a given value
if price < DESIRED_PRICE:
    print("Sending price alert email....")
    message = f"Subject: Amazon Price Tracker Alert\n\nHello,\n\n {product_name} is now ${price}!\n\n{URL}"
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    with connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=message
        )
