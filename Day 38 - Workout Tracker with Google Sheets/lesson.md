# Day 38 - Workout Tracker with Google Sheets

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Workout Tracker with Google Sheets** and avoids generic cross-day boilerplate.

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

You build **Workout Tracker with Google Sheets** as a day-specific project using `requests`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `requests`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.

## 4. Implementation Walkthrough

1. Collect and validate user input before performing transformations.
2. Call external web/API resources and normalize returned data before use.
3. Read/write JSON safely with existence checks and fallback defaults.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
GENDER = ""
WEIGHT_KG = 0
HEIGHT_CM = 0
AGE = 0

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")
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

- **Workout Tracker with Google Sheets** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
