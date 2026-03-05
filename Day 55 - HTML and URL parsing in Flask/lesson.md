# Day 55 - HTML and URL parsing in Flask

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **HTML and URL parsing in Flask** and avoids generic cross-day boilerplate.

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

You build **HTML and URL parsing in Flask** as a day-specific project using `flask`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `flask`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 1. Flask URL Paths and the Flask Debugger
- You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument.
- @app.route("/username/<name>")

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `higher_lower.py`: Supporting module for project logic.

## 4. Implementation Walkthrough

1. Define route handlers and keep request parsing separate from rendering logic.
2. Add targeted checks for edge cases and invalid paths before final output.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1><p>This is a paragraph</p><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3RuNGo1eTQ1dGZqa2xoM2Iyd2puODl3Y3B2NHZhaGQzNG44bG1mMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12ELmx0C4EFKcE/giphy.gif' />"


def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

def make_italic(function):
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- Route and template variable mismatches are common; verify context keys end-to-end.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **HTML and URL parsing in Flask** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
