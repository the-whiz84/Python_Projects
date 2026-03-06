# Day 53 - Data Entry Job Automation: Extract, Transform, and Load

Day 53 brings together two different approaches we have been practicing across the web automation section. The project uses `requests` and BeautifulSoup to collect rental listings from a Zillow-style page, then uses Selenium to open a Google Form and submit each listing one by one.

This is a good lesson for a bit of general theory because the project maps neatly onto a real software pattern: ETL, which stands for extract, transform, and load. The script extracts raw data from one source, transforms it into clean Python lists, and loads it into another system through a browser form.

## 1. Why This Project Uses Two Different Tools

The architecture of this project is one of its most important lessons. It does not use Selenium for everything and it does not use BeautifulSoup for everything. Instead, it splits the problem by responsibility:

- `requests` + BeautifulSoup for collecting page data quickly
- Selenium for interacting with the Google Form where real clicks and typing are required

That split matters. Selenium is powerful, but it is expensive because it launches a real browser and drives the full interface. BeautifulSoup is much lighter when the only goal is to read page content.

So the project is also teaching a broader design habit: choose tools based on the type of work being done, not just on what you used in the previous lesson.

## 2. The Extract Phase Uses HTTP Requests and Parsing

The `ZillowData` class starts by requesting the page and building a BeautifulSoup object:

```python
response = requests.get(URL, headers=chrome_headers)
zillow_data = response.text
self.soup = BeautifulSoup(zillow_data, "html.parser")
```

This is the extract step. The script is not opening a visual browser here. It is simply downloading the HTML and parsing it into a searchable tree.

The custom headers are worth keeping in the lesson too. Even though this example targets a clone site, the code is practicing a realistic scraping habit: sending browser-like headers so the request looks closer to a normal visit.

## 3. Transformation Means Cleaning the Raw Page Data

After parsing the page, the class builds three separate lists:

```python
self.property_addrs = []
self.property_prices = []
self.property_links = []
self.get_listing_address()
self.get_listing_price()
self.get_listing_links()
```

Each helper method transforms raw HTML into a cleaner Python structure. For example, the address method selects address elements and normalizes the text:

```python
address_list = self.soup.select(selector="a address")
self.property_addrs = [(item.getText().strip()).replace(" |", ",") for item in address_list]
```

This is a useful generic Python point. Raw scraped data is usually messy. It often contains extra spaces, symbols, formatting markers, or mixed content. Transformation is the stage where the script shapes that messy data into something consistent enough to use later.

## 4. Price Cleaning Shows Why String Processing Still Matters

The pricing method is a good example of simple text cleanup doing real work:

```python
prices_list = self.soup.find_all(class_='PropertyCardWrapper__StyledPriceLine')
self.property_prices = [(item.getText().split("+", 1)[0]).split("/")[0] for item in prices_list]
```

This line removes extra suffixes such as `+` markers and `/mo` style fragments so the final stored price is shorter and more uniform.

That is worth expanding a little because students sometimes expect automation projects to be mostly about libraries. In practice, a lot of automation still depends on ordinary Python string operations. Libraries help you find the data, but basic Python often does the final cleanup.

## 5. Link Extraction Completes the Dataset

The final extractor gathers the property URLs:

```python
links_list = self.soup.select(selector=".StyledPropertyCardDataWrapper a")
self.property_links = [item.get("href") for item in links_list]
```

At this point, the class has turned one HTML document into three aligned Python lists:

- addresses
- prices
- links

That alignment matters because each index now represents one listing. The first address, first price, and first link belong together. That is what makes the later form-submission loop possible.

## 6. The Load Phase Uses Selenium Because the Target Is Interactive

The `FillGoogleForm` class handles the second half of the pipeline:

```python
class FillGoogleForm:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_form(self):
        self.driver.get(GOOGLE_FORM)
```

This part of the project explains why Selenium is still necessary. A Google Form is not just data to read. It is an interactive interface with input fields, a submit button, and a "submit another response" link. That is the kind of target where a real browser driver makes sense.

So the architecture is not arbitrary. The scraper uses the lightweight tool for the read phase, and the browser automation tool for the write phase.

## 7. Small Helper Methods Keep the Form Filler Focused

The form class splits each action into small methods:

```python
def fill_address(self, text):
    address_form = self.driver.find_element(By.XPATH, value='...')
    address_form.send_keys(text)

def fill_price(self, text):
    price_form = self.driver.find_element(By.XPATH, value='...')
    price_form.send_keys(text)

def fill_link(self, text):
    url_link = self.driver.find_element(By.XPATH, value='...')
    url_link.send_keys(text)
```

That is a helpful design choice because it gives the class a single responsibility: it knows how to work with the form. It does not know how Zillow is scraped. It does not know how the data was cleaned. It only knows where each field lives and how to fill it.

This makes the code easier to maintain. If the form layout changes, the fix belongs in one place.

## 8. `main.py` Acts as the Orchestrator

The main script connects the two classes:

```python
z_data = ZillowData()
g_form = FillGoogleForm()

g_form.open_form()
time.sleep(5)

for item in range(0, len(z_data.property_prices)):
    time.sleep(2)
    g_form.fill_address(z_data.property_addrs[item])
    time.sleep(1)
    g_form.fill_price(z_data.property_prices[item])
    time.sleep(1)
    g_form.fill_link(z_data.property_links[item])
    time.sleep(1)
    g_form.submit_entry()
    time.sleep(1)
    g_form.new_entry()
```

This is where the ETL pattern becomes obvious:

- `ZillowData()` performs extract and transform
- `FillGoogleForm()` performs load
- the loop feeds each cleaned record into the form

Using a loop over index positions keeps the three lists aligned. That is a practical solution because the data was intentionally stored in parallel arrays during extraction.

## 9. The Project Shows Why Separation of Concerns Matters

One of the best parts of this project is that the scraping logic and the form-submission logic are separate. That separation makes the code easier to read, test mentally, and repair.

If the source website changes, you update the `ZillowData` class.
If the form fields change, you update `FillGoogleForm`.
If the high-level workflow changes, you update `main.py`.

That is a clean architectural lesson and one worth preserving in the write-up.

## How to Run the Project

1. Create a Google Form with fields for address, price, and link.
2. Paste the form URL into `GOOGLE_FORM` inside [google_form.py](/Users/wizard/Developer/Python_Projects/Day%2053%20-%20Data%20Entry%20Job%20Automation/google_form.py).
3. Install the required packages if needed:

```bash
pip install requests beautifulsoup4 selenium
```

4. Run the project:

```bash
python main.py
```

You may need to update the Google Form XPaths if your form structure differs from the original project.

## Summary

Day 53 is a strong example of Python as glue between systems. The project extracts listing data with `requests` and BeautifulSoup, transforms it into clean lists, and loads it into Google Forms with Selenium. The bigger lesson is architectural: use the lightweight tool for fast data extraction, use the browser automation tool only where interaction is necessary, and keep those responsibilities separate.
