# Python 100 Days of Code Projects

This repository collects my project work from Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*. It now includes a full lesson pass across the repo, so each project folder has one canonical `lesson.md` written in a consistent instructor style.

## Current Repo State

- `94` day folders are present in this repository.
- Each day folder keeps one canonical lesson file: `lesson.md`.
- Folder names follow the `Day XX - ...` pattern and have been compacted where older names were too long.
- Later lessons were expanded to match project complexity instead of collapsing into short summaries.

## What the Repository Covers

The projects move through the same progression as the course:

- Python fundamentals, control flow, functions, and OOP
- Turtle, Tkinter, PyQt, and game projects
- APIs, JSON, scraping, Selenium, and automation
- Flask apps with templates, forms, auth, and databases
- Pandas, NumPy, Matplotlib, Seaborn, Plotly, and data analysis
- Capstones that combine several skills in one project

## Repository Layout

Each project lives in its own day folder, for example:

- `Day 01 - Band Name`
- `Day 37 - HTTP Methods and Auth Headers`
- `Day 67 - Flask Blog CMS with Editing`
- `Day 77 - NumPy Arrays and Vectorized Computation`
- `Day 100 - Police Deaths in the USA`

Most folders contain some combination of:

- `main.py` or another entry script
- notebooks such as `.ipynb`
- local datasets or static assets
- `requirements.txt`
- `lesson.md`

## How to Use the Repo

### Read a lesson

Open the `lesson.md` inside any day folder first. It explains the project structure, the main concepts, and how to run that specific day.

### Run a project

Many folders can be run directly from their own directory:

```bash
cd "Day XX - Project Name"
python main.py
```

Some days use notebooks instead of a single script. For those, open the `.ipynb` file in Jupyter, VS Code, or Google Colab.

### Install dependencies

Some day folders include their own `requirements.txt`. Install dependencies from inside the project folder when needed:

```bash
pip install -r requirements.txt
```

## Notes

- Not every numbered course day appears as a separate folder. Some projects were combined, and the repo reflects the actual project set rather than a placeholder folder for every calendar day.
- Some projects require external services or credentials such as AWS, third-party APIs, or browser automation tooling. Those setup details are documented in the relevant day folder and lesson.
- The repo includes both script-based projects and notebook-based analysis work, so the correct run path depends on the day.

## External Project Repos

- [Capstone Blog Project](https://github.com/the-whiz84/Capstone_Blog_Project)
- [Flask ToDo App](https://github.com/the-whiz84/Flask-ToDo-App)
- [E-Shop Demo](https://github.com/the-whiz84/E-Shop-demo)
