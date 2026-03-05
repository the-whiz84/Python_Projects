# Day 93 - SteamDB Trending Charts WebScrapping

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **SteamDB Trending Charts WebScrapping** and avoids generic cross-day boilerplate.

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

You build **SteamDB Trending Charts WebScrapping** as a day-specific project using `selenium`, `pandas`, `beautifulsoup`, `bs4`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `selenium`, `pandas`, `beautifulsoup`, `bs4`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `requirements.txt`: Project resource used by this day.
- `steam_most_played_games.csv`: Dataset/input data consumed by the day project.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Load tabular data, clean null/edge values, then compute the target metrics.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
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
```

## 6. How to Run

```bash
pip install -r requirements.txt
```
```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- External sites/APIs change often; verify selectors/fields before assuming parser bugs.
- Check nulls and dtypes before aggregations or charts to avoid misleading results.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **SteamDB Trending Charts WebScrapping** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
