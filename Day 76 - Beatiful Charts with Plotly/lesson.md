# Day 76 - Beatiful Charts with Plotly

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Beatiful Charts with Plotly** and avoids generic cross-day boilerplate.

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

You build **Beatiful Charts with Plotly** as a day-specific project using `notebook`.
Primary entrypoint: `Google Play Store App Analytics.ipynb`.

## 2. Core Concepts

- Day-specific stack and techniques: `notebook`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- Google Play Store Analytics
- 1. Data Cleaning: Removing NaN Values and Duplicates
- The first step as always is getting a better idea about what we're dealing with.

## 3. Project Structure

- `Google Play Store App Analytics.ipynb`: Primary analysis notebook.
- `apps.csv`: Dataset/input data consumed by the day project.
- `requirements.txt`: Project resource used by this day.

## 4. Implementation Walkthrough

1. Run notebook cells in order to preserve variable state and reproducible results.
2. Inspect and clean data before plotting or statistical interpretation.
3. Document conclusions directly beside code so insights remain auditable.

## 5. Day Code Snippet

Excerpt from `Google Play Store App Analytics.ipynb`:
```python
# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format
# Solve error warning for future version when removing duplicates
pd.options.mode.copy_on_write = True
```

## 6. How to Run

```bash
pip install -r requirements.txt
```
```bash
jupyter notebook
```

## 7. Common Pitfalls and Debug Tips

- Check nulls and dtypes before aggregations or charts to avoid misleading results.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Beatiful Charts with Plotly** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
