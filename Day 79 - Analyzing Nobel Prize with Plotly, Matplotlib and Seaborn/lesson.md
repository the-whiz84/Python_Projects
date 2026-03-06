# Day 79 - Multi-Library EDA: Plotly, Matplotlib, and Seaborn

Today, we put several data skills together in one notebook: cleanup, feature engineering, grouped summaries, and chart selection across multiple libraries. The Nobel Prize dataset is a good capstone because it mixes people and organizations, countries and institutions, historical timelines, and demographic fields that are incomplete for reasons that actually matter.

This lesson is less about one library and more about choosing the right tool for each question.

## 1. Clean the Nobel Prize Dataset Carefully

The notebook begins with the usual inspection:

```python
df_data = pd.read_csv('nobel_prize_data.csv')

df_data.shape
df_data.head()
df_data.info()
df_data.duplicated().values.any()
df_data.isna().values.any()
```

The missing values are the first real clue about the data. Many of them appear because some winners are organizations rather than individuals. That means missing `birth_date` or `sex` values are not always "bad data." Sometimes they are telling you that the row represents a different kind of laureate.

The notebook then converts `birth_date` into a datetime column:

```python
df_data.birth_date = pd.to_datetime(df_data.birth_date)
```

And it engineers a numeric share column from the fractional `prize_share` strings:

```python
separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denominator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denominator
```

This is a classic feature-engineering step. The raw data already contains the information, but not in a form that is convenient for aggregation.

## 2. Use Plotly for High-Level Category and Geography Questions

Plotly is the right tool for interactive overview charts. The notebook uses it first to count prizes by category:

```python
prizes_per_category = df_data.category.value_counts()

v_bar = px.bar(
    x=prizes_per_category.index,
    y=prizes_per_category.values,
    color=prizes_per_category.values,
    color_continuous_scale='Aggrnyl',
    title='Number of Prizes Awarded per Category')

v_bar.update_layout(xaxis_title='Nobel Prize Category',
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
v_bar.show()
```

That grouped count gives a clean answer to a broad question: where does most of the Nobel Prize volume sit?

The notebook also groups by country and ISO code so it can build a choropleth:

```python
top20_countries = df_data.groupby(['birth_country_current', 'ISO'], as_index=False).agg({'prize': pd.Series.count})
top20_countries.sort_values(by='prize', ascending=True, inplace=True)

fig = px.choropleth(top20_countries,
                    locations="ISO",
                    color=top20_countries.prize,
                    hover_name="birth_country_current",
                    color_continuous_scale=px.colors.sequential.matter)
fig.show()
```

That chart only works because the data was grouped around a real geographic key. The `ISO` column is what makes the map reliable.

## 3. Use Matplotlib for Long Historical Trends

For the time-based charts, Matplotlib gives the notebook tighter control.

First, it groups prizes by year and computes a moving average:

```python
prize_per_year = df_data.groupby(by='year').count().prize
moving_average = prize_per_year.rolling(window=5).mean()

yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()
```

Then it combines those series in a dual-axis chart:

```python
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100)

ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3)

ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3)
```

This is a good example of why one library does not have to do everything. Plotly handled the exploratory category work. Matplotlib handles the historical chart where axis control and layered styling matter more.

The notebook also computes cumulative country totals over time:

```python
prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]

cumulative_prizes = prize_by_year.groupby(by=['birth_country_current', 'year']).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True)
```

That is a useful chained-grouping pattern when you want to turn yearly counts into a growth story.

## 4. Use Seaborn for Statistical Comparisons

The age analysis is where Seaborn becomes the best fit. The notebook creates a winning-age feature:

```python
birth_years = pd.to_datetime(df_data.birth_date).dt.year
df_data['winning_age'] = df_data.year - birth_years
```

Then it looks at the distribution:

```python
plt.figure(figsize=(8, 4), dpi=200)
sns.histplot(data=df_data, x=df_data.winning_age, bins=30)
plt.xlabel('Age')
plt.title('Distribution of Age on Receipt of Prize')
plt.show()
```

And finally it uses regression-style Seaborn plots to see how age changes over time:

```python
with sns.axes_style("whitegrid"):
    sns.regplot(data=df_data,
                x='year',
                y='winning_age',
                lowess=True,
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})
```

The notebook then goes one step further with category-level comparisons:

```python
with sns.axes_style('whitegrid'):
    sns.lmplot(data=df_data,
               x='year',
               y='winning_age',
               row='category',
               lowess=True,
               aspect=2,
               scatter_kws={'alpha': 0.6},
               line_kws={'color': 'black'})
```

That is exactly where Seaborn shines. It makes it easy to compare the same statistical pattern across multiple subgroups without building every subplot by hand.

## How to Run the Nobel Prize Analysis Notebook

1. Install the dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```
2. Open `Nobel_Prize_Analysis.ipynb` from this folder.
3. Run the notebook from top to bottom so engineered columns such as `share_pct` and `winning_age` exist before the later charts.
4. Check the major outputs:
   - category bar chart
   - country choropleth
   - yearly prize trend chart
   - age trend plots with Seaborn

## Summary

Today, you learned that exploratory analysis is a chain of decisions, not a single chart. You cleaned the Nobel dataset, engineered features from raw strings and dates, grouped data by category, country, and year, and used Plotly, Matplotlib, and Seaborn where each one fit best. The real skill is not knowing three libraries. It is knowing which one helps answer the question in front of you.
