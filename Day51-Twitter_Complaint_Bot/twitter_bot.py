import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# # Keep Chrome opened after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
        self.username = os.environ.get("TWITTER_USERNAME")
        self.password = os.environ.get("TWITTER_PASSWD")


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(3)
        self.driver.find_element(By.ID, value="onetrust-reject-all-handler").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(40)
       
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        print(f"Down Speed: {self.down} Mbps")
        print(f"Up Speed: {self.up} Mbps")


    def tweet_at_provider(self, tweet):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)
        
        # Login to X
        username = self.driver.find_element(By.NAME, value='text')
        username.send_keys(self.username, Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(self.password, Keys.ENTER)
        
        # Extra time added to enter MFA code manually
        time.sleep(30)
        
        # Disable cookie popup
        refuse_cookies = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div/span/span')
        refuse_cookies.click()
        
        # Find message input and type text
        message_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div')
        message_input.send_keys(tweet)
        
        # Wait a few seconds and then press the Post button
        time.sleep(3)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span').click()
        
        time.sleep(2)
        self.driver.quit()
