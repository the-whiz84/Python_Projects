from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element(By.ID, value="articlecount")
# article_count = (articles.text).split()[0]

# print(article_count)
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# search.send_keys(Keys.ENTER)


# driver.quit()