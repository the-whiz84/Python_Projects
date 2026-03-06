# Day 99 - Space Mission Data Analysis and Insight Generation

This notebook is a broad exploratory analysis of global launch history. It mixes country normalization, cost analysis, mission outcomes, organizational comparisons, long-term launch trends, and geopolitical comparisons such as USA versus USSR. That makes it less like a single-question notebook and more like a full exploratory data project.

The challenge here is not only plotting. It is organizing a messy historical dataset into useful views.

## 1. Clean and Normalize the Launch Dataset

The notebook starts with the mission file and trims obvious noise:

```python
df_data = pd.read_csv("mission_launches_Feb2024.csv")
df_data.drop(columns=["Unnamed: 0"], inplace=True)
```

Then it derives a launch-country column from the location text:

```python
df_data["launch_country"] = df_data["Location"].str.split(", ").str[-1]
```

This is followed by a cleanup pass for outdated or ambiguous country names:

```python
df_data["launch_country"] = df_data["launch_country"].replace(
    {
        "Yellow Sea": "China",
        "Russia": "Russian Federation",
        "Pacific Ocean": "USA",
        "Marshall Islands": "USA",
        "North Korea": "Korea, Democratic People's Republic of",
        "South Korea": "Korea, Republic of",
    }
)
```

That normalization work is essential. Without it, geographic grouping would split one real country into multiple inconsistent labels.

The notebook then uses `iso3166` to derive alpha-3 codes:

```python
df_data["launch_country_code"] = df_data["launch_country"].apply(
    lambda x: (countries.get(x).alpha3)
)
```

That is what makes the later choropleth maps possible.

## 2. Explore Launch Volume, Failure, and Cost

Once the data is normalized, the notebook builds a country-level launch table:

```python
df_launches = df_data.groupby(
    ["launch_country", "launch_country_code"], as_index=False
).agg({"Mission_status": pd.Series.count})
df_launches.rename(columns={"Mission_status": "Total_launches"}, inplace=True)
```

And maps it:

```python
px.choropleth(
    data_frame=df_launches,
    locations="launch_country_code",
    color="Total_launches",
    color_continuous_scale="matter",
)
```

It performs the same kind of aggregation for failures:

```python
df_failures = df_data[df_data["Mission_status"] == "Failure"]
df_failures = df_failures.groupby(
    ["launch_country", "launch_country_code"], as_index=False
).agg({"Mission_status": pd.Series.count})
```

The notebook also analyzes launch cost using the `Price` column:

```python
sns.histplot(df_data["Price"].dropna(), bins=30, kde=True)
plt.title("Distribution of Launch Prices (in USD millions)")
```

And compares organizations by total and average launch cost:

```python
total_spent_by_org = df_data.groupby("Organisation")["Price"].sum().reset_index()
avg_spent_per_launch = df_data.groupby("Organisation")["Price"].mean().reset_index()
```

That gives the notebook both operational and financial angles on the same dataset.

## 3. Turn Datetime Data Into Launch Trends

The notebook converts mission timestamps into a proper timeline:

```python
df_data["Datetime"] = pd.to_datetime(df_data["Datetime"], utc=True)
df_data["Year"] = df_data["Datetime"].dt.year
```

From there it can calculate yearly and monthly launch totals:

```python
launches_per_year = (
    df_data.groupby("Year").size().reset_index(name="Number of Launches")
)
```

and:

```python
df_data["YearMonth"] = df_data["Datetime"].dt.to_period("M")
launches_per_month = (
    df_data.groupby("YearMonth").size().reset_index(name="Number of Launches")
)
launches_per_month["Rolling Average"] = (
    launches_per_month["Number of Launches"].rolling(window=12).mean()
)
```

The 12-month rolling average is especially useful because monthly launch counts are noisy. Smoothing exposes the long-term trend much more clearly.

## 4. Compare Superpowers, Organizations, and Leadership Over Time

One of the strongest sections in the notebook is the Cold War comparison. It groups launches by year and by launch country, then combines Russian Federation and Kazakhstan into the USSR bucket where appropriate.

```python
df_cold_war = df_data[df_data["Year"] <= 1991]
df_cold_war = df_cold_war[
    df_cold_war["launch_country"].isin(["USA", "Russian Federation", "Kazakhstan"])
]
```

The notebook uses similar grouped tables to compare:

- top organizations over time
- leading country by total launches each year
- leading country by successful launches each year
- overall USA vs USSR launch counts

Those views make the notebook feel historical rather than purely descriptive.

The sunburst chart also adds a layered organizational perspective:

```python
fig = px.sunburst(df_data, path=["launch_country", "Organisation", "Mission_status"])
fig.show()
```

That chart works well because it shows hierarchy instead of only totals.

## How to Run the Space Missions Notebook

1. Install the dependencies used by the notebook:
   ```bash
   pip install iso3166 pandas numpy matplotlib seaborn plotly
   ```
2. Open `Space_Missions_Analysis.ipynb`.
3. Run the notebook in order so the normalized country columns, datetime features, and grouped summary tables are available before the charts.
4. Verify the major outputs:
   - launch and failure choropleths
   - cost distributions and organization comparisons
   - yearly and rolling monthly launch trends
   - USA vs USSR comparisons

## Summary

Today, you worked through a large exploratory analysis rather than a single-model notebook. The project cleaned geographic labels, derived time features, compared launch volume and failure by country, analyzed cost by organization, and turned the mission history into both business and geopolitical narratives. The main lesson is how much value comes from shaping one dataset into several different analytical views.
