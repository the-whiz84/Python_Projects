# Day 46 - Webscrapping with authentication

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Webscrapping with authentication** and avoids generic cross-day boilerplate.

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

You build **Webscrapping with authentication** as a day-specific project using `requests`, `beautifulsoup`, `bs4`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `requests`, `beautifulsoup`, `bs4`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.

## 4. Implementation Walkthrough

1. Collect and validate user input before performing transformations.
2. Call external web/API resources and normalize returned data before use.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "https://www.example.com/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Retrieve the Top 100 song names for the given period
print(f"Getting Billboard Top 100 songs for the week of {date}........")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
top100_html = response.text

soup = BeautifulSoup(top100_html, "html.parser")
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

- **Webscrapping with authentication** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
