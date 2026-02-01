# 1. What is Selenium Webdriver

- one of the most well-known automation and testing tools for web developers
- it allows us to automate browsers by entering text or clicking buttons

- Selenium module uses the webdriver() class to interact with multiple browsers like Chrome, Safari or Firefox
- each browser uses a different Selenium bridge to interact with that browser


# 2. How to find and select Elements on the page with Selenium

https://selenium-python.readthedocs.io/locating-elements.html
 - we use the built-in method find_element

# from selenium import webdriver
# from selenium.webdriver.common.by import By

Keep Chrome opened after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.de/-/en/dp/B0B7CQ2CHH/?coliid=I1HM1XKBV51B6&colid=20854P5NY1AMF&ref_=list_c_wl_lv_ov_lig_dp_it&th=1")



# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is €{price_euro.text}.{price_cents.text}")

# We did in 3 lines what we struggles to get using BeautifulSoup on Day 47


# driver.close()    # closes the active tab
driver.quit()     # closes the program


# 2.1 Search by class, id, name etc.

# driver.get("https://www.python.org")


search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)
# <selenium.webdriver.remote.webelement.WebElement (session="d3f3aa3f6e8c27b40bc0d2178b667295", element="f.03BCFD3FFE577837344800A60D01E016.d.DE4AE07FE663CE16E08063E328ADBE90.e.5")>
# print(search_bar.tag_name)
# input

print(search_bar.get_attribute("placeholder"))
Search


# 2.2 Search by CSS Selectors

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
# docs.python.org


# 2.3 Search by XPath

bug_report = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_report.text)
# Submit Website Bug


# 3. Automating filling out forms and clicking

# 3.1 Clicking on links

# Hone in on anchor tags using CSS Selectors
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# If we want to click on the link, we use the built-in method
article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()


# 3.2 Finding Inputs and automating text entry

# Find the Search input by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python")

# Pressing Enter after entering search parameter
from selenium.webdriver.common.keys import Keys

<!-- search.send_keys(Keys.ENTER) -->
search.send_keys("Python", Keys.ENTER)