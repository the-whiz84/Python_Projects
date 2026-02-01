from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

GOOGLE_FORM = ""


class FillGoogleForm:
    def __init__(self) -> None:
        # # Keep Chrome opened after program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)


    def open_form(self):
        self.driver.get(GOOGLE_FORM)

    def fill_address(self, text):
        address_form = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_form.send_keys(text)

    def fill_price(self, text):
        price_form = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_form.send_keys(text)

    def fill_link(self, text):
        url_link = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        url_link.send_keys(text)

    def submit_entry(self):
        submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()
    
    def new_entry(self):
        new_answer = self.driver.find_element(By.LINK_TEXT, value="Trimite alt răspuns")
        new_answer.click()
