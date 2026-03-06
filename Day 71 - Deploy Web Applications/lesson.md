# Day 71 - Deployment: Moving a Flask App from Localhost to Production

Up to this point, the course has focused on building Flask applications locally. That is the right place to learn, because localhost is fast, safe, and easy to debug. But a web app only becomes a real web app when other people can reach it through a public URL.

That is what deployment changes. You are no longer writing code only for your own machine. You are preparing the project to run on a server with its own file system, environment variables, process manager, and networking rules.

## 1. What Deployment Actually Means

Deployment is more than uploading Python files to the internet.

A deployed Flask app needs:

- a machine or platform that can run Python
- a way to install dependencies
- a process that starts the application
- environment variables for secrets and configuration
- a public web address that forwards requests to the app

That is why deployment sits at the boundary between programming and operations. The code may already work, but the environment has to be set up correctly before anybody else can use it.

## 2. Why `app.run(debug=True)` Is Only for Development

In many earlier Flask projects, the app starts like this:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

That is fine for local development, but it is not how you want to serve production traffic.

`debug=True` is useful locally because it:

- reloads the app when files change
- shows detailed error pages
- makes debugging faster

In production, those same features become liabilities. Public users should not see debug tracebacks, and the built-in development server is not meant to be your long-running production web server.

This is why deployment platforms usually run Flask through a production WSGI server such as Gunicorn:

```bash
gunicorn main:app
```

That command means:

- import the `main` module
- find the Flask application object named `app`
- serve it using a production-ready process

## 3. Configuration Belongs in Environment Variables

By Day 71, the course has already introduced configuration values such as Flask secret keys, login settings, and API tokens. Those should not be hardcoded into the source code.

A Flask app should read sensitive settings from the environment instead:

```python
import os

app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")
```

This pattern matters even more in production, because hosting providers give you a dashboard for setting variables without storing them in the repository.

That gives you a clean separation:

- Git stores the code
- the hosting platform stores the secrets

It also lets the same project behave differently in development and production without editing the source every time you switch environments.

## 4. Dependency Management Is Part of Deployment

A deployed server does not know which packages your app needs unless you tell it.

That is why Python projects use `requirements.txt`. When your hosting provider builds the app, it installs everything listed there.

A typical workflow is:

```bash
pip freeze > requirements.txt
```

If the Flask blog app depends on packages like Flask, Flask-Login, Flask-Bootstrap, Flask-CKEditor, and SQLAlchemy, they all need to be present in that file or the deployment will fail at import time.

This is one of the biggest differences between "it works on my machine" and "it is deployable." Local success is not enough; the project has to describe its own runtime requirements.

## 5. Static Files, Templates, and URL Generation

The Flask projects in this part of the course rely on:

- Jinja templates
- CSS files
- images
- JavaScript assets

When deployed, all of those still need to resolve correctly. That is why Flask lessons use `url_for()` instead of hardcoded file paths.

For example:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
```

Using `url_for()` keeps the template portable. Whether the app runs locally or on a hosted domain, Flask can generate the correct URL to the static asset.

This is a good example of deployment shaping how you write application code. A small decision in the template layer can make the difference between a working production page and broken CSS.

## 6. Database Persistence Changes in Production

Local Flask projects often use SQLite because it is easy to set up:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
```

That is perfectly fine while learning, but deployment introduces a new question: where does the data live?

On many platforms, the application container or file system may be temporary. If you rely only on a local SQLite file inside that environment, your data may not survive redeploys the way you expect.

This is why production apps often move to a managed database such as PostgreSQL. The application code still talks to SQLAlchemy, but the database itself lives in a persistent service.

A common pattern is:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "sqlite:///blog.db",
)
```

That lets you keep SQLite for local development while using a hosted database in production.

## 7. A Practical Deployment Checklist for These Flask Projects

For the blog-style projects in this course, deployment usually comes down to a short checklist:

1. Make sure the app runs locally without hidden assumptions.
2. Move secrets into environment variables.
3. Confirm `requirements.txt` is current.
4. Use a production start command such as `gunicorn main:app`.
5. Check that templates, forms, and static files still load correctly.
6. Decide whether SQLite is acceptable or whether the app needs a persistent hosted database.

This checklist is useful because deployment errors are often not Python language errors. They come from configuration gaps:

- a missing package
- an unset environment variable
- a bad database URL
- a missing static asset path

Thinking in terms of deployment readiness helps you catch those issues before pushing the app live.

## 8. Why This Day Matters in the Course

Deployment is a transition point. Earlier lessons were about building features. From here onward, the course also starts treating software as something that must be packaged, shared, and maintained.

That mindset matters for the rest of the repository:

- data projects need reproducible environments
- web apps need configuration discipline
- automation scripts still benefit from clean dependencies and version control

In other words, deployment is not just about Flask hosting. It teaches you to think about software as a complete system.

## How to Run the Lesson Locally

This day is mostly conceptual, but you can rehearse the deployment mindset by taking one of the recent Flask projects and checking that it is ready to move beyond localhost.

From a Flask project folder:

```bash
pip install -r requirements.txt
python main.py
```

Then verify:

- the app starts without missing imports
- required secrets are read from environment variables
- static files load correctly
- the project can be started by a process command such as `gunicorn main:app`

## Summary

Day 71 explains what changes when a Flask app leaves your laptop and starts running in a production environment. You learned why the development server is not enough for public traffic, how environment variables protect configuration, why `requirements.txt` is part of the deployment contract, and how static files and database choices affect a hosted application. That perspective turns deployment from a mysterious platform step into a practical extension of how you structure Python projects.
