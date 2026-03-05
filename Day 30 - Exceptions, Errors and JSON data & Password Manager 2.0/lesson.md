# Day 30 - Exceptions, Errors and JSON data & Password Manager 2.0

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Exceptions, Errors and JSON data & Password Manager 2.0** and avoids generic cross-day boilerplate.

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

You build **Exceptions, Errors and JSON data & Password Manager 2.0** as a day-specific project using `tkinter`, `pandas`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `tkinter`, `pandas`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `main_password_manager_2_0.py`: Service module that encapsulates external/data operations.
- `nato_alphabet.py`: Supporting module for project logic.
- `nato_phonetic_alphabet.csv`: Dataset/input data consumed by the day project.

## 4. Implementation Walkthrough

1. Collect and validate user input before performing transformations.
2. Read/write JSON safely with existence checks and fallback defaults.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
json.dump(data, data_file, indent=4)

# Read
# json.load()
data = json.load(data_file)

# Update data
# json.update()
#1. Reading old data
data = json.load(data_file)
#2. Updating old data with new data
data.update(new_data)
#3. Saving updated data
json.dump(data, data_file, indent=4)
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- Check nulls and dtypes before aggregations or charts to avoid misleading results.
- Keep state updates in one place; desynchronized UI/game state causes subtle bugs.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Exceptions, Errors and JSON data & Password Manager 2.0** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
