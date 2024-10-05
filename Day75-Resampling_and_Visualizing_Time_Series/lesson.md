# 1. Data Exploration - Making Sense of Google Search Data

I've gone ahead and already added the import statements and created the four different DataFrames in this notebook. 
Your first step is to explore the data, by getting an understanding of what's actually in those .csv files for this project.

Start with `df_tesla`, then have a look at `df_unemployment` and finally, check out the two bitcoin DataFrames.

### Challenge

Try to answer these questions about the DataFrames:
- What are the shapes of the DataFrames?
- How many rows & columns do they have?
- What are the column names?
- What is the largest number in the search data column? Try using the .describe() function.
- What is the periodicity of the time series data (daily, weekly, monthly)?

### Solution for Tesla

The `df_tesla` DataFrame has 124 rows and 3 columns: for the Month, the search popularity and the closing price of the Tesla stock.

```
print(df_tesla.shape)
df_tesla.head()
```

You can use the `max()` and `min()` functions to see that the largest value in the search column is 31 and the smallest value is 2.
```
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')

print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

Largest value for Tesla in Web Search: 31
Smallest value for Tesla in Web Search: 2
```

One of my favourite functions to run on DataFrames is `.describe()`. 
If you use `df_tesla.describe()`, you get a whole bunch of descriptive statistics. Right off the bat.

### Solution for Unemployment

The unemployment DataFrame has 181 rows and 3 columns. As with Tesla, we have monthly data from 2004 onwards, organized in rows. 
Interestingly here, the largest value in the search column is 100.

    print(f'Largest value for "Unemployment Benefits in Web Search": {df_unemployment['UE_BENEFITS_WEB_SEARCH'].max()}')

    Largest value for "Unemployment Benefits in Web Search": 100

### Solution for Bitcoin

With the Bitcoin data we see that we have two different .csv files. One of them has the day-by-day closing price and the trade volume of Bitcoin across 2204 rows. 
The other has the monthly search volume from Google Trends.

```
print(df_btc_price.shape)
df_btc_price.head()

print(df_btc_search.shape)
df_btc_search.head()

print(f'largest BTC News Search: {df_btc_search['BTC_NEWS_SEARCH'].max()}')
largest BTC News Search: 100
```

## What do the Search Numbers mean?

We can see from our DataFrames that Google's search interest ranges between 0 and 100. But what does that mean? 
Google defines the values of search interest as: 

    Numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term.

Basically, the actual search volume of a term is not publicly available. Google only offers a scaled number. 
Each data point is divided by the total searches of the geography and time range it represents to compare relative popularity.

For each word in your search, Google finds how much search volume in each region and time period your term had relative to all the searches in that region and time period. 
It then combines all of these measures into a single measure of popularity, and then it scales the values across your topics, so the largest measure is set to 100. 
In short: Google Trends doesn’t exactly tell you how many searches occurred for your topic, but it does give you a nice proxy.

Here are the Google Trends Search Parameters that I used to generate the .csv data:

"Tesla", Worldwide, Web Search

"Bitcoin", Worldwide, News Search

"Unemployment Benefits", United States, Web Search


# 2. Data Cleaning - Resampling Time Series Data

First, we have to identify if there are any missing or junk values in our DataFrames.

### Challenge

Can you investigate all 4 DataFrames and find if there are any missing values? 
If yes, find how many missing or NaN values there are. Then, find the row where the missing values occur.
Finally, remove any rows that contain missing values.

### Solution: Finding the missing values

For 3 of the DataFrames there are no missing values. We can verify this using the `.isna()` method. 
This will return a whole series of booleans, but we can chain `.values.any()` to see if any value in the series is `True`.
```
print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
```

Missing values for Tesla?: False
Missing values for U/E?: False
Missing values for BTC Search?: False

However, for the Bitcoin price data, there seems to be a problem. There's a missing value somewhere.

The number of missing values can be found by using `.sum()` to add up the number of occurrences of `True` in the series. This shows that there are 2 missing values.

To find the row where the missing values occur, we can create a subset of the DataFrame using `.isna()` once again (If you've arrived at this answer using a different approach, that's fine too. There are a number of ways to solve this challenge.)
```
print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')

Missing values for BTC price?: True

print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
df_btc_price[df_btc_price.CLOSE.isna()]
```
To remove a missing value we can use `.dropna()`. 
The `inplace` argument allows to overwrite our DataFrame and means we don't have to write:

    df_btc_price = df_btc_price.dropna()

    df_btc_price.dropna(inplace=True)

### Challenge

Our DataFrames contain time-series data. Do you remember how to check the data type of the entries in the DataFrame? 
Have a look at the data types of the MONTH or DATE columns. Convert any strings you find into Datetime objects. 
Do this for all 4 DataFrames. Double-check if your type conversion was successful.

```
type(df_tesla.MONTH[0])
str

df_tesla.MONTH = pd.to_datetime(df_tesla['MONTH'])
type(df_tesla.MONTH[0])
pandas._libs.tslibs.timestamps.Timestamp
```

```
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

df_btc_price.DATE.head()
```
    0   2014-09-17
    1   2014-09-18
    2   2014-09-19
    3   2014-09-20
    4   2014-09-21
    Name: DATE, dtype: datetime64[ns]

## Resampling Time Series Data

Next, we have to think about how to make our Bitcoin price and our Bitcoin search volume comparable. 
Our Bitcoin price is daily data, but our Bitcoin Search Popularity is monthly data.

To convert our daily data into monthly data, we're going to use the `.resample()` function. The only things we need to specify is which column to use (i.e., our `DATE` column) and what kind of sample frequency we want (i.e., the "rule"). 
We want a monthly frequency, so we use `'M'`.  If you ever need to resample a time series to a different frequency, you can find a list of different options here (for example `'Y'` for yearly or `'T'` for minute).

After resampling, we need to figure out how the data should be treated. In our case, we want the last available price of the month - the price at month-end.

```
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

/var/folders/3q/zg5b2vcj50nc6cwf_t1v64wm0000gn/T/ipykernel_12347/1045968048.py:1: FutureWarning: 'M' is deprecated and will be removed in a future version, please use 'ME' instead.
```
If we wanted the average price over the course of the month, we could use something like:

    df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()
This is what our data looks like now:
```
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(df_btc_monthly. shape)
df_btc_monthly.head()
```

# 3. Data Visualisation - Tesla Line Charts in Matplotlib

Let's create a basic line chart of the Tesla stock price and the search popularity and then gradually add more and more styling to our chart.

### Challenge
Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes. Here's what you're aiming for:

```
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
ax1.set_ylabel('TSLA Stock Price')
ax2.set_ylabel('Search Trend')
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)
```

### Challenge
Now let's style the chart a bit more. In particular, let's check out the different colours you can use with Matplotlib.

For our updated chart, let's differentiate the two lines and the axis labels using different colours. Try using one of the blue colour names for the search volume and a HEX code for a red colour for the stock price. Here's what you're aiming for:

Hint: you can colour both the axis labels and the lines on the chart using keyword arguments (`kwargs`).

```
ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()
ax1.set_ylabel('TSLA Stock Price', color='deepskyblue')
ax2.set_ylabel('Search Trend', color='#E63610')
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='deepskyblue')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='#E63610')
```

### Challenge
There are still some ways to improve the look of this chart. First off, let's make it larger. 
- Can you make the following changes:
- Increase the figure size (e.g., to 14 by 8).
- Increase the font sizes for the labels and the ticks on the x-axis to 14.
- Rotate the text on the x-axis by 45 degrees.
- Add a title that reads 'Tesla Web Search vs Price'
- Make the lines on the chart thicker.
- Keep the chart looking sharp by changing the dots-per-inch or DPI value.
- Set minimum and maximum values for the y and x-axis. Hint: check out methods like set_xlim().
- Finally use plt.show() to display the chart below the cell instead of relying on the automatic notebook output.


### Solution: Additional styling, increasing size & resolution

There's a couple of tweaks to the code going on here. First, we use `.figure()` to increase the size and resolution of our chart. 
Since we now have a bigger chart, we should also increase the font size of our labels and the thickness of our lines.

Finally, we are calling `.show()` to explicitly display the chart below the cell. This `.show()` method is important to be aware of if you're ever trying to generate charts in PyCharm or elsewhere outside of an interactive notebook like Google Colab or Jupyter. Also, it gives our notebook a very clean look.
```
# increases size and resolution
plt.figure(figsize=(14,8), dpi=220) 
plt.title('Tesla Web Search vs Price', fontsize=18)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
 
# Displays chart explicitly
plt.show()
```

Here's the code with rotation added to the x-ticks. With `.set_ylim()` and `.set_xlim()` you have precise control over which data you want to show on the chart. 
You can either choose hard values like displaying the Tesla stock price between $0 and $600. 
Or you could use the `.min()` and `.max()` functions to help you work out the bounds for the chart as well.

```
plt.figure(figsize=(14,8), dpi=320)
plt.title('Tesla Web Search vs Price', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
 
plt.show()
```

## Using Locators and DateFormatters to generate Tick Marks on a Time Line

### Adding Locator Tick Marks

When working with time series, it's often quite difficult to get the tick marks on charts looking the way you want to. This is why we have `Locator` helpers.
Using `Locators` we can change our x-axis from looking like this:

The first step is importing `matplotlib.dates`.  This is where all the date plotting capabilities live.

Next, we need a `YearLocator()` and a `MonthLocator()` objects, which will help Matplotlib find the years and the months. 
Then we also need a `DateFormatter()`, which will help us specify how we want to display the dates. 

```
# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
```

Now we can go back to our chart and format where the major and minor ticks should be using the Locators.
```
plt.figure(figsize=(14,8), dpi=320)
plt.title('Tesla Web Search vs Price', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# Format ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
 
plt.show()
```

When we take a look at our chart, we can see the tick marks nicely. The tick marks also allow us to visually date that spike of interest in the middle of the chart - March 2016. This was when the Tesla Model 3 was unveiled. Also, we can clearly see that the most recent spikes in search coincide, not with the release of a new car, but the roaring stock price for the company!


# 4. Data Visualisation - Bitcoin: Line Style and Markers

Now that we've got Tesla looking the way we want it to, let's do the same for Bitcoin. 
We've already matched the sample frequency and we can re-use our chart! Simply copy-paste the entire cell and make some modifications to the code as per the challenge.

### Challenge

- Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
- Change the y-axis label to 'BTC Price'
- Change the y- and x-axis limits to improve the appearance
- Investigate the linestyles to make the BTC closing price a dashed line
- Investigate the marker types to make the search datapoints little circles
- Were big increases in searches for Bitcoin accompanied by big increases in the price?

```
plt.figure(figsize=(14,8), dpi=220)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('BTC Price', color='orange', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 20000])
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

# Format ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='orange', linewidth=2, linestyle='dashed')
ax2.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH, color='skyblue', linewidth=2, marker='o')
 
plt.show()
```

What we see in the chart is that similar to Tesla, the crazy price movements in the beginning of 2018 are associated with very high search volumes. 
Everyone was talking about (and buying) Bitcoin in late 2017/early 2018 so search volumes were at a record high!  
Interestingly, there was quite a huge spike in bitcoin prices in Q1 of 2019, but this time the increase in search volume was much less pronounced (perhaps because at this point everyone knew what Bitcoin was).



# 5. Data Visualisation - Unemployment: How to use Grids

For the next challenge, carry over your existing code once again (by copy-pasting the entire cell) and make some modifications.

### Challenge

- Plot the search for "unemployment benefits" against the official unemployment rate.
- Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate
- Change the y-axis label to: FRED U/E Rate
- Change the axis limits
- Add a grey grid to the chart to better see the years and the U/E rate values. Use dashed lines for the line style.

Can you discern any seasonality in the searches? Is there a pattern?

### Solution: Adding a grid to spot seasonality

Ok, so there are relatively few changes you had to make here. Just the labels and the dataset we're using. 
The line of code I wanted you to figure out from the documentation was this one:

    ax1.grid(color='grey', linestyle='--')

Notice how we can now clearly see the vertical dashed lines line up with spikes in searches for "Unemployment benefits". 
Many of the spikes are at year-end - in December. This clearly shows that there is seasonality in the job market. 
What else do we see? We see that the financial crisis in 2007/2008 caused a massive spike in unemployment. It took around 10 years (2007-2017) for the unemployment to reach the same level it had before the crisis.

```
plt.figure(figsize=(14,8), dpi=220)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([3, 10.5])
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

# Format ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='purple', linestyle='dashed', linewidth=3)
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
ax1.grid(color='grey', linestyle='--')
plt.show()
```

Interestingly the big spike in searches for Unemployment benefits at the end of 2013 was not accompanied by a big increase in the unemployment rate. 
Something else must have been going on around that time.


### Challenge

Calculate the 3-month or 6-month rolling average for the web searches. Plot the 6-month rolling average search data against the actual unemployment. 
What do you see? Which line moves first?

Hint: Take a look at our prior lesson on Programming Languages where we smoothed out time-series data.

```
plt.figure(figsize=(14,8), dpi=220)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([3, 10.5])
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

# Format ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# Calculate the rolling average over a 6 month window
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
 
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='purple', linestyle='dashed', linewidth=3)
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
ax1.grid(color='grey', linestyle='--')
plt.show()
```

What is this telling us? We see that searches for "Unemployment Benefits" happen before the actual official unemployment rate goes up. 
Similarly, the search popularity for the term goes down before the unemployment rate decreases. 
In other words, these searches seem to act as a leading economic indicator for the unemployment rate (which is a lagging indicator).


# 6. Data Visualisation - Unemployment: The Effect of New Data

The financial crisis in 2008 was pretty bad. We saw how it took around 10 years for the unemployment rate to go back to where it was prior to the crisis.

Let's see how 2020 affects our analysis.

### Challenge
Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame. 
Convert the MONTH column to Pandas Datetime objects and then plot the chart. What do you see?

```
df_unemployment_2020 = pd.read_csv("./UE Benefits Search vs UE Rate 2004-20.csv")
df_unemployment_2020.tail()

df_unemployment_2020.MONTH = pd.to_datetime(df_unemployment_2020.MONTH)
```

```
plt.figure(figsize=(14,8), dpi=220)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([3, 15])
ax1.set_xlim([df_unemployment_2020.MONTH.min(), df_unemployment_2020.MONTH.max()])

# Format ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.plot(df_unemployment_2020.MONTH, df_unemployment_2020.UNRATE, color='purple', linestyle='dashed', linewidth=3)
ax2.plot(df_unemployment_2020.MONTH, df_unemployment_2020.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
ax1.grid(color='grey', linestyle='--')
plt.show()
```

What we see is not pretty. The US unemployment rate spiked to unprecedented levels during the COVID pandemic, dwarfing the levels seen during the financial crisis. 
Let's hope the recovery will be swifter this time.


# 7. Learning Points & Summary

In this lesson we looked at how to:
- How to use `.describe()` to quickly see some descriptive statistics at a glance.
- How to use `.resample()` to make a time-series data comparable to another by changing the periodicity.
- How to work with `matplotlib.dates` **Locators** to better style a timeline (e.g., an axis on a chart).
- How to find the number of `NaN` values with `.isna().values.sum()`
- How to change the **resolution** of a chart using the `figure`'s `dpi`
- How to create dashed `'--'` and dotted `'-.'` lines using `linestyles`
- How to use different kinds of `markers` (e.g., `'o'` or `'^'`) on charts.
- Fine-tuning the **styling** of Matplotlib charts by using `limits`, `labels`, `linewidth` and `colors` (both in the form of `named` colours and `HEX` codes).
- Using `.grid()` to help visually identify seasonality in a time series.
