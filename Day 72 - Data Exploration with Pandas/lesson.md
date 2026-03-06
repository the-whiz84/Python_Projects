# Day 72 - Data Exploration: Mastering Pandas

Day 72 is the point where the course starts treating data as something you inspect, clean, and reason about before you ever try to visualize it. The dataset looks simple, but it already contains the kinds of issues you see in real analysis work: missing values, columns with long descriptive names, and salary fields that only become useful once you start comparing them systematically.

The main skill for this lesson is not memorizing Pandas methods. It is learning a repeatable exploration workflow.

## 1. Reading a Dataset into a DataFrame

Pandas gives you a DataFrame, which is the core structure used for almost every tabular analysis in the rest of the course.

The salary dataset is loaded from CSV like this:

```python
import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
```

At that point, Pandas has given you a table with named columns and indexed rows. That sounds basic, but it changes how you work. Instead of manually looping through lines in a file, you can ask direct questions about the data:

- how many rows are there?
- which columns exist?
- where are the missing values?
- which majors have the highest or lowest pay?

That is the first mental shift in data analysis: you stop thinking in terms of raw file handling and start thinking in terms of column operations.

## 2. Inspect Before You Analyze

The notebook does not jump straight into conclusions. It starts with inspection:

```python
df.head()
df.shape
df.columns
df.isna()
df.tail()
```

This is an important habit. In Pandas, you can write a correct-looking calculation against the wrong assumptions very easily. A quick inspection pass tells you:

- whether the dataset loaded the way you expected
- whether column names match the ones you plan to use
- whether the last rows contain missing values
- whether the scale of the dataset is small or large enough to influence your approach

For this dataset, that inspection reveals that not every major has complete salary information. That matters, because salary comparisons stop being reliable if one side of the comparison is missing.

## 3. Cleaning Missing Values Before Doing Any Salary Ranking

The notebook handles incomplete rows with:

```python
clean_df = df.dropna()
```

This line is doing more than cleanup for appearance. It is protecting the later analysis.

Without that step, rankings like "highest mid-career salary" or "lowest starting salary" can behave unpredictably if the relevant cells contain `NaN`. Sometimes Pandas skips missing values for you, sometimes the missing values survive farther into the workflow than you expect. Cleaning first makes the later questions much easier to trust.

This is also a good place to remember a broader Python lesson: data problems are rarely solved by one magical library call. Good analysis usually comes from a sequence of small, understandable preparation steps.

## 4. Finding Extremes with Index-Based Lookups

Once the dataset is clean, the notebook starts asking useful questions about the majors.

For example, the highest starting salary can be found by locating the row index of the maximum value:

```python
clean_df["Starting Median Salary"].idxmax()
clean_df["Starting Median Salary"].loc[43]
clean_df["Undergraduate Major"].loc[43]
```

The same pattern is used for:

- highest mid-career salary
- lowest starting salary
- the major with the lowest risk based on salary spread

This is one of the first places where Pandas feels different from plain Python lists. You are not manually scanning each record. Instead, you use a column operation to find the interesting row, then pull the related values from that row.

That pattern shows up constantly in analysis work.

## 5. Feature Engineering: Creating the Salary Spread Column

One of the best parts of this lesson is that it does not stop at the columns provided by the dataset. It creates a new one:

```python
spread_col = (
    clean_df["Mid-Career 90th Percentile Salary"]
    - clean_df["Mid-Career 10th Percentile Salary"]
)

clean_df.insert(1, "Spread", spread_col)
```

This is feature engineering in a very approachable form. You are deriving a new measure from existing columns so the dataset can answer a better question.

In this case, `Spread` helps describe salary variability. A large spread suggests a wider gap between lower and higher earners in that major. A smaller spread suggests more consistency.

That matters because "highest average pay" is not the only meaningful career question. The notebook starts moving from raw ranking into interpretation:

- Which major pays the most?
- Which major has the most upside?
- Which major appears more stable?

This is where Pandas starts to feel like a tool for thinking, not just for data storage.

## 6. Sorting Turns Raw Data into Decisions

After adding `Spread`, the notebook sorts the DataFrame in different ways:

```python
low_risk = clean_df.sort_values("Spread")
highest_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary")
highest_spread = clean_df.sort_values("Spread", ascending=False)
```

Sorting is simple, but it is central to exploratory analysis. Once the rows are ordered by a meaningful metric, patterns become much easier to see.

This is also a good example of why column names matter. Pandas lets you write very expressive code if the dataset is well labeled. Instead of a vague loop or index math, the code reads like the question you are asking.

## 7. Grouping by Major Category

The lesson becomes more interesting when it stops looking only at individual majors and starts grouping them into broader categories such as engineering, business, or humanities.

The notebook uses `groupby()` to compute mean values per group:

```python
pd.options.display.float_format = "{:,.2f}".format

numeric_df = clean_df.select_dtypes(include=["number"])
clean_df.groupby("Group")[numeric_df.columns].mean()
```

This is an important step because it introduces aggregation. Instead of asking about one row at a time, you ask what tends to happen across a category.

That shift is the foundation for later lessons on grouped time-series data, merged tables, and regression work. Once you understand `groupby()`, you can move between granular and summary views of a dataset much more naturally.

## 8. The Extra-Credit Script Connects Scraping to Pandas

The `main.py` file extends the lesson by pulling a live salary table from PayScale and converting it directly into a DataFrame:

```python
html_data = requests.get(url, headers=header)
df = pd.read_html(StringIO(html_data.text))[0]
```

Then it cleans the scraped table by removing the `Rank` column and stripping text prefixes:

```python
df = df.drop("Rank", axis=1)
df.loc[:, "Major"] = df["Major"].str.replace("Major:", "")
df.loc[:, "Degree Type"] = df["Degree Type"].str.replace("Degree Type:", "")
```

That is a useful bridge from the earlier web scraping section of the course. You are no longer scraping just to print text to the terminal. You are scraping so the result can enter a Pandas workflow and be analyzed like any other dataset.

## 9. Why This Lesson Matters for the Rest of the Course

Day 72 teaches a pattern that comes up again and again:

1. load the data
2. inspect the shape and columns
3. remove or repair invalid rows
4. derive better features
5. sort or group the data to answer real questions

The exact dataset changes later, but that thinking process stays the same.

If you build that habit now, the later visualization and machine learning lessons become much easier, because you already know how to prepare data before asking it for answers.

## How to Run the Project

Install the required packages and run the extra-credit script:

```bash
pip install pandas requests lxml
python main.py
```

For the main lesson workflow, open `college_salaries.ipynb` in Jupyter, VS Code, or Google Colab and run the notebook cells in order. As you work through it, check:

- which rows contain missing salary data
- which major has the highest starting salary
- how the new `Spread` column changes the analysis
- how the grouped averages differ across major categories

## Summary

Day 72 introduces Pandas as a tool for structured exploration rather than just CSV loading. You learned how to inspect a dataset, remove incomplete rows, locate important records with index-based lookups, create new analytical features such as salary spread, and summarize broader trends with `groupby()`. That combination of inspection, cleaning, and interpretation is the foundation for the rest of the data section of the course.
