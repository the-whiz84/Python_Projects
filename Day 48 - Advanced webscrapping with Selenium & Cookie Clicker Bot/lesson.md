# Day 48 - Advanced webscrapping with Selenium & Cookie Clicker Bot

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Advanced webscrapping with Selenium & Cookie Clicker Bot** and avoids generic cross-day boilerplate.

## Table of Contents

- [1. What You Build](#1-what-you-build)
- [2. Core Concepts](#2-core-concepts)
- [3. Project Structure](#3-project-structure)
- [4. Implementation Walkthrough](#4-implementation-walkthrough)
- [5. Day Code Snippet](#5-day-code-snippet)
- [6. How to Run](#6-how-to-run)
- [7. Common Pitfalls and Debug Tips](#7-common-pitfalls-and-debug-tips)
- [8. Practice Extensions](#8-practice-extensions)
- [9. Key Takeaways](#9-key-takeaways)

## 1. What You Build

You build **Advanced webscrapping with Selenium & Cookie Clicker Bot** as a day-specific project using `selenium`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `selenium`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 1. What is Selenium Webdriver
- - one of the most well-known automation and testing tools for web developers
- - it allows us to automate browsers by entering text or clicking buttons

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `challenge.py`: Supporting module for project logic.
- `interaction.py`: Supporting module for project logic.
- `main_cookie_clicker_bot.py`: Supporting module for project logic.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Add targeted checks for edge cases and invalid paths before final output.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.de/-/en/dp/B0B7CQ2CHH/?coliid=I1HM1XKBV51B6&colid=20854P5NY1AMF&ref_=list_c_wl_lv_ov_lig_dp_it&th=1")
driver.get("https://www.python.org")



# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is €{price_euro.text}.{price_cents.text}")
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- External sites/APIs change often; verify selectors/fields before assuming parser bugs.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Advanced webscrapping with Selenium & Cookie Clicker Bot** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
