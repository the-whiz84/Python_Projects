# Day 64 - My Top 10 Movies Website

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **My Top 10 Movies Website** and avoids generic cross-day boilerplate.

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

You build **My Top 10 Movies Website** as a day-specific project using `flask`, `requests`, `sqlalchemy`, `wtforms`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `flask`, `requests`, `sqlalchemy`, `wtforms`.
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
TMDB_TOKEN = os.environ.get("TMDB_TOKEN")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie/"
img_base_url =  "https://image.tmdb.org/t/p/w500"

tmdb_headers = {
"accept": "application/json",
"Authorization": f"Bearer {TMDB_TOKEN}"
}


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)
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

- **My Top 10 Movies Website** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
