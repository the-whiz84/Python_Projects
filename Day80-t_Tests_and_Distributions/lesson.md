# t-Tests and Distributions


### Your Story

Today you will become a doctor, but not just any doctor. You will become Dr Ignaz Semmelweis, a Hungarian physician born in 1818 who worked in the Vienna General Hospital.

In the past, people didn't know about bacteria, germs, or viruses. People illness was caused by "bad air" or evil spirits. But in the 1800s Doctors started looking more at anatomy, doing autopsies and making arguments based on data. Dr Semmelweis suspected that something was going wrong with the procedures at Vienna General Hospital. Dr Semmelweis wanted to figure out why so many women in maternity wards were dying from childbed fever (i.e., puerperal fever).


### Today you'll learn:

- How to make a compelling argument using data
- How to superimpose histograms to show differences in distributions
- How to use a Kernel Density Estimate (KDE) to show a graphic estimate of a distribution.
- How to use **scipy** and test for statistical significance by looking at `p-values`.
- How to highlight different parts of a time series chart in **Matplotib**.
- How to add and configure a Legend in Matplotlib.
- Use NumPy's `.where()` function to process elements depending on a condition.


## 1, Preliminary Data Exploration and Visualising Births & Deaths at Vienna Hospital

You (aka Dr Semmelweis) are working at Vienna General Hospital. Let's take a closer look at the data you've been collecting on the number of births and maternal deaths throughout the 1840s.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_10-38-09-9527e9a9d46107327b4fa76246c62b81.png'>

### Challenge 1: Preliminary Data Exploration

- What is the shape of df_yearly and df_monthly? How many rows and columns?
- What are the column names?
- Which years are included in the dataset?
- Are there any NaN values or duplicates?
- What were the average number of births that took place per month?
- What were the average number of deaths that took place per month?

```
print(df_monthly.info())
print(df_monthly.describe())
print(df_monthly)
print(df_yearly)

    <class 'pandas.core.frame.DataFrame'>
RangeIndex: 98 entries, 0 to 97
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   date    98 non-null     datetime64[ns]
 1   births  98 non-null     int64         
 2   deaths  98 non-null     int64         
dtypes: datetime64[ns](1), int64(2)
memory usage: 2.4 KB
None
                                date  births  deaths
count                             98   98.00   98.00
mean   1845-02-11 04:24:29.387755008  267.00   22.47
min              1841-01-01 00:00:00  190.00    0.00
25%              1843-02-08 00:00:00  242.50    8.00
50%              1845-02-15 00:00:00  264.00   16.50
75%              1847-02-22 00:00:00  292.75   36.75
max              1849-03-01 00:00:00  406.00   75.00
std                              NaN   41.77   18.14
         date  births  deaths
0  1841-01-01     254      37
1  1841-02-01     239      18
2  1841-03-01     277      12
3  1841-04-01     255       4
4  1841-05-01     255       2
..        ...     ...     ...
93 1848-11-01     310       9
94 1848-12-01     373       5
95 1849-01-01     403       9
96 1849-02-01     389      12
97 1849-03-01     406      20

[98 rows x 3 columns]
    year  births  deaths    clinic
0   1841    3036     237  clinic 1
1   1842    3287     518  clinic 1
2   1843    3060     274  clinic 1
3   1844    3157     260  clinic 1
4   1845    3492     241  clinic 1
5   1846    4010     459  clinic 1
6   1841    2442      86  clinic 2
7   1842    2659     202  clinic 2
8   1843    2739     164  clinic 2
9   1844    2956      68  clinic 2
10  1845    3241      66  clinic 2
11  1846    3754     105  clinic 2

print(df_monthly.isna().values.any())
print(df_monthly.duplicated().values.any())
False
False

print(df_yearly.isna().values.any())
print(df_yearly.duplicated().values.any())
False
False

```

Using `.shape`, `.head()`, `.tail()` we see that the dataset covers the years 1841 to 1849. The two tables report the total number of births and the total number of deaths. Interestingly, the yearly data breaks the number of births and deaths down by clinic.

We see that there are no `NaN` values in either of the DataFrames. We can verify this either with using `.info()` or using `.isna().values.any()`.

There are also no duplicate entries. In other words, the dataset appears to be clean.

Using `.describe()` allows us to view some interesting statistics at a glance. We see that on average there were about 267 births and 22.47 deaths per month.


### Challenge 2: Percentage of Women Dying in Childbirth

- How dangerous was childbirth in the 1840s in Vienna?
- Using the annual data, calculate the percentage of women giving birth who died throughout the 1840s at the hospital.
- In comparison, the United States recorded 18.5 maternal deaths per 100,000 or 0.018% in 2013 (<a href='https://en.wikipedia.org/wiki/Maternal_death#:~:text=The%20US%20has%20the%20%22highest,17.8%20per%20100%2C000%20in%202009'>source</a>).


    death_perc = df_yearly.deaths / df_yearly.births * 100
    death_perc

    0     7.81
    1    15.76
    2     8.95
    3     8.24
    4     6.90
    5    11.45
    6     3.52
    7     7.60
    8     5.99
    9     2.30
    10    2.04
    11    2.80
    dtype: float64

Childbirth was very risky! About 7.08% of women died 💀 in the 1840s (compared to 0.018% in the US in 2013).

    prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
    print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')

If someone gave me a bag of 100 M&Ms and told me that 7 of them would kill me, I'd (probably) pass on those M&Ms 🤭. Just saying.


### Challenge 3: Visualize the Total Number of Births 🤱 and Deaths 💀 over Time

Create a Matplotlib chart with twin y-axes. It should look something like this:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_11-06-31-76e4e6fbe90cd4edb47e9dee6eb3da5f.png'>

- Format the x-axis using locators for the years and months (*Hint*: we did this in the Google Trends notebook)
- Set the range on the x-axis so that the chart lines touch the y-axes
- Add gridlines
- Use `skyblue` and `crimson` for the line colors
- Use a dashed line style for the number of deaths
- Change the line thickness to 3 and 2 for the births and deaths respectively.
- Do you notice anything in the late 1840s?

```
plt.figure(figsize=(14,8), dpi=220)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('Births', color='skyblue', fontsize=14)
ax2.set_ylabel('Deaths', color='crimson', fontsize=14)
 
# Set the minimum and maximum values on the axes
ax1.set_ylim([180, 400])
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

# Format ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.plot(df_monthly.date, df_monthly.births, color='skyblue', linewidth=3)
ax2.plot(df_monthly.date, df_monthly.deaths, color='crimson', linestyle='dashed', linewidth=2)
ax1.grid(color='grey', linestyle='--')
plt.show()
```

Just as in previous notebooks we can use `.twinx()` to create two y-axes. Then it's just a matter of adding a gird with `.grid()` and configuring the look of our plots with the `color`, `linewidth`, and `linestyle` parameters.

    plt.figure(figsize=(14,8), dpi=200)
    plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
    
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    
    ax1.grid(color='grey', linestyle='--')
    
    ax1.plot(df_monthly.date, 
            df_monthly.births, 
            color='skyblue', 
            linewidth=3)
    
    ax2.plot(df_monthly.date, 
            df_monthly.deaths, 
            color='crimson', 
            linewidth=2, 
            linestyle='--')
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_11-11-50-6276fcca4bbc46fa057415c170ba9189.png'>

To get the tickmarks showing up on the x-axis, we need to use mda`tes and Matplotlib's locators.

    # Create locators for ticks on the time axis
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter('%Y') 

We can then use the locators in our chart:

    plt.figure(figsize=(14,8), dpi=200)
    plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)
    
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    
    ax1.set_ylabel('Births', color='skyblue', fontsize=18)
    ax2.set_ylabel('Deaths', color='crimson', fontsize=18)
    
    # Use Locators
    ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)
    
    ax1.grid(color='grey', linestyle='--')
    
    ax1.plot(df_monthly.date, 
            df_monthly.births, 
            color='skyblue', 
            linewidth=3)
    
    ax2.plot(df_monthly.date, 
            df_monthly.deaths, 
            color='crimson', 
            linewidth=2, 
            linestyle='--')
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_11-16-35-039658c53b985fcbb11f9ffa26d074fd.png'>

What we see is that something happened after 1847. The total number of deaths seems to have dropped, despite an increasing number of births! 🤔


## 2. Analyzing the Yearly Data Split By Clinic

Welcome to your workplace...

There are two maternity wards at the Vienna General Hospital: clinic 1 and clinic 2. 
Clinic 1 was staffed by all-male doctors and medical students, and clinic 2 was staffed by female midwives.

### Challenge 1: The Yearly Data Split by Clinic

Let's turn our attention to the annual data. Use plotly to create line charts of the births and deaths of the two different clinics at the Vienna General Hospital.
- Which clinic is bigger or more busy judging by the number of births?
- Has the hospital had more patients over time?
- What was the highest number of deaths recorded in clinic 1 and clinic 2?


To show two line charts side by side we can use plotly and provide the clinic column as the color.

    line = px.line(df_yearly, 
                x='year', 
                y='births',
                color='clinic',
                title='Total Yearly Births by Clinic')
    
    line.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_11-31-13-b5897c5011eadac9f54e6956b30d4f97.png'>

We see that more and more women gave birth at the hospital over the years. 
Clinic 1, which was staffed by male doctors and medical students was also the busier or simply the larger ward. More births took place in clinic 1 than in clinic 2.

We also see that, not only were more people born in clinic 1, more people also died in clinic 1.

    line = px.line(df_yearly, 
                x='year', 
                y='deaths',
                color='clinic',
                title='Total Yearly Deaths by Clinic')
    
    line.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_11-32-45-1f1c814dd89d9e8102ff7642a53a3ecd.png'>

To compare apples and apples, we need to look at the proportion of deaths per clinic.


### Challenge 2: Calculate the Proportion of Deaths at Each Clinic

Calculate the proportion of maternal deaths per clinic. That way we can compare like with like.
- Work out the percentage of deaths for each row in the `df_yearly` DataFrame by adding a column called "`pct_deaths`".
- Calculate the average maternal death rate for clinic 1 and clinic 2 (i.e., the total number of deaths per the total number of births).
- Create another plotly line chart to see how the percentage varies year over year with the two different clinics.
- Which clinic has a higher proportion of deaths?
- What is the highest monthly death rate in clinic 1 compared to clinic 2?


We can add a new column that has the percentage of deaths for each row like this: 

    df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births

The average death rate for the entire time period for clinic 1 is:

    clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
    avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
    print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')

9.92%. In comparison, clinic 2 which was staffed by midwives had a much lower death rate of 3.88% over the course of the entire period. Hmm... 🤔

    clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
    avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
    print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')

Once again, let's see this on a chart

    line = px.line(df_yearly, 
                x='year', 
                y='pct_deaths',
                color='clinic',
                title='Proportion of Yearly Deaths by Clinic')
    
    line.show()

1842 was a rough year. About 16% of women died in clinic 1 and about 7.6% of women died in clinic 2.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_11-48-48-f1ea588ddc802796ce504f8cae08a844.png'>

Still, clinic 2 had a consistently lower death rate than clinic 1! This is what puzzled and frustrated Dr Semmelweis.

**The story continues...**

At first, Dr Semmelweis thought that the position of the women giving birth was the issue. In clinic 2, the midwives' clinic, women gave birth on their sides. 
In the doctors' clinic, women gave birth on their backs. So, Dr. Semmelweis, had women in the doctors' clinic give birth on their sides. 
However, this had no effect on the death rate.

Next, Dr Semmelweis noticed that whenever someone on the ward died, a priest would walk through clinic 1, past the women's beds ringing a bell 🔔. 
Perhaps the priest and the bell ringing terrified the women so much after birth that they developed a fever, got sick and died. 
Dr Semmelweis had the priest change his route and stop ringing the bell 🔕. Again, this had no effect.

At this point, Dr Semmelweis was so frustrated he went on holiday to Venice. Perhaps a short break would clear his head. 
When Semmelweis returned from his vacation, he was told that one of his colleagues, a pathologist, had fallen ill and died. 
His friend had pricked his finger while doing an autopsy on a woman who had died from childbed fever and subsequently got very sick himself and died. 😮

Looking at the pathologist's symptoms, Semmelweis realized the pathologist died from the same thing as the women he had autopsied.  
This was his breakthrough: anyone could get sick from childbed fever, not just women giving birth!

This is what led to Semmelweis' new theory. Perhaps there were little pieces or particles of a corpse that the doctors and medical students were getting on their hands while dissecting the cadavers during an autopsy. 
And when the doctors delivered the babies in clinic 1, these particles would get inside the women giving birth who would then develop the disease and die.


## 3. The Effect of Handwashing

In June 1846, Dr Semmelweis ordered everyone on his medical staff to start cleaning their hands and instruments not just with soap and water but with a chlorine solution (he didn't know it at the time, but chlorine is an amazing disinfectant). The reason Dr Semmelweis actually chose the chlorine was that he wanted to get rid of any smell on doctors' hands after an autopsy. No one knew anything about bacteria, germs or viruses at the time.


### Challenge 1: The Effect of Handwashing

- Add a column called "pct`_deaths" to `df_monthly` that has the percentage of deaths per birth for each row.
- Create two subsets from the `df_monthly` data: before and after Dr Semmelweis ordered washing hand.
- Calculate the average death rate prior to June 1846.
- Calculate the average death rate after June 1846.

```
df_monthly['pct_deaths'] = df_monthly.deaths / df_monthly.births
before_soap = df_monthly[df_monthly.date < handwashing_start]
after_soap = df_monthly[df_monthly.date >= handwashing_start]

avg_before = before_soap.deaths.sum() / before_soap.births.sum() * 100
print(f'Average death rate before soap is {avg_before:.3}%.')
avg_after = after_soap.deaths.sum() / after_soap.births.sum() * 100
print(f'Average death rate after soap is {avg_after:.3}%.')

Average death rate before soap is 10.5%.
Average death rate after soap is 2.15%.
```

We can add a column with the proportion of deaths per birth like so:

    df_monthly['pct_deaths'] = df_monthly.deaths/df_monthly.births

Then we can create two subsets based on the handwashing_start date.

    before_washing = df_monthly[df_monthly.date < handwashing_start]
    after_washing = df_monthly[df_monthly.date >= handwashing_start]

The death rate per birth dropped dramatically after handwashing started - from close to 10.53% to 2.15%. 
We can use the colon and dot inside a print statement to determine the number of digits we'd like to print out from a number.

    bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
    aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100
    print(f'Average death rate before 1847 was {bw_rate:.4}%')
    print(f'Average death rate AFTER 1847 was {aw_rate:.3}%')


### Challenge 2: Calculate a Rolling Average of the Death Rate

Create a DataFrame that has the 6-month rolling average death rate prior to mandatory handwashing.

*Hint*: You'll need to set the dates as the index in order to avoid the date column being dropped during the calculation

To work out the moving 6-month average we first set the date column as the index. Then we can use the same Pandas functions as in the Google Trends notebook.

    roll_df = before_washing.set_index('date')
    roll_df = roll_df.rolling(window=6).mean()

            births  deaths  pct_deaths
    date                                  
    1841-01-01     NaN     NaN         NaN
    1841-02-01     NaN     NaN         NaN
    1841-03-01     NaN     NaN         NaN
    1841-04-01     NaN     NaN         NaN
    1841-05-01     NaN     NaN         NaN
    ...            ...     ...         ...
    1847-01-01  274.50   29.00        0.11
    1847-02-01  290.50   23.50        0.08
    1847-03-01  296.17   18.83        0.07
    1847-04-01  305.83   22.00        0.07
    1847-05-01  305.33   22.67        0.07

    [76 rows x 3 columns]

### Challenge 3: Highlighting Subsections of a Line Chart

Copy-paste and then modify the Matplotlib chart from before to plot the monthly death rates (instead of the total number of births and deaths). 
The chart should look something like this:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_12-27-28-063144e4acbc37b96bfd66f6f25f75f3.png'>

- Add 3 separate lines to the plot: the death rate before handwashing, after handwashing, and the 6-month moving average before handwashing.
- Show the monthly death rate before handwashing as a thin dashed black line.
- Show the moving average as a thicker, crimson line.
- Show the rate after handwashing as a skyblue line with round markers.
- Look at the <a href='https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html'>code snippet</a> in the documentation to see how you can add a legend to the chart.


After copy-pasting the previous code for the Matplotlib chart, we just need to change a few things. 
First, we remove the twin axes. And instead, we plot the three different lines on the same axis. 
To create the legend, we supply a label to the `.plot()` function and capture return value in a variable. 
It's important to notice that `.plot()` returns more than one thing, so we need to use a comma (`,`) since we're only grabbing the first item. 
We can then feed these handles into `plt.legend()`.

```
plt.figure(figsize=(14,8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
 
plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)
 
ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
 
plt.grid(color='grey', linestyle='--')
 
moving_average_line, = plt.plot(roll_df.index, 
                    roll_df.pct_deaths, 
                    color='crimson', 
                    linewidth=3, 
                    linestyle='--',
                    label='6m Moving Average')
before_soap_line, = plt.plot(before_soap.date, 
                    before_soap.pct_deaths,
                    color='black', 
                    linewidth=1, 
                    linestyle='--', 
                    label='Before Handwashing')
after_soap_line, = plt.plot(after_soap.date, 
                    after_soap.pct_deaths, 
                    color='skyblue', 
                    linewidth=3, 
                    marker='o',
                    label='After Handwashing')
 
plt.legend(handles=[moving_average_line, before_soap_line, after_soap_line],
           fontsize=18)
 
plt.show()
```

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_12-26-50-27dd134e94624962bdb420ddb176e825.png'>


## 4. Visualizing Distributions and Testing for Statistical Significance

There are even more powerful arguments we can make to convince our fellow doctors in clinic 1 of the virtues of handwashing. 
The first are statistics regarding the mean monthly death rate. The second are compelling visualizations to accompany the statistics.


### Challenge 1: Calculate the Difference in the Average Monthly Death Rate

- What was the average percentage of monthly deaths before handwashing (i.e., before June 1847)?
- What was the average percentage of monthly deaths after handwashing was made obligatory?
- By how much did handwashing reduce the average chance of dying in childbirth in percentage terms?
- How do these numbers compare to the average for all the 1840s that we calculated earlier?
- How many times lower are the chances of dying after handwashing compared to before?

A lot of statistical tests rely on comparing features of distributions, like the **mean**. 
We see that the average death rate before handwashing was 10.5%. After handwashing was made obligatory, the average death rate was 2.11%. 
The difference is massive. Handwashing decreased the average death rate by 8.4%, a 5x improvement. 😮

    avg_prob_before = before_soap.pct_deaths.mean() * 100
    print(f'Chance of death during childbirth before handwashing: {avg_prob_before:.3}%.')
    
    avg_prob_after = after_soap.pct_deaths.mean() * 100
    print(f'Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.')
    
    mean_diff = avg_prob_before - avg_prob_after
    print(f'Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!')
    
    times = avg_prob_before / avg_prob_after
    print(f'This is a {times:.2}x improvement!')

    Chance of death during childbirth before handwashing: 10.5%.
    Chance of death during childbirth AFTER handwashing: 2.11%.
    Handwashing reduced the monthly proportion of deaths by 8.4%!
    This is a 5.0x improvement!


### Challenge 2: Using Box Plots to Show How the Death Rate Changed Before and After Handwashing

The statistic above is impressive, but how do we show it graphically? 
With a box plot we can show how the quartiles, minimum, and maximum values changed in addition to the mean.

- Use NumPy's <a href='https://numpy.org/doc/stable/reference/generated/numpy.where.html'>.where()</a> function to add a column to `df_monthly` that shows if a particular date was before or after the start of handwashing.
- Then use plotly to create box plot of the data before and after handwashing.
- How did key statistics like the mean, max, min, 1st and 3rd quartile changed as a result of the new policy


The easiest way to create a box plot is to have a column in our DataFrame that shows the rows' "category" (i.e., was it before or after obligatory handwashing). NumPy allows us to easily test for a condition and add a column of data.

    df_monthly['washing_hands'] = np.where(df_monthly.date < handwashing_start, 'No', 'Yes')

Now we can use plotly:

    box = px.box(df_monthly, 
                x='washing_hands', 
                y='pct_deaths',
                color='washing_hands',
                title='How Have the Stats Changed with Handwashing?')
    
    box.update_layout(xaxis_title='Washing Hands?',
                    yaxis_title='Percentage of Monthly Deaths',)
    
    box.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_14-39-42-eb859925d7e636d7244c6b410bad919b.png'>

The plot shows us the same data as our Matplotlib chart, but from a different perspective. Here we also see the massive spike in deaths in late 1842. 
Over 30% of women who gave birth that month died in hospital. What we also see in the box plot is how not only did the average death rate come down, but so did the overall range - we have a lower max and 3rd quartile too. Let's take a look at a histogram to get a better sense of the distribution.


### Challenge 3: Use Histograms to Visualise the Monthly Distribution of Outcomes

Create a plotly <a href='https://plotly.com/python/histograms/'>histogram</a> to show the monthly percentage of deaths.

- Use docs to check out the available parameters. Use the <a href='https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html'>`color` parameter</a> to display two overlapping histograms.
- The time period of handwashing is shorter than not handwashing. Change `histnorm` to `percent` to make the time periods comparable.
- Make the histograms slightly transparent
- Experiment with the number of `bins` on the histogram. Which number works well in communicating the range of outcomes?
- Just for fun, display your box plot on the top of the histogram using the `marginal` parameter


To create our histogram, we once again make use of the `color` parameter. This creates two separate histograms for us. 
When we set the opacity to 0.6 or so we can clearly see how the histograms overlap. 
The trick to getting a sensible-looking histogram when you have a very different number of observations is to set the `histnorm` to '`percent`'. 
That way the histogram with more observations won't completely overshadow the shorter series.

    hist = px.histogram(df_monthly, 
                    x='pct_deaths', 
                    color='washing_hands',
                    nbins=30,
                    opacity=0.6,
                    barmode='overlay',
                    histnorm='percent',
                    marginal='box',)
    
    hist.update_layout(xaxis_title='Proportion of Monthly Deaths',
                    yaxis_title='Count',)
    
    hist.show()

I quite like how in plotly we can display our box plot from earlier at the top.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_14-49-58-3961b13cff88b2866bba7da183716a04.png'>

Now, we have only about 98 data points or so, so our histogram looks a bit jagged. It's not a smooth bell-shaped curve. However, we can estimate what the distribution would look like with a Kernel Density Estimate (KDE).


### Challenge 4: Use a Kernel Density Estimate (KDE) to visualize a smooth distribution

Use <a href='https://seaborn.pydata.org/generated/seaborn.kdeplot.html'>Seaborn's `.kdeplot()`</a> to create two kernel density estimates of the `pct_deaths`, one for before handwashing and one for after.

- Use the `shade` parameter to give your two distributions different colors.
- What weakness in the chart do you see when you just use the default parameters?
- Use the `clip` parameter to address the problem.


To create two bell-shaped curves of the estimated distributions of the death rates we just call `.kdeplot()` twice.

    plt.figure(dpi=200)
    # By default the distribution estimate includes a negative death rate!
    sns.kdeplot(before_washing.pct_deaths, shade=True)
    sns.kdeplot(after_washing.pct_deaths, shade=True)
    plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
    plt.show()

    shade` is now deprecated in favor of `fill`; setting `fill=True`.
    This will become an error in seaborn v0.14.0; please update your code



    plt.figure(dpi=200)
    # By default the distribution estimate includes a negative death rate!
    sns.kdeplot(before_soap.pct_deaths, fill=True)
    sns.kdeplot(after_soap.pct_deaths, fill=True)
    plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_14-59-53-0b2eb0809a34c6eb94983086e631800c.png'>

However, the problem is that we end up with a negative monthly death rate on the left tail. 
The doctors would be very surprised indeed if a corpse came back to life after an autopsy! 🧟‍♀️

The solution is to specify a lower bound of 0 for the death rate.

    plt.figure(dpi=200)

    sns.kdeplot(before_soap.pct_deaths, fill=True, clip=(0,1))
    sns.kdeplot(after_soap.pct_deaths, fill=True, clip=(0,1))
    plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
    plt.xlim(0, 0.40)
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-23_15-00-50-d951f463f0f6b86e096672a3d6a05e77.png'>

Now that we have an idea of what the two distributions look like, we can further strengthen our argument for handwashing by using a statistical test. 
We can test whether our distributions ended up looking so different purely by chance (i.e., the lower death rate is just an accident) or if the 8.4% difference in the average death rate is **statistically significant**.


### Challenge 5: Use a T-Test to Show Statistical Significance

Use a **t-test** to determine if the differences in the means are statistically significant or purely due to chance.

If the **p-value** is less than 1% then we can be 99% certain that handwashing has made a difference to the average monthly death rate.

- Import `stats` from scipy
- Use the <a href='https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html'>`.ttest_ind()`</a> function to calculate the t-statistic and the p-value
- Is the difference in the average proportion of monthly deaths statistically significant at the 99% level?


The first step is to import stats from scipy

    import scipy.stats as stats

When we calculate the p_value we see that it is 0.0000002985 or .00002985% which is far below even 1%. 
In other words, the difference in means is highly statistically significant and we can go ahead on publish our research paper 😊

    t_stat, p_value = stats.ttest_ind(a=before_soap.pct_deaths, 
                                    b=after_soap.pct_deaths)
    print(f'p-palue is {p_value:.10f}')
    print(f't-statstic is {t_stat:.4}')

    p-palue is 0.0000002985
    t-statstic is 5.512



## 5. Learning Points & Summary

Well done, Doctor! With your thorough analysis and compelling visualisations of the handwashing data, you've convinced the hospital board to continue making hand washing obligatory!

**Today you've learned**

- How to use histograms to visualise distributions
- How to superimpose `histograms` on top of each other even when the data series have different lengths
- How to smooth out kinks in a histogram and visualise a distribution with a Kernel Density Estimate (`KDE`)
- How to improve a KDE by specifying boundaries on the estimates
- How to use `scipy` and test for statistical significance by looking at `p-values`.
- How to highlight different parts of a time series chart in Matplotib.
- How to add and configure a Legend in Matplotlib.
- Use NumPy's `.where()` function to process elements depending on a condition.
