# Day 78 - Linear Regression and Seaborn Statistical Plots

Today, we use a movie dataset to answer a simple question with more discipline than a plain scatter plot would give us: does spending more on a film usually lead to higher worldwide revenue?

This lesson is not just about drawing a line through a cloud of points. It is about cleaning the data first, deciding which rows belong in the model, and then using Seaborn and scikit-learn to describe the relationship honestly.

## 1. Inspect and Clean the Dataset

The notebook starts with the normal exploration pass:

```python
data = pd.read_csv('./MovieData2023.csv')

print(data.shape)
print(data.head())
print(data.isna().values.any())
print(data.duplicated().values.any())
data.info()
```

This matters because a regression model can look mathematically neat even when the source columns are still strings.

The money fields need type conversion first:

```python
chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        data[col] = data[col].astype(str).str.replace(char, "")
    data[col] = pd.to_numeric(data[col])
```

That loop is a good cleanup pattern because it avoids repeating the same transformation three times.

The release date column also needs normalization:

```python
data.Release_Date = data.Release_Date.astype(str).str.replace("Unknown", "")
data.Release_Date = pd.to_datetime(data.Release_Date, format='mixed')
```

At this point, the dataset is finally shaped for arithmetic and modeling.

## 2. Decide Which Films Belong in the Analysis

A lot of the early notebook work is not about the regression line at all. It is about identifying records that would distort the story.

For example, the notebook checks films with zero domestic gross:

```python
zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)
```

Rows like these often represent one of three things:

- unreleased films
- incomplete records
- films that never entered the market you are studying

That is why filtering matters before modeling. If the target column mixes real commercial failures with not-yet-released films, the fitted line becomes harder to interpret.

## 3. Use Seaborn to See the Relationship

Once the table is clean enough, Seaborn gives you a compact way to plot both the scatter and the fitted trend:

```python
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})
```

`regplot()` is useful because it keeps the chart readable while still carrying statistical meaning. You see the spread of the data and the overall direction at the same time.

The notebook then compares newer films with different styling and tighter axis control:

```python
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("darkgrid"):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     scatter_kws={'alpha': 0.4, 'color': '#2f4b7c'},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 470000000),
           ylabel="Revenue in $ billions",
           xlabel='Budget in $100 millions')
```

That is a good reminder that visualization is part of model interpretation. If the axes are uncontrolled or the scatter is too dense, the plot becomes much harder to read.

## 4. Quantify the Trend with scikit-learn

Seaborn shows the relationship. Scikit-learn lets you quantify it.

```python
regression = LinearRegression()
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

regression.fit(X, y)
```

This defines a simple linear model:

- `X` is the production budget
- `y` is worldwide gross revenue

The fitted line summarizes the average relationship inside the cleaned dataset. It does **not** prove that budget alone determines success. Movie performance depends on far more than production cost:

- release timing
- franchise strength
- marketing
- competition
- international reach

That is why the regression is valuable as a summary, not as a law of filmmaking.

## How to Run the Regression Notebook

1. Install the dependencies:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
2. Open `Seaborn_and_Linear_Regression.ipynb` from this folder.
3. Run the cleaning cells before the plotting or regression cells.
4. Verify the main milestones:
   - money columns are numeric
   - release dates are parsed
   - the Seaborn regression plot renders correctly
   - the `LinearRegression()` model fits on the cleaned subset

## Summary

Today, you learned that regression starts with data preparation, not with the model class. You cleaned currency fields, handled questionable rows, visualized the relationship with Seaborn, and then quantified it with scikit-learn. The important habit is not memorizing the API. It is deciding what data belongs in the model before you trust the line it gives back.
