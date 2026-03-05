# Day 69 - Capstone Blog Project - Adding Users

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Capstone Blog Project - Adding Users** and avoids generic cross-day boilerplate.

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

You build **Capstone Blog Project - Adding Users** as a day-specific project using `flask`, `sqlalchemy`, `wtforms`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `flask`, `sqlalchemy`, `wtforms`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 1. Creating Relational Databases
- Given that the 1st user is the admin and the blog owner. It would make sense if we could link the blog posts they write to their user in the database.
- In the future, maybe we will want to invite other users to write posts in the blog and grant them the admin privileges.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `forms.py`: Supporting module for project logic.
- `requirements.txt`: Project resource used by this day.

## 4. Implementation Walkthrough

1. Define route handlers and keep request parsing separate from rendering logic.
2. Add targeted checks for edge cases and invalid paths before final output.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)


# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)
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
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Capstone Blog Project - Adding Users** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
