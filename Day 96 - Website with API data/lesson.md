# Day 96 - Website with API data

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Website with API data** and avoids generic cross-day boilerplate.

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

You build **Website with API data** as a day-specific project using `flask`, `requests`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `flask`, `requests`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `requirements.txt`: Project resource used by this day.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Define route handlers and keep request parsing separate from rendering logic.
3. Read/write JSON safely with existence checks and fallback defaults.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
app = Flask(__name__)

API_URL = "https://the-one-api.dev/v2/"

book_response = requests.get(f"{API_URL}book").json()
all_books = book_response["docs"]
book_id = [doc["_id"] for doc in all_books]


@app.route("/")
def home():
    return render_template("index.html", all_books=all_books)
```

## 6. How to Run

```bash
pip install -r requirements.txt
```
```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- Route and template variable mismatches are common; verify context keys end-to-end.
- External sites/APIs change often; verify selectors/fields before assuming parser bugs.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Website with API data** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
