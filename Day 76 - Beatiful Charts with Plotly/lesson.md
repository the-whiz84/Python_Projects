# Day 76 - Interactive Analytics Dashboards with Plotly

Today, we move from static charts to interactive ones, but the real lesson is still data preparation. Plotly can make a chart feel modern and responsive, but it cannot rescue a dataset full of missing ratings, duplicate apps, text-valued numbers, and outliers that flatten the scale.

The Play Store project works because the cleanup and the chart design support each other.

## 1. Clean the App Store Dataset

The notebook starts by making the raw table easier to work with:

```python
pd.options.display.float_format = '{:,.2f}'.format
pd.options.mode.copy_on_write = True

df_apps = pd.read_csv('apps.csv')
df_apps.drop(columns=['Last_Updated', 'Android_Ver'], inplace=True)
```

That early cleanup is useful for two reasons:

- it removes fields that are not part of the analysis
- it makes the remaining table easier to reason about

The next step is handling incomplete rows:

```python
df_apps_clean = df_apps.dropna()
df_apps_clean.isna()
```

For an exploratory notebook, this is a reasonable trade. The goal is not perfect imputation. The goal is a dependable working set for the charts that come later.

## 2. Remove Duplicates and Convert Text to Numbers

Marketplace scrapes often include the same app more than once. If you ignore that, your category counts and install totals get inflated.

```python
df_apps_clean.drop_duplicates(subset='App', keep='first', inplace=True)
```

The key detail is `subset='App'`. A full-row duplicate check would miss many practical duplicates because two entries for the same app can differ in review count or other secondary fields.

The notebook then fixes the numeric columns stored as strings. `Installs` arrives with commas:

```python
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
```

And `Price` arrives with currency formatting:

```python
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
```

Filtering the extreme prices is a practical move. One novelty app with a huge price tag can distort the scale and make the real market hard to see.

## 3. Choose Plotly Charts That Fit the Question

The first Plotly chart is a donut chart for content ratings:

```python
ratings = df_apps_clean.Content_Rating.value_counts()

fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             hole=0.6)

fig.update_traces(textposition='inside', textinfo='percent', textfont_size=15)
fig.show()
```

This works because the categories are mutually exclusive and the user benefits from hover-based exploration.

The notebook then groups installs by category and moves to a horizontal bar chart:

```python
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

h_bar = px.bar(x=category_installs.Installs,
               y=category_installs.index,
               orientation='h')
h_bar.show()
```

The horizontal orientation is the right choice because category names are text-heavy. A vertical chart would spend too much of its visual budget on rotated labels.

## 4. Build Better Category Comparisons with Aggregation and Merge

One of the stronger ideas in the notebook is category concentration. Total installs alone do not tell the whole story. A category with huge installs and very few apps means something different from a category with huge installs spread across thousands of apps.

To compare those two dimensions, the notebook combines app counts with install totals:

```python
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
cat_merged_df = pd.merge(left=cat_number, right=category_installs, on='Category', how="inner")

scatter = px.scatter(data_frame=cat_merged_df,
                     x='App',
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
scatter.show()
```

The log scale is a smart choice because app-store data is extremely uneven. Without it, a few giant categories would dominate the plot.

The notebook also cleans multi-valued genres by splitting on semicolons and stacking the result:

```python
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
num_genres = stack.value_counts()
```

That is a useful normalization pattern. A single cell should not quietly contain multiple categories if you plan to count categories later.

Finally, the notebook compares free and paid apps by category:

```python
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
```

That grouped summary is a good example of how dashboard data is usually prepared: first build compact tables around one question, then feed those tables into the charting layer.

## How to Run the Play Store Analytics Notebook

1. Install the dependencies:
   ```bash
   pip install pandas plotly
   ```
2. Open `Google Play Store App Analytics.ipynb` from this folder.
3. Run the cleanup cells first so `df_apps_clean` is ready before any visualizations.
4. Check the main outputs:
   - donut chart for content ratings
   - horizontal bar chart for installs by category
   - scatter plot for category concentration

## Summary

Today, you learned that interactive charts are only as good as the table behind them. You cleaned a scraped marketplace dataset, removed duplicates, converted text-valued numbers into numeric columns, and used Plotly to build charts that support comparison rather than just decoration. The notebook is a good example of how data cleaning and chart choice should work together.
