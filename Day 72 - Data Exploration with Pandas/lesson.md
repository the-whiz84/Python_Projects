# Day 72 - Data Exploration: Mastering Pandas

Today, we transition from building applications to **Analyzing Data**. In the professional world, data is rarely "ready" for a chart. It is messy, missing values, and buried in complex formats.

We are using **Pandas**—the industry-standard library for data manipulation. Today, we bridge the gap between our web scraping skills and data science by extracting and cleaning college salary data to find which majors actually pay off.

## 1. The Data Science Pipeline: ETL

Every data project follows the **ETL** (Extract, Transform, Load) architecture:

1.  **Extract**: Grabbing data from a CSV, a Database, or even directly from a website's HTML table.
2.  **Transform**: "Cleaning" the data. Removing null values, fixing data types, and stripping unwanted characters.
3.  **Load**: Loading the clean data into a **DataFrame** for analysis.

In `main.py`, we used a bridge between scraping and data science:

```python
# Extracting directly from a live URL using Pandas read_html
df = pd.read_html(StringIO(html_data.text))[0]
```

## 2. Pandas Architecture: Series vs. DataFrames

To master Pandas, you must understand its two fundamental data structures:

- **Series**: A 1-dimensional array. Think of it as a single column in an Excel sheet. Every element has an **Index**.
- **DataFrame**: A 2-dimensional table. Think of it as the entire Excel sheet. It is essentially a collection of **Series** objects sharing the same Index.

## 3. The Art of Data Inspection

Before you write a single line of analysis, you must "interview" your data. We use these critical commands:

- **`df.head()`**: See the first 5 rows to understand the structure.
- **`df.shape`**: See how many rows and columns you are dealing with (e.g., `(51, 6)`).
- **`df.columns`**: See the exact names of your columns (crucial for typos!).
- **`df.isna()`**: Identify where data is missing.

## 4. Architectural Cleaning: Handling the Garbage

Data Science follows the **GIGO** rule: _Garbage In, Garbage Out_. If your dataset has "NaN" (Not a Number) values in a salary column, your "Average" calculation will be wrong.

We implemented professional cleaning by removing incomplete rows:

```python
# Removing the last row or any row with missing data
clean_df = df.dropna()
```

We also "normalized" our strings. Notice how we used `.str.replace()` to strip currency symbols and descriptive prefixes, allowing us to convert the column to a numeric type later.

## 5. Fetching Insights: Accessing Data

We learned how to "slice" our data like a pro:

- **By Column**: `df['Major']` or `df[['Major', 'Early Career Pay']]`.
- **By Row (Location)**: `df.loc[0]` (access by label) or `df.iloc[0]` (access by integer position).

## How to Run the Salary Explorer

1.  **Environment Setup**:
    Install the Data Science stack:
    ```bash
    pip install pandas lxml requests
    ```
2.  **Launch**:
    You can run the script directly:
    ```bash
    python main.py
    ```
    _Alternatively, open `college_salaries.ipynb` in VS Code or Google Colab for an interactive experience._
3.  **Verification**:
    - Look at the `head()` output.
    - Notice how "Petroleum Engineering" leads the pack in early career pay.
    - Verify that the "Rank" column was dropped successfully to simplify the analysis.

## Summary

Today, you learned that being a Data Scientist is 80% cleaning and 20% calculating. You mastered the ETL pipeline, learned the difference between Series and DataFrames, and built a robust "Inspection" workflow to ensure your data stays clean.

Tomorrow, we add "Eyes" to our data! We will learn **Matplotlib** to turn these raw numbers into compelling, professional visualizations.
