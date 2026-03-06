# Day 100 - Capstone Data Analysis: Police Deaths in the USA

Day 100 is a capstone because it asks you to combine several public datasets into one social analysis. The notebook does not work with a single table. It brings together police fatalities, poverty rates, household income, graduation rates, and racial composition by city and state. That makes the challenge less about one chart and more about integrating multiple sources responsibly.

This is a sensitive subject, so the analysis also needs more care than a typical toy dataset.

## 1. Load and Clean Several Public Datasets Together

The notebook begins by loading five separate CSV files:

```python
df_hh_income = pd.read_csv("Median_Household_Income_2015.csv", encoding="windows-1252")
df_pct_poverty = pd.read_csv(
    "Pct_People_Below_Poverty_Level.csv", encoding="windows-1252"
)
df_pct_completed_hs = pd.read_csv(
    "Pct_Over_25_Completed_High_School.csv", encoding="windows-1252"
)
df_share_race_city = pd.read_csv("Share_of_Race_By_City.csv", encoding="windows-1252")
df_fatalities = pd.read_csv("Deaths_by_Police_US.csv", encoding="windows-1252")
```

The notebook then checks shape, schema, and duplicates before filling missing values:

```python
df_hh_income.fillna(0, inplace=True)
df_pct_poverty.fillna(0, inplace=True)
df_pct_completed_hs.fillna(0, inplace=True)
df_share_race_city.fillna(0, inplace=True)
df_fatalities.fillna(0, inplace=True)
```

That early cleanup is important because later grouped summaries will fail or mislead if key percentage columns still contain strings or nulls.

## 2. Compare Poverty and Education by State

One of the first analysis paths converts state-level poverty rates into numeric form:

```python
df_pct_poverty["poverty_rate"] = pd.to_numeric(
    df_pct_poverty["poverty_rate"], errors="coerce"
)

state_poverty_rate = (
    df_pct_poverty.groupby("Geographic Area")["poverty_rate"].mean().reset_index()
)
```

The notebook does something similar for high school completion:

```python
df_pct_completed_hs["percent_completed_hs"] = pd.to_numeric(
    df_pct_completed_hs["percent_completed_hs"], errors="coerce"
)

state_hs_grad_rate = (
    df_pct_completed_hs.groupby("Geographic Area")["percent_completed_hs"]
    .mean()
    .reset_index()
)
```

Those two summaries are then compared with both Plotly and Matplotlib. The subplot approach is especially useful because it puts two state-level trends into one coordinated figure:

```python
fig = make_subplots(specs=[[{"secondary_y": True}]])
```

This is a good example of when multiple visualization libraries can coexist in one notebook. Plotly gives interactive state comparisons, while Matplotlib gives more direct control over the paired-axis version.

## 3. Analyze Fatalities by Race, Age, and Weapon Status

The fatalities table is then used for demographic analysis. For example, race counts become a donut chart:

```python
race_counts = df_fatalities["race"].value_counts()

fig = px.pie(
    names=race_counts.index,
    values=race_counts.values,
    title="People Killed by Race",
    hole=0.4,
)
```

The notebook also examines whether the deceased were armed:

```python
armed_counts = df_fatalities["armed"].value_counts(normalize=True) * 100
```

and builds a simplified "gun vs unarmed vs other" comparison:

```python
gun_vs_unarmed_counts = (
    df_fatalities["armed"]
    .astype(str)
    .apply(lambda x: "gun" if "gun" in x else "unarmed" if x == "unarmed" else "other")
    .value_counts()
)
```

This kind of recoding is important. Raw categories are often too fragmented to interpret directly, so the notebook groups them into analysis-ready buckets.

The age analysis uses Seaborn:

```python
g = sns.FacetGrid(df_fatalities, hue="race", height=5, aspect=2)
g.map(sns.kdeplot, "age", fill=True).add_legend()
```

That lets the notebook compare age distributions across racial groups rather than only total counts.

## 4. Compare Fatalities to Local Demographics

The most ambitious part of the notebook is the city-level comparison between fatalities and racial composition.

First, the race-share columns are converted to numeric:

```python
df_share_race_city['share_white'] = pd.to_numeric(df_share_race_city['share_white'], errors='coerce')
df_share_race_city['share_black'] = pd.to_numeric(df_share_race_city['share_black'], errors='coerce')
df_share_race_city['share_native_american'] = pd.to_numeric(df_share_race_city['share_native_american'], errors='coerce')
df_share_race_city['share_asian'] = pd.to_numeric(df_share_race_city['share_asian'], errors='coerce')
df_share_race_city['share_hispanic'] = pd.to_numeric(df_share_race_city['share_hispanic'], errors='coerce')
```

Then the notebook groups by geography and merges those shares with fatality counts in the top cities.

This is where the notebook becomes a real capstone. It is no longer only summarizing one dataset. It is combining datasets to ask harder contextual questions about representation, inequality, and geographic variation.

Because the subject is serious, the lesson here is also methodological: data integration can reveal patterns, but it does not automatically explain causality. The notebook is best used as an exploratory tool, not as proof of a complete social theory.

## How to Run the Capstone Notebook

1. Install the analysis stack:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```
2. Open `Fatal_Force.ipynb`.
3. Run the notebook in order so the cleaned numeric columns and grouped summary tables exist before the later charts and comparisons.
4. Verify the major outputs:
   - poverty and graduation summaries by state
   - race and armed-status charts from the fatalities table
   - age distribution comparison by race
   - city/state demographic comparison tables

## Summary

Today, you finished with a true capstone analysis. The notebook integrates multiple public datasets, cleans them into comparable forms, and uses grouped summaries plus visualizations to examine poverty, education, race, and fatal police encounters together. The main lesson is not only technical. It is that complex public problems require careful data preparation, cautious interpretation, and respect for the limits of the data.
