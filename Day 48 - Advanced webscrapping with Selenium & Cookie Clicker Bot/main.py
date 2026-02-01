from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome opened after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.de/-/en/dp/B0B7CQ2CHH/?coliid=I1HM1XKBV51B6&colid=20854P5NY1AMF&ref_=list_c_wl_lv_ov_lig_dp_it&th=1")
driver.get("https://www.python.org")



# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is €{price_euro.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)
# <selenium.webdriver.remote.webelement.WebElement (session="d3f3aa3f6e8c27b40bc0d2178b667295", element="f.03BCFD3FFE577837344800A60D01E016.d.DE4AE07FE663CE16E08063E328ADBE90.e.5")>
# print(search_bar.tag_name)
# input

# print(search_bar.get_attribute("placeholder"))
# Search

button = driver.find_element(By.ID, value="submit")
# print(button.size)
# {'height': 40, 'width': 46}

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
# docs.python.org

bug_report = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_report.text)
# Submit Website Bug

# driver.close()    # closes the active tab
driver.quit()     # closes the program