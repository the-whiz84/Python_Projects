# Analyzing the Nobel Prize with Plotly, Matplotlib and Seaborn

Today we're going to analyze a dataset on the past winners of the Nobel Prize. Let's see what patterns we can uncover in the past Nobel laureates and what can we learn about the Nobel prize and our world more generally.

On November 27, 1895, Alfred Nobel signed his last will in Paris. When it was opened after his death, the will caused a lot of controversy, as Nobel had left much of his wealth for the establishment of a prize. 
Alfred Nobel dictates that his entire remaining estate should be used to endow “prizes to those who, during the preceding year, have conferred the greatest benefit to humankind”. Every year the Nobel Prize is given to scientists and scholars in the categories chemistry, literature, physics, physiology or medicine, economics, and peace.


## 1. Explore and Clean the Dataset

**Challenge 1**

Preliminary data exploration.
- What is the shape of `df_data`? How many rows and columns?
- What are the column names and what kind of data is inside of them?
- In which year was the Nobel prize first awarded?
- Which year is the latest year included in the dataset?

    df_data.shape
    (962, 16)

    df_data.head()
    df_data.tail()

    df_data.info()
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 962 entries, 0 to 961
    Data columns (total 16 columns):
    #   Column                 Non-Null Count  Dtype 
    ---  ------                 --------------  ----- 
    0   year                   962 non-null    int64 
    1   category               962 non-null    object
    2   prize                  962 non-null    object
    3   motivation             874 non-null    object
    4   prize_share            962 non-null    object
    5   laureate_type          962 non-null    object
    6   full_name              962 non-null    object
    7   birth_date             934 non-null    object
    8   birth_city             931 non-null    object
    9   birth_country          934 non-null    object
    10  birth_country_current  934 non-null    object
    11  sex                    934 non-null    object
    12  organization_name      707 non-null    object
    13  organization_city      707 non-null    object
    14  organization_country   708 non-null    object
    15  ISO                    934 non-null    object
    dtypes: int64(1), object(15)
    memory usage: 120.4+ KB

When we run df_data.shape, df_data.tail(), and df_data.head(), we see that there are 962 rows and 16 columns. 
The first Nobel prizes were awarded in 1901 and the data goes up to 2020.

We notice that the columns contain the following information:
- **birth_date**: date in string format
- **motivation**: description of what the prize is for
- **prize_share**: given as a fraction
- **laureate_type**: individual or organization
- **birth_country**: has countries that no longer exist
- **birth_country_current**: current name of the country where the birth city is located
- **ISO**: three-letter international country code
- **organization_name**: research institution where the discovery was made
- **organization_city**: location of the institution


**Challenge 2**
- Are there any duplicate values in the dataset?
- Are there NaN values in the dataset?
- Which columns tend to have NaN values?
- How many NaN values are there per column?
- Why do these columns have NaN values?

```
df_data.duplicated().values.any()
False

print(df_data.isna().values.any())
True

df_data.isna().sum()
year                       0
category                   0
prize                      0
motivation                88
prize_share                0
laureate_type              0
full_name                  0
birth_date                28
birth_city                31
birth_country             28
birth_country_current     28
sex                       28
organization_name        255
organization_city        255
organization_country     254
ISO                       28
dtype: int64

```

There are no duplicates in the dataset:

    print(f'Any duplicates? {df_data.duplicated().values.any()}')

However, there are a number of NaN values

    print(f'Any NaN values among the data? {df_data.isna().values.any()}')

We can get a count of the NaN values per column using

    df_data.isna().sum()

Why are there so many `NaN` values for the birth date? And why are there so many missing values among the organization columns?

Filtering on the NaN values in the birth date column we see that we get back a bunch of organizations, like the UN or the Red Cross.

    col_subset = ['year','category', 'laureate_type',
                'birth_date','full_name', 'organization_name']
    df_data.loc[df_data.birth_date.isna()][col_subset]

That makes sense. We also see that since the organization's name is in the `full_name` column, the `organization_name` column contains `NaN`.

In addition, when we look at for rows where the `organization_name` column has no value, we also see that many prizes went to people who were not affiliated with a university or research institute. This includes many of the `Literature` and `Peace` prize winners.

    col_subset = ['year','category', 'laureate_type','full_name', 'organization_name']
    df_data.loc[df_data.organization_name.isna()][col_subset]


**Challenge 3**

Convert the `birth_date` column to Pandas `Datetime` objects

Add a Column called `share_pct` which has the laureates' share as a percentage in the form of a floating-point number.

```
df_data.year = pd.to_datetime(df_data.year)
df_data.birth_date = pd.to_datetime(df_data.birth_date)
df_data.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 962 entries, 0 to 961
Data columns (total 16 columns):
 #   Column                 Non-Null Count  Dtype         
---  ------                 --------------  -----         
 0   year                   962 non-null    datetime64[ns]
 1   category               962 non-null    object        
 2   prize                  962 non-null    object        
 3   motivation             874 non-null    object        
 4   prize_share            962 non-null    object        
 5   laureate_type          962 non-null    object        
 6   full_name              962 non-null    object        
 7   birth_date             934 non-null    datetime64[ns]
 8   birth_city             931 non-null    object        
 9   birth_country          934 non-null    object        
 10  birth_country_current  934 non-null    object        
 11  sex                    934 non-null    object        
 12  organization_name      707 non-null    object        
 13  organization_city      707 non-null    object        
 14  organization_country   708 non-null    object        
 15  ISO                    934 non-null    object        
dtypes: datetime64[ns](2), object(14)
memory usage: 120.4+ KB
```

Adding a column that contains the percentage share first requires that we split the string on the forward slash. 
Then we can convert to a number. And finally, we can do the division.

    separated_values = df_data.prize_share.str.split('/', expand=True)
    numerator = pd.to_numeric(separated_values[0])
    denomenator = pd.to_numeric(separated_values[1])
    df_data['share_pct'] = numerator / denomenator

Now we can check if our type conversions were successful:

    df_data.info()

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 962 entries, 0 to 961
    Data columns (total 17 columns):
    #   Column                 Non-Null Count  Dtype         
    ---  ------                 --------------  -----         
    0   year                   962 non-null    datetime64[ns]
    1   category               962 non-null    object        
    2   prize                  962 non-null    object        
    3   motivation             874 non-null    object        
    4   prize_share            962 non-null    object        
    5   laureate_type          962 non-null    object        
    6   full_name              962 non-null    object        
    7   birth_date             934 non-null    datetime64[ns]
    8   birth_city             931 non-null    object        
    9   birth_country          934 non-null    object        
    10  birth_country_current  934 non-null    object        
    11  sex                    934 non-null    object        
    12  organization_name      707 non-null    object        
    13  organization_city      707 non-null    object        
    14  organization_country   708 non-null    object        
    15  ISO                    934 non-null    object        
    16  share_pct              962 non-null    float64       
    dtypes: datetime64[ns](2), float64(1), object(14)
    memory usage: 127.9+ KB


## 2. plotly Bar & Donut Charts: Analyze Prize Categories & Women Winning Prizes


### Challenge 1: Come up with 3 Questions

A big part of data science is coming up with questions that you'd like to explore. 
This is the most difficult aspect to teach in a tutorial because it's completely open-ended and requires some creativity. 
Often times you will be asking questions of the data, that it actually cannot answer - and that's ok. That's all part of the process of discovery.

Pause here for a moment and think about the kind of data you saw in the columns. Write down at least 3 questions that you'd like to explore as part of this analysis. 
For example, your question might go like: "What percentage of the Nobel laureates were women?" or "How many prizes were given out in each category". 
Practice coming up with a few of your own questions.

In the upcoming lessons, you might find that we will write the code to answer some of your questions. And if not, your questions make for a great exercise to take this analysis even further.

The challenges below are all based on questions we're going to ask the data:

### Challenge 2

Create a <a href='https://plotly.com/python/pie-charts/'>donut chart</a> using plotly which shows how many prizes went to men compared to how many prizes went to women. 
What percentage of all the prizes went to women?

To create the chart we use the our `.value_counts()` method together with plotly's `.pie()` function. 
We see that out of all the Nobel laureates since 1901, only about 6.2% were women.

    biology = df_data.sex.value_counts()
    fig = px.pie(labels=biology.index, 
                values=biology.values,
                title="Percentage of Male vs. Female Winners",
                names=biology.index,
                hole=0.4,)
    
    fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
    
    fig.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_11-56-24-23e01a3883d76f0a36dd62e0ad401479.png'>



### Challenge 3

- What are the names of the first 3 female Nobel laureates?
- What did the win the prize for?
- What do you see in their `birth_country`? Were they part of an organization?

    df_data[df_data.sex == 'Female'].head(3)

Even without looking at the data, you might have already guessed one of the famous names: Marie Curie.

    df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_11-59-16-2880c50d998356973cfa975e30bd642c.png'>



### Challenge 4

Did some people get a Nobel Prize more than once? If so, who were they?

Winning a Nobel prize is quite an achievement. However, some folks have actually won the prize multiple times. To find them, we can use many different approaches. 
One approach is to look for duplicates in the full_name column:

    is_winner = df_data.duplicated(subset=['full_name'], keep=False)
    multiple_winners = df_data[is_winner]
    print(f'There are {multiple_winners.full_name.nunique()}' \
        ' winners who were awarded the prize more than once.')

There are 6 winners who were awarded the prize more than once.

    col_subset = ['year', 'category', 'laureate_type', 'full_name']
    multiple_winners[col_subset]

Only 4 of the repeat laureates were individuals.

We see that Marie Curie actually got the Nobel prize twice - once in physics and once in chemistry. Linus Carl Pauling got it first in chemistry and later for peace given his work in promoting nuclear disarmament. Also, the International Red Cross was awarded the Peace prize a total of 3 times. The first two times were both during the devastating World Wars.
### Challenge 5

- In how many categories are prizes awarded?
- Create a plotly bar chart with the number of prizes awarded by category.
- Use the color scale called `Aggrnyl` to color the chart, but don't show a color axis.
- Which category has the most number of prizes awarded?
- Which category has the fewest number of prizes awarded?

To find the number of unique categories in a column we can use:

    df_data.category.nunique()

To generate the vertical plotly bar chart, we again use .value_counts():

    prizes_per_category = df_data.category.value_counts()
    v_bar = px.bar(
            x = prizes_per_category.index,
            y = prizes_per_category.values,
            color = prizes_per_category.values,
            color_continuous_scale='Aggrnyl',
            title='Number of Prizes Awarded per Category')
    
    v_bar.update_layout(xaxis_title='Nobel Prize Category', 
                        coloraxis_showscale=False,
                        yaxis_title='Number of Prizes')
    v_bar.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_13-59-47-6fea83b45bae6cda8e421d02b71aa380.png'>


### Challenge 6

- When was the first prize in the field of Economics awarded?
- Who did the prize go to?

    df_data[df_data.category == 'Economics'].head()

The chart above begs the question: "Why are there so few prizes in the field of economics?". 
Looking at the first couple of winners in the economics category, we have our answer:

    df_data[df_data.category == 'Economics'].sort_values('year')[:3]

The economics prize is much newer. It was first awarded in 1969, compared to 1901 for physics.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-03-25-9b4e50252c31bbc38d8171905a26b9a5.png'>


### Challenge 7

Create a plotly <a href='https://plotly.com/python/bar-charts/'>bar chart</a> that shows the split between men and women by category.

Hover over the bar chart. How many prizes went to women in Literature compared to Physics?


We already saw that overall, only 6.2% of Nobel prize winners were female. Does this vary by category?

    cat_men_women = df_data.groupby(['category', 'sex'], 
                                as_index=False).agg({'prize': pd.Series.count})
    cat_men_women.sort_values('prize', ascending=False, inplace=True)

We can combine `.groupby()` and `.agg()` with the `.count()` function. This way we can count the number of men and women by prize category.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-06-59-34c0d756c22989eb982fcf00dd78bcff.png'>

We can then use the parameter `.color`  in the `.bar()` function to mark the number of men and women on the chart:

    v_bar_split = px.bar(x = cat_men_women.category,
                        y = cat_men_women.prize,
                        color = cat_men_women.sex,
                        title='Number of Prizes Awarded per Category split by Men and Women')
    
    v_bar_split.update_layout(xaxis_title='Nobel Prize Category', 
                            yaxis_title='Number of Prizes')
    v_bar_split.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-09-23-ba9b59621175ffd123d135b4cd46fed5.png'>

We see that overall the imbalance is pretty large with physics, economics, and chemistry. Women are somewhat more represented in categories of Medicine, Literature and Peace. Splitting bar charts like this is an incredibly powerful way to show a more granular picture.


## 3. Using Matplotlib to Visualise Trends over Time

Now let's look at how things have changed over time. This will give us a chance to review what we learnt about creating charts with two y-axes in Matplotlib and generating arrays with NumPy.

### Challenge 1

Are more prizes awarded recently than when the prize was first created? Show the trend in awards visually.
- Count the number of prizes awarded every year.
- Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analyzing Google Trends).
- Using Matplotlib superimpose the rolling average on a scatter plot.
- Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-15-10-c99698bd9d7749499bb42a4763d446a6.png'>

- Use the <a href='https://matplotlib.org/stable/gallery/color/named_colors.html'>named colors</a> to draw the data points in `dogerblue` while the rolling average is coloured in `crimson`.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-15-24-c67d3b9baeaa22b2f28b6d3a2202d77a.png'>

- Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out?
- What could be the reason for the trend in the chart?


First, we have to count the number of Nobel prizes that are awarded each year.

    prize_per_year = df_data.groupby(by='year').count().prize
    prize_per_year

    year
    1901     6
    1902     7
    1903     7
    1904     6
    1905     5
            ..
    2016    11
    2017    12
    2018    13
    2019    14
    2020    12
    Name: prize, Length: 117, dtype: int64

This just involves grouping the data so that we can count the number of entries per year. To calculate the 5-year moving average we use `.rolling()` and `.mean()` like we did with the Google Trend data.

    moving_average = prize_per_year.rolling(window=5).mean()
    moving_average

    year
    1901     NaN
    1902     NaN
    1903     NaN
    1904     NaN
    1905    6.20
            ... 
    2016   11.60
    2017   12.00
    2018   12.00
    2019   12.20
    2020   12.40
    Name: prize, Length: 117, dtype: float64


Now we can create a Matplotlib chart that superimposes the two:

    plt.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
    
    plt.plot(prize_per_year.index, 
            moving_average.values, 
            c='crimson', 
            linewidth=3,)
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-23-51-6e82d0a2a593ae5f05b2562d18daed03.png'>

With the help of a little styling, this chart could look better. To create 5-year tick marks on the x-axis, we generate an array using **NumPy**:

    np.arange(1900, 2021, step=5)

Then we tap into functions like the `.figure()`, the `.title()`, the `.xticks()`, and `.yticks()` to fine-tune the chart.

In addition, we will shortly be adding a second y-axis, so we can use an `Axes` object to draw our scatter and line plots.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-20-53-0c21b93b7886ff45ea6503747813ff1c.png'>


### Challenge 2

Investigate if more prizes are shared than before.
- Calculate the average prize share of the winners on a year by year basis.
- Calculate the 5 year rolling average of the percentage share.
- Copy-paste the cell from the chart you created above.
- Modify the code to add a secondary axis to your Matplotlib chart.
- Plot the rolling average of the prize share on this chart.
- See if you can invert the secondary y-axis to make the relationship even more clear.


Now we can work out the rolling average of the percentage share of the prize. If more prizes are given out, perhaps it is because the prize is split between more people.

    yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
    share_moving_average = yearly_avg_share.rolling(window=5).mean()

    print(yearly_avg_share)
          share_pct
    year           
    1901       0.83
    1902       0.71
    1903       0.71
    1904       0.83
    1905       1.00
    ...         ...
    2016       0.55
    2017       0.50
    2018       0.46
    2019       0.43
    2020       0.50

    [117 rows x 1 columns]

    print(share_moving_average)
        share_pct
    year           
    1901        NaN
    1902        NaN
    1903        NaN
    1904        NaN
    1905       0.82
    ...         ...
    2016       0.52
    2017       0.50
    2018       0.50
    2019       0.50
    2020       0.49

    [117 rows x 1 columns]


If more people get the prize, then the average share should go down, right?

    plt.figure(figsize=(16,8), dpi=200)
    plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(ticks=np.arange(1900, 2021, step=5), 
            fontsize=14, 
            rotation=45)
    
    ax1 = plt.gca()
    ax2 = ax1.twinx() # create second y-axis
    ax1.set_xlim(1900, 2020)
    
    ax1.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
    
    ax1.plot(prize_per_year.index, 
            moving_average.values, 
            c='crimson', 
            linewidth=3,)
    
    # Adding prize share plot on second axis
    ax2.plot(prize_per_year.index, 
            share_moving_average.values, 
            c='grey', 
            linewidth=3,)
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-31-42-191579962fb7cb3a64f2c97d6f78c438.png'>

To see the relationship between the number of prizes and the laureate share even more clearly we can invert the second y-axis.

    plt.figure(figsize=(16,8), dpi=200)
    plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(ticks=np.arange(1900, 2021, step=5), 
            fontsize=14, 
            rotation=45)
    
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax1.set_xlim(1900, 2020)
    
    # Can invert axis
    ax2.invert_yaxis()
    
    ax1.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
    
    ax1.plot(prize_per_year.index, 
            moving_average.values, 
            c='crimson', 
            linewidth=3,)
    
    ax2.plot(prize_per_year.index, 
            share_moving_average.values, 
            c='grey', 
            linewidth=3,)
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-38-11-076469c853c7b83bc6a9ec20fc1a0aaf.png'>

What do we see on the chart? Well, there is clearly an upward trend in the number of prizes being given out as more and more prizes are shared. 
Also, more prizes are being awarded from 1969 onwards because of the addition of the economics category. 
We also see that very few prizes were awarded during the first and second world wars. Note that instead of there being a zero entry for those years, we instead see the effect of the wars as missing blue dots.


## 4. A Choropleth Map and the Countries with the Most Prizes

For this next bit, we're going to compare which countries actually get the most prizes. And we're also going to look at in which categories those prizes are awarded. 
This has me feeling a little like I'm at the Olympics 😊.


### Challenge 1: Top 20 Country Ranking

- Create a Pandas DataFrame called `top20_countries` that has the two columns. The prize column should contain the total number of prizes won.
- Is it best to use `birth_country`, `birth_country_current` or `organization_country`?
- What are some potential problems when using `birth_country` or any of the others? Which column is the least problematic?
- Then use plotly to create a horizontal bar chart showing the number of prizes won by each country. Here's what you're after:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-43-26-c29a036da3674550eb3e9879a6f1b3a6.png'>

- What is the ranking for the top 20 countries in terms of the number of prizes?


Looking at our DataFrame there are actually 3 different columns to choose from for creating this ranking: `birth_country`, `birth_country_current` or `organization_country`. However, they each have certain problems and limitations.

If you look at the entries in the birth country, you'll see that some countries no longer exist! These include the Soviet Union or Czechoslovakia for example. 
Hence, using `birth_country_current` is better, since it has the country name which controls the city where the laureate was born. 
Now, notice that this does not determine the laureates' nationality since some globetrotting folks gave birth to their future Nobel laureate children while abroad. 
Also, people's nationalities can change as they emigrate and acquire different citizenship or get married and change citizenship. What this boils down to is that we will have to be clear about the assumptions that we will make in the upcoming analysis.

We can create the list of the top 20 countries like this:

    top_countries = df_data.groupby(['birth_country_current'], 
                                    as_index=False).agg({'prize': pd.Series.count})
    
    top_countries.sort_values(by='prize', inplace=True)
    top20_countries = top_countries[-20:]

    h_bar = px.bar(x=top20_countries.prize,
               y=top20_countries.birth_country_current,
               orientation='h',
               color=top20_countries.prize,
               color_continuous_scale='Viridis',
               title='Top 20 Countries by Number of Prizes')
 
    h_bar.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title='Country',
                        coloraxis_showscale=False)
    h_bar.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_15-28-14-d0951596c2e1a822e6b53fd9fc21e3ff.png'>

The United States has a massive number of prizes by this measure. The UK and Germany are in second and third place respectively.

### Challenge 2: Choropleth Map

Create this choropleth map using <a href='https://plotly.com/python/choropleth-maps/'>the plotly documentation</a>:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_14-44-57-c9ec3018035c0e32588e167a8e8b0a00.png'>


Experiment with plotly's available <a href='https://plotly.com/python/builtin-colorscales/'>colors</a>. I quite like the sequential colour `matter` on this map.

**Hint**: You'll need to use a 3 letter country code for each country.

```
top20_countries = df_data.groupby(['birth_country_current', 'ISO'], 
                                  as_index=False).agg({'prize': pd.Series.count})
 
top20_countries.sort_values(by='prize', ascending=True, inplace=True)

top20_countries = top20_countries[-20:]
top20_countries

fig = px.choropleth(top20_countries, locations="ISO",
                    color=top20_countries.prize, 
                    hover_name="birth_country_current", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.matter)
fig.show()
```

To show the above ranking on a color coded map, we need to make use of the ISO codes.

    df_countries = df_data.groupby(['birth_country_current', 'ISO'], 
                                as_index=False).agg({'prize': pd.Series.count})
    df_countries.sort_values('prize', ascending=False)

This means we can use the ISO country codes for the locations parameter on the choropleth.

    world_map = px.choropleth(df_countries,
                            locations='ISO',
                            color='prize', 
                            hover_name='birth_country_current', 
                            color_continuous_scale=px.colors.sequential.matter)
    
    world_map.update_layout(coloraxis_showscale=True,)
 
    world_map.show()


### Challenge 3: Country Bar Chart with Prize Category

See if you can divide up the plotly bar chart you created above to show the which categories made up the total number of prizes. 
Here's what you're aiming for:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_15-11-40-896b68120f5e2daa0e2823f286619336.png'>

- In which category are Germany and Japan the weakest compared to the United States?
- In which category does Germany have more prizes than the UK?
- In which categories does France have more prizes than Germany?
- Which category makes up most of Australia's Nobel prizes?
- Which category makes up half of the prizes in the Netherlands?
- Does the United States have more prizes in Economics than all of France? What about in Physics or Medicine?
- The hard part is preparing the data for this chart!

*Hint*: Take a two-step approach. The first step is grouping the data by country and category. 
Then you can create a DataFrame that looks something like this:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_15-11-54-d06c71c4976b32b66b2bef08144cb67a.png'>


Preparing our data to show the breakdown by category and country is challenging. 
We'll take a two-step approach here. First we count the prizes by category in each country:

    top20_countries = df_data.groupby(['birth_country_current'], 
                                  as_index=False).agg({'prize': pd.Series.count})
    top20_countries.sort_values(by='prize', ascending=True, inplace=True)
    top20_countries = top20_countries[-20:]


    cat_country = df_data.groupby(['birth_country_current', 'category'], 
                                as_index=False).agg({'prize': pd.Series.count})
    cat_country.sort_values(by='prize', ascending=False, inplace=True)

            birth_country_current   category  prize
    204  United States of America   Medicine     78
    206  United States of America    Physics     70
    201  United States of America  Chemistry     55
    202  United States of America  Economics     49
    198            United Kingdom   Medicine     28
    ..                        ...        ...    ...
    97                       Iraq      Peace      1
    99                    Ireland   Medicine      1
    100                   Ireland    Physics      1
    102                    Israel  Economics      1
    210                  Zimbabwe      Peace      1

    [211 rows x 3 columns]

Next, we can merge the DataFrame above with the top20_countries DataFrame that we created previously. That way we get the total number of prizes in a single column too. 
This is important since we want to control the order for our bar chart.

    merged_df = pd.merge(cat_country, top20_countries, on='birth_country_current')
    # change column names
    merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize'] 
    merged_df.sort_values(by='total_prize', inplace=True)

            birth_country_current    category  cat_prize  total_prize
    210                  Zimbabwe       Peace          1            1
    161                Bangladesh       Peace          1            1
    153                Costa Rica       Peace          1            1
    147                  Ethiopia       Peace          1            1
    145                   Myanmar       Peace          1            1
    ..                        ...         ...        ...          ...
    3    United States of America   Economics         49          281
    2    United States of America   Chemistry         55          281
    1    United States of America     Physics         70          281
    19   United States of America  Literature         10          281
    0    United States of America    Medicine         78          281

    [211 rows x 4 columns]

Now we can create our bar chart again. This time we use the color parameter based on the category.

    cat_cntry_bar = px.bar(x=merged_df.cat_prize,
                        y=merged_df.birth_country_current,
                        color=merged_df.category,
                        orientation='h',
                        title='Top 20 Countries by Number of Prizes and Category')
    
    cat_cntry_bar.update_layout(xaxis_title='Number of Prizes', 
                                yaxis_title='Country')
    cat_cntry_bar.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_15-44-31-1906cb97c5380befcc9d9c09d2880032.png'>

Splitting the country bar chart by category allows us to get a very granular look at the data and answer a whole bunch of questions. 
For example, we see is that the US has won an incredible proportion of the prizes in the field of Economics. 
In comparison, Japan and Germany have won very few or no economics prize at all. Also, the US has more prizes in physics or medicine alone than all of France's prizes combined. 
On the chart, we also see that Germany won more prizes in physics than the UK and that France has won more prizes in peace and literature than Germany, even though Germany has been awarded a higher total number of prizes than France.

When did the United States become so dominant? Was it always this way? Has the prize become more global in scope? 


### Challenge 4: Prizes by Country over Time

Every country's fortunes wax and wane over time. Investigate how the total number of prizes awarded changed over the years.
- When did the United States eclipse every other country in terms of the number of prizes won?
- Which country or countries were leading previously?
- Calculate the cumulative number of prizes won by each country in every year. Again, use the `birth_country_current` of the winner to calculate this.
- Create a plotly <a href='https://plotly.com/python/line-charts/'>line chart</a> where each country is a coloured line.


To see how the prize was awarded over time. To do that, we can count the number of prizes by country by year.

    prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
    prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]

Then we can create a series that has the cumulative sum for the number of prizes won.

    cumulative_prizes = prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum()
    cumulative_prizes.reset_index(inplace=True) 

Using this, we can create a chart, using the current birth country as the `color`:

    l_chart = px.line(cumulative_prizes,
                    x='year', 
                    y='prize',
                    color='birth_country_current',
                    hover_name='birth_country_current')
    
    l_chart.update_layout(xaxis_title='Year',
                        yaxis_title='Number of Prizes')
    
    l_chart.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-05-40-d768858f0f5ab25eb4082e5b2d0332cf.gif'>

What we see is that the United States really started to take off after the Second World War which decimated Europe. 
Prior to that, the Nobel prize was pretty much a European affair. Very few laureates were chosen from other parts of the world. 
This has changed dramatically in the last 40 years or so. There are many more countries represented today than in the early days. 
Interestingly we also see that the UK and Germany traded places in the 70s and 90s on the total number of prizes won. 
Sweden being 5th place pretty consistently over many decades is quite interesting too. Perhaps this reflects a little bit of home bias? 😊

All this analysis of different countries makes me curious about where the actual research is happening. Where are the cities and organisations located where people actually make discoveries? 


## 5. Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations

### Challenge 1

Many Nobel laureates are affiliated with a university, a laboratory, or a research organization (apart from Literature and Peace prize winners as we've seen). 
But the world is a big place. Which research institutions had the most Nobel laureates working there at the time of making the discovery?

Create a bar chart showing the organisations affiliated with the Nobel laureates. It should looks something like this:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-18-43-4bf4936075c466a83bf4fee81d4bcbd5.png'>

- Which organisations make up the top 20?
- How many Nobel prize winners are affiliated with the University of Chicago and Harvard University?

    top20_orgs = df_data.groupby(['organization_name'], 
                                    as_index=False).agg({'prize': pd.Series.count})
    
    top20_orgs.sort_values(by='prize', ascending=True, inplace=True)
    top20_orgs = top20_orgs[-20:]

    print(top20_orgs)
                                    organization_name  prize
    79                               Institut Pasteur      7
    109                             London University      7
    67                         Harvard Medical School      7
    192                     University College London      7
    40                             Cornell University      8
    12                              Bell Laboratories      8
    258                               Yale University      9
    111           MRC Laboratory of Molecular Biology     10
    222                          University of Oxford     12
    152                        Rockefeller University     13
    119                           Max-Planck-Institut     13
    146                          Princeton University     15
    38                            Columbia University     17
    26   California Institute of Technology (Caltech)     17
    197                       University of Cambridge     18
    198                         University of Chicago     20
    117   Massachusetts Institute of Technology (MIT)     21
    167                           Stanford University     23
    68                             Harvard University     29
    196                      University of California     40

    org_bar = px.bar(x=top20_orgs.prize,
                y=top20_orgs.organization_name,
                orientation='h',
                color=top20_orgs.prize,
                color_continuous_scale='Viridis',
                title='Top 20 Organizations by Number of Prizes')
    
    org_bar.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title='Organization',
                        coloraxis_showscale=False)
    org_bar.show()


This one should be pretty simple:

    top20_orgs = df_data.organization_name.value_counts()[:20]
    top20_orgs.sort_values(ascending=True, inplace=True)

Our chart includes many of the usual suspects:

    org_bar = px.bar(x = top20_orgs.values,
                    y = top20_orgs.index,
                    orientation='h',
                    color=top20_orgs.values,
                    color_continuous_scale=px.colors.sequential.haline,
                    title='Top 20 Research Institutions by Number of Prizes')
    
    org_bar.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title='Institution',
                        coloraxis_showscale=False)
    org_bar.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-32-06-e8df8d97281819d8f0359c11bac9bfb8.png'>


### Challenge 2

Each research organisation is located in a particular city. Are some cities hot spots for scientific discoveries? Where do major discoveries tend to take place?

- Create another plotly bar chart graphing the top 20 organisation cities of the research institutions associated with a Nobel laureate.
- Where is the number one hotspot for discoveries in the world?
- Which city in Europe has had the most discoveries?

    top20_orgs_cities = df_data.organization_city.value_counts()[:20]
    top20_orgs_cities.sort_values(ascending=True, inplace=True)

    city_bar2 = px.bar(x=top20_orgs_cities.values,
                y=top20_orgs_cities.index,
                orientation='h',
                color=top20_orgs_cities.values,
                color_continuous_scale='Viridis',
                title="Top 20 Organization's Cities by Number of Prizes")
    
    city_bar2.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title="Organization's City",
                        coloraxis_showscale=False)
    city_bar2.show()

Cambridge Massachusets and New York in the United States lead the pack:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-33-45-b33d120ab774aace3fda3b522a405341.png'>


### Challenge 3

Contrast the above chart with the birth city of the Nobel laureates. Would you expect to see a similar ranking for where the laureates are born versus where most discoveries are made? Would you expect to see the most populous cities producing the highest number of Nobel laureates? 

- Create a plotly bar chart graphing the top 20 birth cities of Nobel laureates.
- Use a named colour scale called `Plasma` for the chart.
- What percentage of the United States prizes came from Nobel laureates born in New York?
- How many Nobel laureates were born in London, Paris and Vienna?
- Out of the top 5 cities, how many are in the United States?

    top20_cities = df_data.birth_city.value_counts()[:20]
    top20_cities.sort_values(ascending=True, inplace=True)
    top20_cities

    birth_city
    Ann Arbor, MI             3
    Montreal                  4
    Cairo                     4
    Pittsburgh, PA            4
    Prague                    5
    Frankfurt-on-the-Main     5
    Hamburg                   6
    Stockholm                 6
    Moscow                    7
    Munich                    7
    Budapest                  8
    Brooklyn, NY              8
    Washington, DC            8
    Boston, MA                8
    Berlin                   11
    Chicago, IL              12
    Vienna                   14
    London                   19
    Paris                    26
    New York, NY             53
    Name: count, dtype: int64

    city_bar = px.bar(x=top20_cities.values,
                y=top20_cities.index,
                orientation='h',
                color=top20_cities.values,
                color_continuous_scale='Plasma',
                title="Top 20 Laureate Birth Cities by Number of Prizes")
    
    city_bar.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title="Laureate's Birth City",
                        coloraxis_showscale=False)
    city_bar.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-40-44-6ffe0befd6b184a767c184fb64906fda.png'>

A higher population definitely means that there's a higher chance of a Nobel laureate to be born there. New York, Paris, and London are all very populous. 
However, Vienna and Budapest are not and still produced many prize winners. That said, much of the ground-breaking research does not take place in big population centres, so the list of birth cities is quite different from the list above. 
Cambridge Massachusets, Stanford, Berkely and Cambridge (UK) are all the places where many discoveries are made, but they are not the birthplaces of laureates.


### Challenge 4

- Create a DataFrame that groups the number of prizes by organisation.
- Then use the plotly documentation to create a <a href='https://plotly.com/python/sunburst-charts/'>sunburst chart</a>
- Click around in your chart, what do you notice about Germany and France?

Here's what you're aiming for:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-28-14-33e9e87ab3c8bed913f451342e7af3fe.png'>

Each country has a number of cities, which in turn contain the research organisations. The sunburst chart is perfect for representing this relationship. 
It will give us an idea of how geographically concentrated scientific discoveries are!

    country_city_org = df_data.groupby(by=['organization_country', 
                                        'organization_city', 
                                        'organization_name'], as_index=False).agg({'prize': pd.Series.count})
    
    country_city_org = country_city_org.sort_values('prize', ascending=False)

             organization_country     organization_city  \
    205  United States of America         Cambridge, MA   
    280  United States of America          Stanford, CA   
    206  United States of America         Cambridge, MA   
    209  United States of America           Chicago, IL   
    195  United States of America          Berkeley, CA   
    ..                        ...                   ...   
    110                     Japan               Sapporo   
    111                     Japan                 Tokyo   
    112                     Japan                 Tokyo   
    113                     Japan                 Tokyo   
    290  United States of America  Yorktown Heights, NY   

                                organization_name  prize  
    205                           Harvard University     29  
    280                          Stanford University     23  
    206  Massachusetts Institute of Technology (MIT)     21  
    209                        University of Chicago     20  
    195                     University of California     19  
    ..                                           ...    ...  
    110                          Hokkaido University      1  
    111                      Asahi Kasei Corporation      1  
    112                          Kitasato University      1  
    113                Tokyo Institute of Technology      1  
    290         IBM Thomas J. Watson Research Center      1  

    [291 rows x 4 columns]


    burst = px.sunburst(country_city_org, 
                        path=['organization_country', 'organization_city', 'organization_name'], 
                        values='prize',
                        title='Where do Discoveries Take Place?',
                    )
    
    burst.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title='City',
                        coloraxis_showscale=False)
    
    burst.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_16-47-52-801621189ef9ffc4c83025bac35b9861.gif'>

France is a great example of concentration. Practically all the organisations affiliated with Nobel prize winners are in Paris. 
In contrast, scientific discoveries are much more spread out across Germany. Meanwhile, the UK is dominated by Cambridge and London.


## 6. Unearthing Patterns in the Laureate Age at the Time of the Award

How old are the Nobel laureates at the time when they win the prize? Does this vary by category? 
Also, how has the age of the laureates changed over time?


### Challenge 1

Calculate the age of the laureate in the year of the ceremony and add this as a column called `winning_age` to the `df_data` DataFrame. 
*Hint*: you can use <a href='https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html'>this</a> to help you.


First, we need to extract the year as a number from the birth_date column:

    birth_years = df_data.birth_date.dt.year

Now we can work out the age at the time of the award:

    df_data['winning_age'] = df_data.year - birth_years


### Challenge 2

Who were the oldest and the youngest winners?

- What are the names of the youngest and oldest Nobel laureate?
- What did they win the prize for?
- What is the average age of a winner?
- 75% of laureates are younger than what age when they receive the prize?
- Use Seaborn to <a href='https://seaborn.pydata.org/generated/seaborn.histplot.html'>create histogram</a> to visualise the distribution of laureate age at the time of winning. Experiment with the number of `bins` to see how the visualisation changes.

    display(df_data.nlargest(n=1, columns='winning_age'))
    display(df_data.nsmallest(n=1, columns='winning_age'))

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_17-03-14-869510accc99fe0ab455b4f22582010a.png'>

John Goodenough was 97 years old when he got the Nobel prize!!! Holy moly. Interestingly John was born to American parents while they were in Germany. 
This is one example where our analysis of countries counts an extra "German" prize even though he is an American citizen. 
Too bad we don't have a nationality column in our dataset! Nonetheless, this goes to show it is never too late to win a Nobel prize.


### Challenge 3

- Calculate the descriptive statistics for the age at the time of the award.
- Then visualise the distribution in the form of a histogram using Seaborn's `.histplot()` function.
- Experiment with the `bin` size. Try 10, 20, 30, and 50.

Using `.describe()` is a fantastic way to get a feeling for how the numbers are distributed in a particular column. 
However, actually visualising them on a histogram to see their distribution is highly recommended too since it allows us to see if we have a bell-shaped curve or something else.

    df_data.winning_age.describe()

    count   934.00
    mean     59.95
    std      12.62
    min      17.00
    25%      51.00
    50%      60.00
    75%      69.00
    max      97.00
    Name: winning_age, dtype: float64

Here's what the histogram looks like:

    plt.figure(figsize=(8, 4), dpi=200)
    sns.histplot(data=df_data,
                x=df_data.winning_age,
                bins=30)
    plt.xlabel('Age')
    plt.title('Distribution of Age on Receipt of Prize')
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_17-10-14-da5c8f344ae6c5029801d057b8fdc7da.png'>



### Challenge 4

Are Nobel laureates being nominated later in life than before? Have the ages of laureates at the time of the award increased or decreased over time?
- Use Seaborn to create a <a href='https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot'>.regplot</a> with a trendline.
- Set the `lowess` parameter to `True` to show a moving average of the linear fit.
- According to the best fit line, how old were Nobel laureates in the years 1900-1940 when they were awarded the prize?
- According to the best fit line, what age would it predict for a Nobel laureate in 2020?


The histogram above shows us the distribution across the entire dataset, over the entire time period. But perhaps the age has changed over time.

    plt.figure(figsize=(8,4), dpi=200)
    with sns.axes_style("whitegrid"):
        sns.regplot(data=df_data,
                    x='year',
                    y='winning_age',
                    lowess=True, 
                    scatter_kws = {'alpha': 0.4},
                    line_kws={'color': 'black'})
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_17-12-43-5144baca380dabc48a83b7f56107e44f.png'>

Using the lowess parameter allows us to plot a local linear regression. This means the best fit line is still linear, but it's more like a moving average which gives us a non-linear shape across the entire series. 
This is super neat because it clearly shows how the Nobel laureates are getting their award later and later in life. 
From 1900 to around 1950, the laureates were around 55 years old, but these days they are closer to 70 years old when they get their award! 
The other thing that we see in the chart is that in the last 10 years the spread has increased. We've had more very young and very old winners. 
In 1950s/60s winners were between 30 and 80 years old. Lately, that range has widened.


### Challenge 5

How does the age of laureates vary by category?
- Use Seaborn's <a href='https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot'>.boxplot()</a> to show how the mean, quartiles, max, and minimum values vary across categories. Which category has the longest "whiskers"?
- In which prize category are the average winners the oldest?
- In which prize category are the average winners the youngest?
- You can also use plotly to create the box plot if you like.

Seaborn allows us to create the above chart by category. But first, let's look at a box plot by category.

    plt.figure(figsize=(8,4), dpi=200)
    with sns.axes_style("whitegrid"):
        sns.boxplot(data=df_data,
                    x='category',
                    y='winning_age')
    
    plt.show()

The box plot shows us the mean, the quartiles, the maximum and the minimum values. 
It raises an interesting question: "Are peace prize winners really older than physics laureates?".

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_17-23-05-5e95226b748f8a0e7a4ce93dcfad6064.png'>


### Challenge 6

- Now use Seaborn's <a href='https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot'>.lmplot()</a> and the row parameter to create 6 separate charts for each prize category. Again set `lowess` to `True`.
- What are the winning age trends in each category?
- Which category has the age trending up and which category has the age trending down?
- Is this `.lmplot()` telling a different story from the `.boxplot()`?
- Create a third chart with Seaborn. This time use `.lmplot()` to put all 6 categories on the same chart using the `hue` parameter.

To get a more complete picture, we should look at how the age of winners has changed over time. The box plot above looked at the dataset as a whole.

    with sns.axes_style('whitegrid'):
        sns.lmplot(data=df_data,
                x='year', 
                y='winning_age',
                row = 'category',
                lowess=True, 
                aspect=2,
                scatter_kws = {'alpha': 0.6},
                line_kws = {'color': 'black'},)
    
    plt.show()

We see that winners in physics, chemistry, and medicine have gotten older over time. The ageing trend is strongest for physics. 
The average age used to be below 50, but now it's over 70. Economics, the newest category, is much more stable in comparison. 
The peace prize shows the opposite trend where winners are getting younger! As such, our scatter plots showing the best fit lines over time and our box plot of the entire dataset can tell very different stories!

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_17-31-22-d66b1a164a613c588b625f824fd37dfa.gif'>

To combine all these charts into the same chart, we can use the `hue` parameter

    with sns.axes_style("whitegrid"):
        sns.lmplot(data=df_data,
                x='year',
                y='winning_age',
                hue='category',
                lowess=True, 
                aspect=2,
                scatter_kws={'alpha': 0.5},
                line_kws={'linewidth': 5})
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-20_17-32-54-bd27d07d133eb4afa6b96be9fe335ed3.png'>


## 7. Learning Points & Summary

Today was a big and difficult project. Congratulations on making it all the way through! You too deserve a prize 🏅!


In this lesson, we reviewed many concepts that we've covered previously, including:
- How to uncover and investigate `NaN` values.
- How to convert objects and string data types to numbers.
- Creating donut and bar charts with plotly.
- Create a rolling average to smooth out time-series data and show a trend.
- How to use `.value_counts()`, `.groupby()`, `.merge()`, `.sort_values()` and `.agg()`.


In addition, we learned many new things too. We looked at how to:
- Create a Choropleth to display data on a map.
- Create bar charts showing different segments of the data with plotly.
- Create Sunburst charts with plotly.
- Use Seaborn's `.lmplot()` and show best-fit lines across multiple categories using the `row`, `hue`, and `lowess` parameters.
- Understand how a different picture emerges when looking at the same data in different ways (e.g., box plots vs a time series analysis).
- See the distribution of our data and visualise descriptive statistics with the help of a histogram in Seaborn.
