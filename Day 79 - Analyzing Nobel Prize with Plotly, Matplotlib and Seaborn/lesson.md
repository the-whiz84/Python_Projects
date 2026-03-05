# Day 79 - Analyzing Nobel Prize with Plotly, Matplotlib and Seaborn

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Analyzing Nobel Prize with Plotly, Matplotlib and Seaborn** and avoids generic cross-day boilerplate.

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

You build **Analyzing Nobel Prize with Plotly, Matplotlib and Seaborn** as a day-specific project using `notebook`.
Primary entrypoint: `Nobel_Prize_Analysis.ipynb`.

## 2. Core Concepts

- Day-specific stack and techniques: `notebook`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- Analyzing the Nobel Prize with Plotly, Matplotlib and Seaborn
- Today we're going to analyze a dataset on the past winners of the Nobel Prize. Let's see what patterns we can uncover in the past Nobel laureates and what can we learn about the Nobel prize and our world more generally.
- On November 27, 1895, Alfred Nobel signed his last will in Paris. When it was opened after his death, the will caused a lot of controversy, as Nobel had left much of his wealth for the establishment of a prize.

## 3. Project Structure

- `Nobel_Prize_Analysis.ipynb`: Primary analysis notebook.
- `nobel_prize_data.csv`: Dataset/input data consumed by the day project.
- `requirements.txt`: Project resource used by this day.

## 4. Implementation Walkthrough

1. Run notebook cells in order to preserve variable state and reproducible results.
2. Inspect and clean data before plotting or statistical interpretation.
3. Document conclusions directly beside code so insights remain auditable.

## 5. Day Code Snippet

Excerpt from `Nobel_Prize_Analysis.ipynb`:
```python
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
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

- **Analyzing Nobel Prize with Plotly, Matplotlib and Seaborn** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
