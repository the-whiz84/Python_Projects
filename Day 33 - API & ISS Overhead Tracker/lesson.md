# Day 33 - API & ISS Overhead Tracker

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **API & ISS Overhead Tracker** and avoids generic cross-day boilerplate.

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

You build **API & ISS Overhead Tracker** as a day-specific project using `tkinter`, `requests`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `tkinter`, `requests`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `kanye_quote.py`: Supporting module for project logic.
- `main_api.py`: Supporting module for project logic.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Read/write JSON safely with existence checks and fallback defaults.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
MY_LAT = 45.649490
MY_LONG = 25.606550



def check_position():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	iss_latitude = float(data["iss_position"]["latitude"])
	iss_longitude = float(data["iss_position"]["longitude"])
	if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
		return True
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- External sites/APIs change often; verify selectors/fields before assuming parser bugs.
- Keep state updates in one place; desynchronized UI/game state causes subtle bugs.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **API & ISS Overhead Tracker** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
