# Day 57 - Blog Project & Templating with Jinja in Flask Apps

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Blog Project & Templating with Jinja in Flask Apps** and avoids generic cross-day boilerplate.

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

You build **Blog Project & Templating with Jinja in Flask Apps** as a day-specific project using `flask`, `requests`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `flask`, `requests`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 1. URL building and templating with Jinja
- Jinja is a templating language built for Python. It is bundled with the Flask framework.
- It uses specific syntax that can specify inside the HTML file which part is evaluated as Python code.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `post.py`: Supporting module for project logic.
- `server.py`: Entrypoint script coordinating the full flow.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Define route handlers and keep request parsing separate from rendering logic.
3. Read/write JSON safely with existence checks and fallback defaults.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:index>')
```

## 6. How to Run

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

- **Blog Project & Templating with Jinja in Flask Apps** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
