# Day 75 - Resampling and Visualizing Time Series

Today, the problem is not "how do I plot this data?" It is "how do I make these timelines comparable in the first place?" Tesla search traffic is monthly. Bitcoin prices are daily. Bitcoin search interest is monthly. Unemployment data is monthly again. If the frequencies and date types do not line up, the chart can look polished while saying nothing useful.

This lesson is about **time-series integrity**: clean dates, matching intervals, and charts that reflect the actual rhythm of the data.

## 1. Inspect the Time-Series Sources

The notebook begins by loading four different datasets:

```python
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
```

This first pass matters because time-series datasets differ in two ways:

- what they measure
- how often they measure it

Google Trends values are also worth reading carefully. They are not raw search counts. They are normalized popularity scores from `0` to `100`, where `100` means the peak popularity inside that query range.

That makes the series useful for relative comparison, but it also means you should read it as **attention**, not as literal volume.

## 2. Clean Missing Values and Convert Dates

Before any resampling happens, the notebook checks for missing values and finds that the Bitcoin price table needs cleanup.

```python
df_btc_price.dropna(inplace=True)
```

Missing values are especially dangerous in time-series work because they can distort:

- resampled summaries
- rolling averages
- line charts that imply continuity

Once the null handling is done, the notebook converts the date columns into real datetime objects:

```python
df_tesla.MONTH = pd.to_datetime(df_tesla['MONTH'])
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
```

This step is essential. If pandas still sees the time column as text, resampling and date-aware plotting will not behave correctly. Datetime conversion is what turns a string column into a real timeline.

## 3. Resample Data to a Comparable Frequency

The Bitcoin price data arrives daily, but the search-interest series is monthly. To compare them, the notebook downsamples the price data to month-end values.

```python
df_btc_monthly = df_btc_price.resample('ME', on='DATE').last()
```

There are two decisions hidden inside that one line:

- `ME` means month-end frequency
- `.last()` means "use the final observed price in each month"

That is a defensible choice because the comparison is between monthly search interest and a monthly closing snapshot of the market. If the question were different, you might choose `.mean()` instead and compare against an average monthly price.

The key idea is that **resampling is analytical**, not cosmetic. You are deciding how raw observations become a new time series.

## 4. Build Time-Series Charts That People Can Read

The Tesla section introduces the chart pattern used throughout the notebook: two y-axes, one shared time axis, and deliberate formatting for dates.

```python
plt.figure(figsize=(14,8), dpi=320)
plt.title('Tesla Web Search vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
plt.show()
```

The notebook improves the x-axis even further with `matplotlib.dates`:

```python
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
```

That formatting work is not decoration. It keeps the chart readable over long periods.

The same pattern is then reused for Bitcoin:

```python
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
         color='orange', linewidth=2, linestyle='dashed')
ax2.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH,
         color='skyblue', linewidth=2, marker='o')
```

Reuse is a good sign here. Once you solve the figure architecture for one timeline comparison, you should keep that structure and swap in new datasets.

## 5. Use Rolling Averages to Expose the Trend

The unemployment section is the most analytical part of the notebook because it does more than compare two lines. It asks whether search interest can move ahead of the official unemployment rate.

First, the notebook overlays the two series:

```python
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE,
         color='purple', linestyle='dashed', linewidth=3)
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)
ax1.grid(color='grey', linestyle='--')
```

Then it smooths the data with a 6-month rolling average:

```python
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)
```

That smoothing removes month-to-month noise and makes the broader direction easier to see. The result is a more interesting economic reading: searches for unemployment benefits often move before the official unemployment rate catches up.

The notebook closes by loading the `2004-20` unemployment file, which shows how a new slice of time can completely change the scale of the chart once the pandemic shock appears.

## How to Run the Time-Series Notebook

1. Install the required libraries:
   ```bash
   pip install pandas matplotlib
   ```
2. Open `Google Trends and Data Visualisation.ipynb` from this folder.
3. Run the cells in order so the cleaned datetime columns and `df_btc_monthly` exist before the chart cells.
4. Verify the three key outcomes:
   - Tesla search and price can be compared on dual axes.
   - Bitcoin prices must be resampled before comparison with search interest.
   - Rolling averages make the unemployment trend easier to interpret.

## Summary

Today, you learned that time-series analysis starts before the plot. You cleaned missing values, converted strings into datetimes, resampled daily data into monthly data, and used rolling averages to make noisy series readable. Once the timeline is trustworthy, Matplotlib becomes much more useful because the chart is finally showing comparable data.
