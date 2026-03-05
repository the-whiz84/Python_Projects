# Day 72 - Data Exploration with Pandas

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Data Exploration with Pandas** and avoids generic cross-day boilerplate.

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

You build **Data Exploration with Pandas** as a day-specific project using `requests`, `pandas`, `notebook`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `requests`, `pandas`, `notebook`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 1. Getting Set Up for Data Science
- Introducing the <Google Colab Notebook>
- PyCharm is a fantastic IDE, but when we're exploring and visualizing a dataset, you'll find the Python notebook format better suited.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `college_salaries.ipynb`: Primary analysis notebook.
- `salaries_by_college_major.csv`: Dataset/input data consumed by the day project.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Load tabular data, clean null/edge values, then compute the target metrics.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
header = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15",
  "sec-fetch-dest": "document",
  "Accept-Language": "en-US,en;q=0.9",
  "X-Requested-With": "XMLHttpRequest"
}
html_data = requests.get(url, headers=header)

# create data frame by importing html data
df = pd.read_html(StringIO(html_data.text))[0]

# clean up data frame
df = df.drop('Rank', axis=1)
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- External sites/APIs change often; verify selectors/fields before assuming parser bugs.
- Check nulls and dtypes before aggregations or charts to avoid misleading results.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Data Exploration with Pandas** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
