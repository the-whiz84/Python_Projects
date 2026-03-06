# Day 93 - Trend Data Scraping, Cleaning, and Reporting

This project scrapes the SteamDB charts, extracts the most-played games table, converts the values into structured records, and saves the result as a CSV. It is a good example of a scraping workflow that mixes Selenium and BeautifulSoup rather than relying on only one tool.

That combination matters because some pages are easier to parse after the browser has already rendered them.

## 1. Use Selenium to Reach the Dynamic Page State

The script starts by launching a browser:

```python
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
```

Then it loads the SteamDB charts page and scrolls:

```python
url = "https://steamdb.info/charts/?sort=24h"
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

That scroll is a useful scraping habit. On sites with lazy loading or client-side rendering, the browser often has to interact with the page before the full target content appears.

The script also waits for the table explicitly:

```python
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "table-apps"))
)
```

Without that wait, the parser might run against a partial DOM and fail intermittently.

## 2. Hand the Rendered Page to BeautifulSoup

Once the table is present, the script switches from browser automation to HTML parsing:

```python
soup = BeautifulSoup(driver.page_source, "html.parser")
table = soup.find("table", id="table-apps")
```

This is a strong hybrid approach:

- Selenium gets the page into the right state
- BeautifulSoup handles structured extraction

That division of labor often produces cleaner scraping code than trying to do everything with browser selectors alone.

## 3. Normalize the Table Into Structured Records

The extraction loop pulls a few key fields from each row:

```python
games = []
for row in table.select("tbody tr"):
    game_name = row.select_one("td:nth-child(3) a").text.strip()
    current_players = (
        row.select_one("td:nth-child(4)").text.strip().replace(",", "")
    )
    peak_24h = row.select_one("td:nth-child(5)").text.strip().replace(",", "")
    all_time_peak = row.select_one("td:nth-child(6)").text.strip().replace(",", "")
```

The important cleanup step is the numeric normalization. Player counts arrive as formatted text with commas, so the script strips those separators and converts the values to integers before storing them.

That is what turns the scrape into usable data rather than just copied text.

## 4. Export the Result as a Reusable Dataset

After the records are collected, the script builds a DataFrame and writes it to disk:

```python
df = pd.DataFrame(games)
df.to_csv("steam_most_played_games.csv", index=False)
```

That final CSV is what makes the project reusable. The scrape does not end in a print statement. It ends in a report artifact that another analysis step could pick up later.

The script also wraps the whole flow in exception handling and always closes the browser in `finally`, which is the right habit for automation that launches external processes.

## How to Run the SteamDB Scraper

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the scraper:
   ```bash
   python main.py
   ```
3. Verify the workflow:
   - the table loads successfully
   - the script reports how many games it found
   - `steam_most_played_games.csv` is created with numeric player columns

## Summary

Today, you built a scrape-to-report pipeline. Selenium handled the dynamic page state, BeautifulSoup parsed the rendered HTML, pandas stored the result, and CSV export turned the scrape into a reusable dataset. The big lesson is choosing the right tool for each phase of the extraction workflow rather than forcing one library to do everything.
