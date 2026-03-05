# Day 75 - Resampling and Visualizing Time Series

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Resampling and Visualizing Time Series** and avoids generic cross-day boilerplate.

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

You build **Resampling and Visualizing Time Series** as a day-specific project using `notebook`.
Primary entrypoint: `Google Trends and Data Visualisation.ipynb`.

## 2. Core Concepts

- Day-specific stack and techniques: `notebook`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 1. Data Exploration - Making Sense of Google Search Data
- I've gone ahead and already added the import statements and created the four different DataFrames in this notebook.
- Your first step is to explore the data, by getting an understanding of what's actually in those .csv files for this project.

## 3. Project Structure

- `Google Trends and Data Visualisation.ipynb`: Primary analysis notebook.
- `Bitcoin Search Trend.csv`: Dataset/input data consumed by the day project.
- `Daily Bitcoin Price.csv`: Dataset/input data consumed by the day project.
- `TESLA Search Trend vs Price.csv`: Dataset/input data consumed by the day project.
- `UE Benefits Search vs UE Rate 2004-19.csv`: Dataset/input data consumed by the day project.
- `UE Benefits Search vs UE Rate 2004-20.csv`: Dataset/input data consumed by the day project.

## 4. Implementation Walkthrough

1. Run notebook cells in order to preserve variable state and reproducible results.
2. Inspect and clean data before plotting or statistical interpretation.
3. Document conclusions directly beside code so insights remain auditable.

## 5. Day Code Snippet

Excerpt from `Google Trends and Data Visualisation.ipynb`:
```python
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
```

## 6. How to Run

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

- **Resampling and Visualizing Time Series** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
