# Day 80 - t-Tests and Distributions

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **t-Tests and Distributions** and avoids generic cross-day boilerplate.

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

You build **t-Tests and Distributions** as a day-specific project using `notebook`.
Primary entrypoint: `Dr_Semmelweis_Handwashing_Discovery.ipynb`.

## 2. Core Concepts

- Day-specific stack and techniques: `notebook`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- t-Tests and Distributions
- Today you will become a doctor, but not just any doctor. You will become Dr Ignaz Semmelweis, a Hungarian physician born in 1818 who worked in the Vienna General Hospital.
- In the past, people didn't know about bacteria, germs, or viruses. People illness was caused by "bad air" or evil spirits. But in the 1800s Doctors started looking more at anatomy, doing autopsies and making arguments based on data. Dr Semmelweis suspected that something was going wrong with the procedures at Vienna General Hospital. Dr Semmelweis wanted to figure out why so many women in maternity wards were dying from childbed fever (i.e., puerperal fever).

## 3. Project Structure

- `Dr_Semmelweis_Handwashing_Discovery.ipynb`: Primary analysis notebook.
- `annual_deaths_by_clinic.csv`: Dataset/input data consumed by the day project.
- `monthly_deaths.csv`: Dataset/input data consumed by the day project.
- `requirements.txt`: Project resource used by this day.

## 4. Implementation Walkthrough

1. Run notebook cells in order to preserve variable state and reproducible results.
2. Inspect and clean data before plotting or statistical interpretation.
3. Document conclusions directly beside code so insights remain auditable.

## 5. Day Code Snippet

Excerpt from `Dr_Semmelweis_Handwashing_Discovery.ipynb`:
```python
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scipy.stats as stats
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

- **t-Tests and Distributions** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.
