# Day 98 - Practical Python Automation Workflows

Day 98 is unusual because the repository does not contain a finished automation script yet. The `main.py` file is only a placeholder:

```python
# To be done when neeeded
```

That means the real lesson is not "read this completed implementation." It is "design and build an automation from scratch using everything you have learned so far."

This is still a valuable day because open-ended project prompts are where tutorial knowledge either becomes practical skill or stays theoretical.

## 1. Start With a Repetitive Workflow Worth Automating

Automation is only useful when it removes repeated manual work. A good project for this day usually has three qualities:

- it happens often
- it follows a clear sequence of steps
- it benefits from consistency more than from human judgment

Typical candidates include:

- renaming or reorganizing files
- scraping and exporting routine reports
- sending status emails
- processing PDFs or images in batches
- turning web data into CSV summaries

The important design move is choosing a task with clear inputs and outputs before writing code.

## 2. Break the Automation Into Stages

Even without a finished script in the repo, the right structure is predictable. Most Python automation jobs can be split into a pipeline such as:

1. gather input
2. validate it
3. perform the repeated transformation
4. save or publish the result
5. report success or failure

That architecture matters because automation can become brittle very quickly if file access, parsing, output generation, and error handling are all mixed together.

This is one of the biggest shifts from tutorial code to real software: the script should be understandable even when it runs unattended.

## 3. Design for Reliability, Not Just Convenience

Automation scripts often fail in predictable places:

- missing files
- malformed input
- changed web pages or APIs
- permission issues
- partial output from interrupted runs

That is why a practical automation script should usually include:

- explicit validation up front
- clear error messages
- idempotent or predictable output naming
- a way to rerun safely

The fact that the repository leaves the implementation open is actually useful here. It forces you to think about the workflow before coding the mechanics.

## 4. Use Earlier Course Skills as Building Blocks

By Day 98, you already have enough tools to build strong automations:

- file handling from earlier Python projects
- pandas for cleanup and export
- requests and BeautifulSoup for data collection
- Selenium for browser-driven automation
- Flask if the output needs a web UI
- cloud services or email APIs if the automation must publish results

A strong Day 98 project is usually not a brand-new idea. It is a composition of earlier skills into one repeatable workflow.

## How to Run the Day 98 Project

At the moment, there is no completed automation flow in the repository beyond the placeholder `main.py`, so there is nothing meaningful to execute yet beyond opening the file.

If you use this day as intended, the run path becomes:

1. define the workflow you want to automate
2. implement the script in `main.py`
3. add any dependencies required by that workflow
4. run the resulting automation with the input files or services it expects

## Summary

Today, the lesson is the blank space itself. The repository does not hand you a finished automation, which forces you to choose a real workflow, design the steps, and build the script yourself. That is the point of the project phase: moving from guided examples to work you can specify and implement on your own.
