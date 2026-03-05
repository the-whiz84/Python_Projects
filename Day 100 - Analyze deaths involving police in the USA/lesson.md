# Day 100 - Analyze deaths involving police in the USA

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Analyze deaths involving police in the USA** and avoids generic cross-day boilerplate.

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

You build **Analyze deaths involving police in the USA** as a day-specific project using `notebook`.
Primary entrypoint: `Fatal_Force.ipynb`.

## 2. Core Concepts

- Day-specific stack and techniques: `notebook`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `Fatal_Force.ipynb`: Primary analysis notebook.
- `Deaths_by_Police_US.csv`: Dataset/input data consumed by the day project.
- `Median_Household_Income_2015.csv`: Dataset/input data consumed by the day project.
- `Pct_Over_25_Completed_High_School.csv`: Dataset/input data consumed by the day project.
- `Pct_People_Below_Poverty_Level.csv`: Dataset/input data consumed by the day project.
- `Share_of_Race_By_City.csv`: Dataset/input data consumed by the day project.

## 4. Implementation Walkthrough

1. Run notebook cells in order to preserve variable state and reproducible results.
2. Inspect and clean data before plotting or statistical interpretation.
3. Document conclusions directly beside code so insights remain auditable.

## 5. Day Code Snippet

Excerpt from `Fatal_Force.ipynb`:
```python
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# This might be helpful:
from collections import Counter
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

- **Analyze deaths involving police in the USA** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
