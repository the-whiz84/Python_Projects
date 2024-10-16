from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Set up Selenium WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

try:
    url = "https://steamdb.info/charts/?sort=24h"
    driver.get(url)

    # Scroll to the bottom of the page to trigger any lazy-loaded content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Step 2: Wait for the table with id 'table-apps' to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "table-apps"))
        )
        print("Table found, proceeding to extract data...")

    except TimeoutException:
        print("Error: Timed out waiting for the table to load.")
        driver.quit()
        exit()

    # Step 3: Parse the page with BeautifulSoup after the table is loaded
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Step 4: Select the table using its id
    table = soup.find("table", id="table-apps")

    # Step 5: Extract relevant data from the table
    games = []
    for row in table.select("tbody tr"):
        game_name = row.select_one("td:nth-child(3) a").text.strip()
        current_players = (
            row.select_one("td:nth-child(4)").text.strip().replace(",", "")
        )
        peak_24h = row.select_one("td:nth-child(5)").text.strip().replace(",", "")
        all_time_peak = row.select_one("td:nth-child(6)").text.strip().replace(",", "")

        games.append(
            {
                "Game": game_name,
                "Current Players": int(current_players),
                "Peak Players (24h)": int(peak_24h),
                "All Time Peak": int(all_time_peak),
            }
        )

    # Log the number of games found
    print(f"Found {len(games)} games.")

    # Step 6: Save the data to a CSV file
    df = pd.DataFrame(games)
    df.to_csv("steam_most_played_games.csv", index=False)
    print("Data has been saved to steam_most_played_games.csv")

except NoSuchElementException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
