# Day 74 - Aggregating and Merging Datasets with Pandas

Today, we stop treating a CSV like a self-contained world. The LEGO project spreads information across multiple files: colors, sets, and themes. That is much closer to how real business data is organized. If you want to answer useful questions, you need to summarize one table, join it to another, and keep your charts honest when the dataset includes incomplete years.

This lesson is really about three pandas moves that show up everywhere in data work: **groupby**, **agg**, and **merge**.

## 1. First Pass Data Exploration

The notebook starts small with `colors.csv`. That is a good choice because it lets you practice counting categories before you move into the more complex set history.

```python
colors = pd.read_csv("./data/colors.csv")
print(colors.groupby('is_trans').count())
# or
colors.is_trans.value_counts()
```

Both approaches answer the same question: how many transparent and opaque colors are in the dataset? The difference is in how they scale.

- `value_counts()` is fast when all you need is a frequency table.
- `groupby()` becomes more useful when the result will feed a larger summary later.

That distinction matters. In pandas, the first question is often simple, but the second question usually wants a grouped table you can keep building on.

## 2. Aggregating the LEGO Timeline

The main dataset is the set history. Once you read it in, the obvious business question is how LEGO's catalog changed over time.

```python
sets = pd.read_csv("./data/sets-1.csv")
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
```

This gives you a year-by-year count of sets. It is a basic aggregation, but it teaches an important pattern: a grouped DataFrame lets you collapse a long list of records into a time series you can reason about.

The notebook then asks a slightly harder question: how many **themes** existed each year? Counting rows is not enough any more. Now you need a custom aggregation on a specific column:

```python
themes_by_year = sets.groupby('year').agg({f'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
```

This is where `agg()` starts to matter. Real analysis rarely stops at row counts. You often need:

- unique counts with `nunique()`
- averages with `mean()`
- totals with `sum()`
- minimums and maximums

Changing the aggregation changes the question you are answering, even when the source table stays the same.

## 3. Visualizing Growth Without Lying With the Chart

Once you have yearly summaries, plotting them is easy. Plotting them honestly takes more care.

The set data includes very recent entries that do not represent complete years. If you graph every row, the chart suggests LEGO suddenly collapsed at the end of the series. That is not a business event. It is a partial-year artifact.

```python
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')
```

There are two lessons in that block:

1. Slicing off incomplete years is part of responsible analysis.
2. `twinx()` solves a real scaling problem when two series share time but not magnitude.

The notebook also measures how set complexity changed by averaging part counts per year:

```python
parts_per_set = sets.groupby('year').agg({f'num_parts': pd.Series.mean})
parts_per_set.head()
```

That is a useful shift in perspective. Earlier, the analysis measured catalog breadth. Here it measures typical set size. Same library, same grouping pattern, different business question.

## 4. Merging Tables to Recover Meaning

This is the part that makes the lesson title literal. If you count the most common `theme_id` values, you get numbers, not names. That summary is mathematically correct and practically useless until you join it to `themes.csv`.

```python
set_theme_count = sets["theme_id"].value_counts()
set_theme_count = pd.DataFrame({
    'id': set_theme_count.index,
    'set_count': set_theme_count.values,
})

merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df.head()
```

That merge works because the tables are relational:

- `themes.csv` stores the primary key `id`
- `sets.csv` stores `theme_id` as the foreign key

Once you understand that relationship, `merge()` stops feeling like a pandas trick and starts feeling like a database operation.

The merged result feeds the final chart:

```python
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
```

The chart looks simple because the hard work happened upstream. That is a recurring pattern in data science: if the final graph is clean, the shaping work before it was probably correct.

## How to Run the LEGO Analysis

1. Install the dependencies you need for the notebook:
   ```bash
   pip install pandas matplotlib
   ```
2. Open `Lego_Analysis.ipynb` from this folder in Jupyter or VS Code.
3. Run the notebook top to bottom so grouped tables such as `sets_by_year`, `themes_by_year`, and `merged_df` exist before the plotting cells.
4. Check the two main visual takeaways:
   - LEGO's catalog expands sharply in the modern era.
   - The most common theme ids only become readable after the merge with `themes.csv`.

## Summary

Today, you learned how analysts move between multiple related tables instead of one flat CSV. You used `groupby()` to build yearly summaries, `agg()` to change the meaning of those summaries, and `merge()` to reconnect ids to readable metadata. That combination is one of the core workflows in pandas, and you will keep using it long after this LEGO project is over.
