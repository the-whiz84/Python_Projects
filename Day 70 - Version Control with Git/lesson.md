# Day 70 - Version Control: The Architecture of Git

Git becomes important the moment a project stops being a single throwaway script. This day uses a tiny Flask app to show why version control matters: the code is simple, but it already has source files, dependencies, environment variables, and files that should never be committed.

Instead of treating Git as a list of commands to memorize, this lesson is about understanding the workflow that keeps a Python project safe, reviewable, and easy to change.

## 1. Why Version Control Matters Even on Small Python Projects

The project for this day is only a few files:

- `main.py` runs a Flask app
- `requirements.txt` records dependencies
- `.gitignore` keeps local junk and secrets out of version control

That is enough structure for real problems to appear:

- you can break a working route while experimenting
- you can forget which version of the app matched a screenshot or tutorial step
- you can accidentally commit local environment files or credentials

Git solves those problems by storing a history of snapshots. Each commit is a named checkpoint you can inspect, compare, or restore later.

In practice, that means you can try a change like adding a new route, updating a dependency, or reorganizing configuration without losing the last known-good version of the project.

## 2. The Working Tree, Staging Area, and Commit History

The most important Git concept for beginners is that there are three different states for your files.

### Working tree

This is what is currently on disk in your project folder. If you edit `main.py`, the change lives here first.

### Staging area

This is the review step before a commit. You choose which changes belong in the next snapshot.

### Commit history

Once committed, the snapshot becomes part of the repository timeline.

That gives you a clean workflow:

```bash
git status
git add main.py
git commit -m "Add superhero name Flask route"
```

The point of staging is not ceremony. It is control. If you changed `main.py` and also updated `requirements.txt`, Git lets you decide whether those belong in one commit or two separate ones.

That matters more as projects grow, because small focused commits are much easier to review and much easier to undo.

## 3. Using This Project to Understand What Should Be Tracked

The Flask app is short, but it shows a realistic split between code you want in git and machine-specific files you do not.

The application code belongs in the repository:

```python
from flask import Flask
from getname import random_name
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
```

This code should be versioned because it defines how the app behaves.

The secret value behind `FLASK_KEY` should not be versioned. You want the code that reads the environment variable, but not the actual secret stored in your local `.env` file. That separation is one of the first professional habits Git teaches.

The same logic applies to generated files and local tooling state. The `.gitignore` file in this folder already blocks things like Python cache files and local editor noise so the repository stays focused on the source.

## 4. Reading `.gitignore` Like a Python Developer

Many Git lessons explain `.gitignore` too quickly, but for Python work it is essential.

You usually want to ignore:

- `__pycache__/`
- `.env`
- virtual environments such as `venv/`
- editor-specific files

The goal is not just tidiness. It is portability.

If another developer clones the repo, they should get:

- the application code
- the dependency list
- the template or asset files the app needs

They should not get:

- your machine-specific cache files
- your interpreter state
- your private keys

That is why `.gitignore` is part of the project architecture, not an afterthought.

## 5. A Practical Commit Workflow for Tutorial Projects

The safest way to use Git while learning is to commit at meaningful checkpoints, not after every keystroke and not only at the end of the day.

Good commit moments for a project like this are:

- after the Flask app runs successfully
- after environment variables are wired in correctly
- after `.gitignore` is protecting local-only files
- after dependency changes are reflected in `requirements.txt`

A clean workflow looks like this:

```bash
git status
git add main.py requirements.txt .gitignore
git commit -m "Set up Flask app with environment-based secret key"
```

That message tells future-you exactly what changed and why that commit exists.

If you later introduce a bug, `git log` and `git diff` make it much easier to trace when the app stopped working. For a tutorial repo with 100 days of projects, that history becomes extremely valuable.

## 6. Branches and Why They Matter Before Teamwork Starts

Branches are often introduced as a team feature, but they help even when you are working alone.

If you want to experiment with a new route, a refactor, or a deployment-specific change, you can create a branch instead of risking the stable version of your project.

```bash
git checkout -b feature/deployment-config
```

Now you can try changes freely. If the experiment works, merge it. If it fails, you can discard that branch without damaging your main line of progress.

This is one of the reasons Git feels so different from keeping backup copies like `main_old.py` or `project-final-final-v2`. Git gives structure to experimentation.

## 7. Git as Part of the Development Process

By Day 70, version control is no longer optional background knowledge. The rest of the course includes deployment, data projects, APIs, and larger app structures. Those topics are much easier to manage when every project has a clear history.

The big idea is simple:

- code belongs in git
- secrets and generated files do not
- commits should describe one meaningful change
- branches let you experiment safely

Once those habits are in place, Git stops feeling like an extra tool and starts feeling like part of how you write Python professionally.

## How to Run the Project

Install the dependencies, create a local `.env` file with `FLASK_KEY`, and run the Flask app:

```bash
pip install -r requirements.txt
python main.py
```

While working, use Git from the project folder to inspect and save your progress:

```bash
git status
git add .
git commit -m "Describe the checkpoint clearly"
```

## Summary

Day 70 turns Git into part of your normal Python workflow. You learned how the working tree, staging area, and commit history fit together, why `.gitignore` protects the quality of a repository, and how this small Flask app already shows the difference between source code that should be tracked and secrets or cache files that should not. That foundation matters for every project that follows, because from this point on you are maintaining software, not just writing isolated scripts.
