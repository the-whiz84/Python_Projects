# Linear Regression and Data Visualization with Seaborn

In this lesson, we're going to be looking at movie budget and revenue data. 
This dataset is perfect for trying out some new tools like **scikit-learn** to run a linear regression and **seaborn**, a popular data visualization library built on top of Matplotlib. 


## 1. Explore and Clean the Data

As with any dataset, the first steps are going to be data exploration and data cleaning. We need to get a better understanding of what we're dealing with. 
Since you've gone through this process a number of times before on previous days, can you tackle the following challenges on your own? 

***Challenge 1***

Answer these questions about how the data is structured:
- How many rows and columns does the dataset contain?
- Are there any NaN values present?
- Are there any duplicate rows?
- What are the data types of the columns?

    data = pd.read_csv('cost_revenue_dirty.csv')

    print(data.shape)
    print(data.head())
    print(data.isna())
    print(data.duplicated(subset='Movie_Title'))
    data.dtypes

    (5391, 6)
   Rank Release_Date                     Movie_Title USD_Production_Budget  \
    0  5293     8/2/1915           The Birth of a Nation              $110,000   
    1  5140     5/9/1916                     Intolerance              $385,907   
    2  5230   12/24/1916    20,000 Leagues Under the Sea              $200,000   
    3  5299    9/17/1920  Over the Hill to the Poorhouse              $100,000   
    4  5222     1/1/1925                  The Big Parade              $245,000   

    USD_Worldwide_Gross USD_Domestic_Gross  
    0         $11,000,000        $10,000,000  
    1                  $0                 $0  
    2          $8,000,000         $8,000,000  
    3          $3,000,000         $3,000,000  
    4         $22,000,000        $11,000,000  

    Rank                      int64
    Release_Date             object
    Movie_Title              object
    USD_Production_Budget    object
    USD_Worldwide_Gross      object
    USD_Domestic_Gross       object
    dtype: object

With any new dataset, it's a good idea to do some standard checks and conversions. 
I typically always first look at `.shape`, `.head()`, `.tail()`, `.info()` and `.sample()`.  Here's what I'm spotting already:

<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-14_14-46-28-63dd3d1025bbcd51f2effa33132c48f0.png">

There are thousands of entries in the DataFrame - one entry for each movie. We'll have some challenges formatting the data before we can do more analysis because we have non-numeric characters in our budget and revenue columns.

We can check for `NaN` values with this line:

    data.isna().values.any()

And check for duplicates with this line:

    data.duplicated().values.any()

We can see the total number of duplicates by creating a subset and looking at the length of that subset:

    duplicated_rows = data[data.duplicated()]
    len(duplicated_rows)

The fact that there are no duplicates or `NaN` (not-a-number) values in the dataset will make our job easier. 
We can also see if there are null values in `.info()`, which also shows us that we need to do some type conversion.


**Challenge 2**

Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`.

Note that domestic in this context refers to the United States.

    data.USD_Production_Budget = data.USD_Production_Budget.astype(str).str.replace('$', "")
    data.USD_Production_Budget = data.USD_Production_Budget.astype(str).str.replace(',', "")
    data.USD_Production_Budget = pd.to_numeric(data.USD_Production_Budget)

    data.USD_Worldwide_Gross = data.USD_Worldwide_Gross.astype(str).str.replace('$', "")
    data.USD_Worldwide_Gross = data.USD_Worldwide_Gross.astype(str).str.replace(',', "")
    data.USD_Worldwide_Gross = pd.to_numeric(data.USD_Worldwide_Gross)

    data.USD_Domestic_Gross = data.USD_Domestic_Gross.astype(str).str.replace('$', "")
    data.USD_Domestic_Gross = data.USD_Domestic_Gross.astype(str).str.replace(',', "")
    data.USD_Domestic_Gross = pd.to_numeric(data.USD_Domestic_Gross)
    data.dtypes

    Rank                      int64
    Release_Date             object
    Movie_Title              object
    USD_Production_Budget     int64
    USD_Worldwide_Gross       int64
    USD_Domestic_Gross        int64
    dtype: object

In order to convert the data in the budget and revenue columns and remove all the non-numeric characters, we can use a nested for loop. 
We create two Python lists: the characters to remove and the column names. Inside the nested loop we can combine `.replace()` and `.to_numeric()` to achieve our goal.

    chars_to_remove = [',', '$']
    columns_to_clean = ['USD_Production_Budget', 
                        'USD_Worldwide_Gross',
                        'USD_Domestic_Gross']
    
    for col in columns_to_clean:
        for char in chars_to_remove:
            # Replace each character with an empty string
            data[col] = data[col].astype(str).str.replace(char, "")
        # Convert column to a numeric data type
        data[col] = pd.to_numeric(data[col])



**Challenge 3**

Convert the `Release_Date` column to a Pandas `Datetime` type.

    data.Release_Date = pd.to_datetime(data.Release_Date)
    data.dtypes

    Rank                              int64
    Release_Date             datetime64[ns]
    Movie_Title                      object
    USD_Production_Budget             int64
    USD_Worldwide_Gross               int64
    USD_Domestic_Gross                int64
    dtype: object

To convert the Release_Date column to a `DateTime` object, all we need to do is call the `to_datetime()` function.

    data.Release_Date = pd.to_datetime(data.Release_Date)

When we check `.info()` again we see that the columns now have the desired data type. This allows us to proceed with the next parts of our analysis.


## 2. Investigate the Films that had Zero Revenue

Now that we've done some legwork on cleaning our data, we can investigate our data set more thoroughly.


**Challenge 1**

- What is the average production budget of the films in the data set?
- What is the average worldwide gross revenue of films?
- What were the minimums for worldwide and domestic revenue?
- Are the bottom 25% of films actually profitable or do they lose money?
- What are the highest production budget and highest worldwide gross revenue of any film?
- How much revenue did the lowest and highest budget films make?

    data.describe()

We can answer many of the questions with a single command: `.describe()`.

    data.describe()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-14_17-25-22-50638b2907fc1a16098f440072858223.png'>

The average film costs about $32m to make and makes around 3x that (or ~$92m) in worldwide revenue. So that's encouraging.

But quite a lot of films lose money too. In fact, all the films in the bottom quartile lose money, since the average cost is $5 million and they only bring in $3.8m in worldwide revenue!

The minimum domestic and worldwide revenue is $0. That makes sense. If a film never gets screened or is cancelled, then this is the number we would expect to see here.

On the other hand, the highest production budget was $460,000,000 and the highest worldwide revenue was $2,923,706,026.00. $2.5 Billion revenue! Holy smokes.

So which film was the lowest budget film in the dataset?

    data[data.USD_Production_Budget == 1100]

I've ... never heard of this film. But it looks like a real money maker. It grossed $181,041 with a measly $1,100 budget. 
😮 Wow. Talk about return on investment!

And the highest budget film in the dataset is:

    data[data.USD_Production_Budget == 460000000]

Avatar: The Way of Water for the 2023 data set


**Challenge 2**

How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?

    zero_domestic = data[data.USD_Domestic_Gross == 0]
    print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
    zero_domestic.sort_values('USD_Production_Budget', ascending=False)

    Number of films that grossed $0 domestically 706

We see that there are 706 films in the dataset that had no revenue in the United States. 


**Challenge 3**

How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally (i.e., the biggest flops)?

    zero_worldwide = data[data.USD_Worldwide_Gross == 0]
    print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
    zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

    Number of films that grossed $0 worldwide 413

When we check worldwide revenue instead, we see that there are 413 films that made no money internationally. Once again, some of the films have not been released yet at the time the data was compiled. However, 706 versus 413. Why is there a difference? 

The reason is that some international films were never screened in the United States.


## 3. Filter on Multiple Conditions: International Films

So far, we've created subsets for our DataFrames based on a single condition. But what if we want to select our data based on more than one condition? 
For example, which films made money internationally (i.e., `data.USD_Worldwide_Gross != 0`), but had zero box office revenue in the United States (i.e., `data.USD_Domestic_Gross == 0`)? 

How would we create a filter for these two conditions? One approach is to use the `.loc[]` property combined with the <a href='https://docs.python.org/3.4/library/operator.html#mapping-operators-to-functions'>bitwise and</a> `&` operator.

    international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                  (data.USD_Worldwide_Gross != 0)]
    international_releases

Why does this work? Pandas is built on top of NumPy, which uses Python's `bitwise` operators. And these bitwise operators allow us to do comparisons on an element by element basis in both NumPy and Pandas! Here's an example: 

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-14_18-25-38-1acab27e5b6c677db5828de681d34cbe.png'>

However, we're also checking if the domestic revenue was zero and the worldwide revenue was not zero. 
Because the bitwise operator takes precedence, we need to include parentheses `()` around the comparisons we'd like to prioritize.

    international_releases = data.loc[(data.USD_Domestic_Gross == 0) & (data.USD_Worldwide_Gross != 0)]
    print(f'Number of international releases: {len(international_releases)}')
    international_releases.head()

    Number of international releases: 293

However, this is not the only technique we can use to make multiple comparisons.

**Challenge**
Use the Pandas <a href='https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html'>.query()</a> `function `to accomplish the same thing. 
Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States.

Hint: This time you'll have to use the `and` keyword.

    data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0').head()

In this case, we enclose the entire query inside a string.

    international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
    print(f'Number of international releases: {len(international_releases)}')
    international_releases.tail()

The column names are recognized and we see the following:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-14_18-34-38-3cdecd04820328d2020a3300f5bab57c.png'>


### Unreleased Films

Now we can turn our attention to films in the dataset that were not released at the time the data was collected. 
This is why films like **Singularity** and **Aquaman** had zero revenue.

**Challenge**
Identify which films were not released yet as of the time of data collection (May 1st, 2018).

How many films are included in the dataset that have not yet had a chance to be screened in the box office? 

Create another DataFrame called data_clean that does not include these films.

    unreleased_films = data.query('Release_Date >= @scrape_date')
    unreleased_films

There are a total of 7 unreleased films at the time of data collection included in the dataset. (5 for the 2023 csv)
From this point on, we'll work with another DataFrame called `data_clean` that does not include these films.

    data_clean = data.drop(unreleased_films.index)

**Bonus Challenge:** Films that Lost Money

Having removed the unreleased films entirely can you calculate the percentage of films that did not break even at the box office? 
We already saw that more than the bottom quartile of movies appears to lose money when we ran `.describe()`. 
However, what is the true percentage of films where the costs exceed the worldwide gross revenue? 

    lost_money = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
    print(f"Number of films that lost money: {len(lost_money)}")
    lost_money.head(10)

    Number of films that lost money: 2405

    lost_money.shape[0]/data_clean.shape[0]
    0.37542928504527007

Again, there are different ways you could have calculated this. For example, using the `.loc[]` property,

    money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
    len(money_losing)/len(data_clean)

or the `.query()` function

    money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
    money_losing.shape[0]/data_clean.shape[0]

In both cases, we see that a whopping 37.5% 😮 of films do not recoup their production budget at the box office. 
💸💸💸 Who knew that film finance could be so risky! 😬


## 4. Seaborn Data Visualization: Bubble Charts

We're now ready to visualize our data. Today I want to introduce you to another popular data visualization tool that you can use alongside plotly and Matplotlib: Seaborn. 
<a href='https://seaborn.pydata.org'>Seaborn</a> is built on top of Matplotlib and it makes creating certain visualizations very convenient.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-15_09-09-20-72497b72e13443b2cebd18af668ac37e.png'>

**Import Seaborn**

The first step is adding Seaborn to our notebook. By convention we'll use the name `sns`.

### Seaborn Scatter Plots

To create a `.scatterplot()`, all we need to do is supply our DataFrame and the column names that we'd like to see on our axes.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-15_09-13-55-0b4231f5cf7793d115a8aafa96f58d4e.png'>

That should look familiar. 😊 Because Seaborn is built on top of Matplotlib, we can dive into the Matplotlib layer anytime to configure our chart. 
For example, we can increase the size of our figure:

    plt.figure(figsize=(8,4), dpi=200)
    sns.scatterplot(data=data_clean, x='USD_Production_Budget', y='USD_Worldwide_Gross')
    plt.show()

And to style our chart we can simply configure the `Axes` object that is returned from `sns.scatterplot()`.

    plt.figure(figsize=(8,4), dpi=200)
    ax = sns.scatterplot(data=data_clean,
                        x='USD_Production_Budget', 
                        y='USD_Worldwide_Gross')
    
    ax.set(ylim=(0, 3000000000),
        xlim=(0, 470000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-15_09-21-28-2f57d90c5f1f97686b5c48b765b21051.png'>

Here we're diving into the Matplotb layer to set the limits on the axes and change the labels.

### From Scatter Plot to Bubble Chart

But the reason we're using Seaborn is because of the `hue` and `size` parameters that make it very easy to create a bubble chart. 
These parameters allow us to color the data and change their size according to one of the columns in our DataFrame.

    plt.figure(figsize=(8,4), dpi=200)
    ax = sns.scatterplot(data=data_clean,
                        x='USD_Production_Budget', 
                        y='USD_Worldwide_Gross',
                        hue='USD_Worldwide_Gross', # colour
                        size='USD_Worldwide_Gross',) # dot size
    
    ax.set(ylim=(0, 3000000000),
        xlim=(0, 470000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions',)
    
    plt.show()

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-15_09-28-08-831897dbfc869643665e710decb79e5f.png'>

Now our higher grossing movies are bigger and darker on our chart. That's super handy. 
But Seaborn offers a number of convenient styling options as well.

To set the styling on a single chart (as opposed to all the charts in the entire notebook) we can use Python's `with` keyword. 
We've seen `with` used already when it comes to opening files in previous lessons.

    plt.figure(figsize=(8,4), dpi=200)
    
    # set styling on a single chart
    with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data=data_clean,
                        x='USD_Production_Budget', 
                        y='USD_Worldwide_Gross',
                        hue='USD_Worldwide_Gross',
                        size='USD_Worldwide_Gross')
    
    ax.set(ylim=(0, 3000000000),
            xlim=(0, 470000000),
            ylabel='Revenue in $ billions',
            xlabel='Budget in $100 millions')

In addition to `'darkgrid'`, Seaborn has a number of <a href='https://python-graph-gallery.com/104-seaborn-themes/'>built-in themes</a>. so you can style your chart very quickly. Try out 'whitegrid', 'dark',  or 'ticks' for example.

**Challenge**
Now that you've seen how to create a beautiful bubble chart in Seaborn, it's time to create your own. 
Can you write the code to replicate this chart? Notice how we are actually representing THREE dimensions in this chart: the budget, the release date, and the worldwide revenue. This is what makes bubble charts so awesomely informative.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-15_09-44-00-eac16a0a1c99356a123eb410d99157ec.png'>

    plt.figure(figsize=(8,4), dpi=200)
    
    with sns.axes_style("darkgrid"):
        ax = sns.scatterplot(data=data_clean, 
                        x='Release_Date', 
                        y='USD_Production_Budget',
                        hue='USD_Worldwide_Gross',
                        size='USD_Worldwide_Gross',)
    
        ax.set(ylim=(0, 480000000),
            xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
            xlabel='Year',
            ylabel='Budget in $100 millions')

**Analysis**

What do we see here? What is this chart telling us? Well, first off, movie budgets have just exploded in the last 40 years or so. 
Up until the 1970s, the film industry appears to have been in an entirely different era. 
Budgets started growing fast from the 1980s onwards and continued to grow through the 2000s. 
Also, the industry has grown massively, producing many more films than before. The number of data points is so dense from 2000 onwards that they are overlapping.

## 5. Floor Division: A Trick to Convert Years to Decades

In our bubble charts, we've seen how massively the industry has changed over time, especially from the 1970s onwards. 
This makes me think it makes sense to separate our films out by decade. Here's what I'm after:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-15_10-07-36-6a3655edec46115548a0f09bbd8b1173.png'>

**Challenge**

Can you create a column in `data_clean` that has the decade of the movie release. For example, a film released in 1992 or 1999 should have 1990 in the `Decade` column.

Here is one approach that you can follow:
1. Create a <a href='https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html'>DatetimeIndex object</a> from the `Release_Date` column.
2. Grab all the years from the `DatetimeIndex` object using the `.year` property.
3. Use floor division `//` to convert the year data to the decades of the films.
4. Add the decades as a `Decade` column to the `data_clean` DataFrame.

    data_years = pd.DatetimeIndex(data=data_clean.Release_Date).year
    data_years

    Index([2022.0, 2019.0, 2011.0, 2015.0, 2023.0, 2015.0, 2018.0, 2007.0, 2017.0,
       2015.0,
       ...
       1993.0, 2004.0, 2006.0,    nan, 2022.0, 1999.0, 2005.0, 2015.0, 2005.0,
       2021.0],
      dtype='float64', name='Release_Date', length=6406)
    
    Changed in version 2.0.0: The various numeric date/time attributes (day, month, year etc.) now have dtype int32. Previously they had dtype int64.


To create a DatetimeIndex, we just call the constructor and provide our release date column as an argument to initialize the DatetimeIndex object. 
Then we can extract all the years from the DatetimeIndex.

    dt_index = pd.DatetimeIndex(data_clean.Release_Date)
    years = dt_index.year

Now, all we need to do is convert the years to decades. For that, we will use floor division (aka integer division). The difference to regular division is that the result is effectively rounded down.

    5.0 / 2
    # output: 2.5
    5.0 // 2
    # output: 2.0

In our case, we will use the floor division by 10 and then multiplication by 10 to convert the release year to the release decade:
<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_11-13-38-ea1ff36ff1f36d1b44616077685626e5.png'>

    decades = years//10*10
    data_clean['Decade'] = decades

**Challenge**
Create two new DataFrames: `old_films` and `new_films`
- old_films should include all the films before 1970 (up to and including 1969)
- new_films should include all the films from 1970 onwards
- How many of our films were released prior to 1970?
- What was the most expensive film made prior to 1970?

    old_films = data_clean[data_clean.Decade <= 1960]
    new_films = data_clean[data_clean.Decade > 1960]
    print(len(old_films))
    old_films.sort_values('USD_Production_Budget', ascending=False)

    167

The cut-off for our calculation is 1960 in the Decade column because this will still include 1969. 
When we inspect our `old_films` DataFrame we see that it only includes 167 films. As we saw in the bubble chart, the bulk of films in the dataset have been released in the last 30 years.

The most expensive film prior to 1970 was **Cleopatra**, with a production budget of $42 million. 
That's some serious 1960s money, and judging by the trailer, a lot of it went into extravagant costumes, set design, and plenty of extras. Impressive.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_11-40-07-75393a74422b12f0ccc714e15e3eafbe.png'>


## 6. Plotting Linear Regressions with Seaborn

Let's visualize the relationship between the movie budget and the worldwide revenue using linear regression. 
Seaborn makes this incredibly easy with the `.regplot()` function.

    sns.regplot(data=old_films, 
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross')

This creates a scatter plot and draws a linear regression line together with the confidence interval at the same time.

To style the chart further, we can once again, drop into the Matplotlib layer and supply keyword arguments as dictionaries. 
We can customize the scatter plot (e.g., by changing the transparency of the dots) and the regression line itself (e.g., by changing the color).

    plt.figure(figsize=(8,4), dpi=200)
    with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films, 
                x='USD_Production_Budget', 
                y='USD_Worldwide_Gross',
                scatter_kws = {'alpha': 0.4},
                line_kws = {'color': 'black'})

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_11-54-26-bf6d69797f23a0d34875a64c59e36720.png'>

What do we see here? Well, first off we can spot Cleopatra on the far right. But also, we see that many lower budget films made much more money! 
The relationship between the production budget and movie revenue is not very strong. 
Many points on the left are very far away for the line, so the line appears not to capture the relationship between budget and revenue very well at all!

But does the same hold true for the newer films?

**Challenge**
Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`.

Style the chart
- Put the chart on a 'darkgrid'.
- Set limits on the axes so that they don't show negative values.
- Label the axes on the plot "Revenue in $ billions" and "Budget in $ millions".
- Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).

Interpret the chart
- Do our data points for the new films align better or worse with the linear regression than for our older films?
- Roughly how much would a film with a budget of $150 million make according to the regression line?

    plt.figure(figsize=(8,4), dpi=200)
    with sns.axes_style("darkgrid"):
    ax = sns.regplot(data=new_films, 
                x='USD_Production_Budget', 
                y='USD_Worldwide_Gross',
                scatter_kws = {'alpha': 0.4, 'color': '#2f4b7c'},
                line_kws = {'color': '#ff7c43'})
    
    ax.set(ylim=(0, 3000000000),
            xlim=(0, 480000000),
            ylabel="Revenue in $ billions",
            xlabel='Budget in $100 millions'
            )

To style the chart we can use the same techniques as before: providing values for the `.regplot()` function, as well as making use of the Matplotlib Axes object to fine-tune the limits, labels, and general style.

How do we interpret our chart? This time we are getting a much better fit, compared to the old films. 
We can see this visually from the fact that our data points line up much better with our regression line (pun intended). 
Also, the confidence interval is much narrower. We also see that a film with a $150 million budget is predicted to make slightly under $500 million by our regression line.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_14-57-10-7c88b2c9af63e82477610c41a9fe6a4d.png'>

All in all, we can be pretty confident that there does indeed seem to be a relationship between a film's budget and that film's worldwide revenue.

But how much of the variation in revenue does the budget actually explain? And how much extra revenue can we expect for an additional $1 increase in the budget? To find out, we need to dive into the numbers underlying our regression model.


## 7. Use scikit-learn to Run Your Own Regression

Let's dive into our linear regression model a bit more. We are using a **univariate** regression. This is a regression with a single **explanatory variable** (our movie BUDGET). Explanatory variables are also referred to as **features** in machine learning terminology.

Using our data on budgets, the linear regression estimates the best possible line to fit our movie revenues. The regression line has the following structure:

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_15-19-24-b9cd86771c12cda554da251a16471df9.png'>

To find the best possible line, our regression will estimate the y-intercept ("theta zero") and the slope ("theta one"). 
The line's **intercept** on the y-axis tells us how much revenue a movie would make if the budget was 0. 
The **slope** tells us how much extra revenue we get for a $1 increase in the movie budget.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_15-31-02-3bdbeb669ce3d7ecebe72abb986e8d35.png'>

So how can we find out what our model's estimates are for theta-one and theta-zero? And how can we run our own regression, regardless of whether we want to visualize it on a chart? For that, we can use <a href='https://scikit-learn.org/stable/'>scikit-learn</a>.

**Import scikit-learn**

Let's add the `LinearRegression` from scikit-learn to our notebook

    from sklearn.linear_model import LinearRegression

Now we can run a <a href='https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html'>LinearRegression</a>. 
First, let's create a `LinearRegression` object that will do the work for us.

    regression = LinearRegression()

Now we should specify our features and our targets (i.e., our response variable).
 You will often see the features named capital `X` and the target named lower case `y`:

    # Explanatory Variable(s) or Feature(s)
    X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
    
    # Response Variable or Target
    y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 

Our `LinearRegression` does not like receiving Pandas `Series` (e.g., `new_films.USD_Production_Budget`), so I've created some new DataFrames here.

Now it's time to get to work and run the calculations:

    # Find the best-fit line
    regression.fit(X, y)

That's it. Now we can look at the values of theta-one and theta-zero from the equation above.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_16-11-16-2c2283cc96442b3c62e1c95e9eb31cde.png'>

    # Theta zero
    regression.intercept_
    array([-9085682.96234395])

    # Theta one
    regression.coef_
    array([[3.13920381]])

Both `intercept_` and `coef_` are simply attributes of the <a href='https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html'>LinearRegression object</a>. 
Don't worry about the underscores at the end, these are simply part of the attribute names that the scikit-learn developers have chosen.

How do we interpret the **y-intercept**? Literally, means that if a movie budget is $0, the estimated movie revenue is -$9.08 million. 
Hmm... so this is clearly unrealistic. Why would our model tell us such nonsense? 
Well, the reason is that we are specifying what the model should be ahead of time - namely a straight line - and then finding the best straight line for our data. 
Considering that you can't have negative revenue or a negative budget, we have to be careful about interpreting our very simple model too literally. 
After all, it's just an estimate and this estimate will be the most accurate on the chart where we have the most data points (rather than at the extreme left or right).

What about the **slope**? The slope tells us that for every extra $1 in the budget, movie revenue increases by $3.1. So, that's pretty interesting. 
That means the higher our budget, the higher our estimated revenue. If budgets are all that matter to make lots of money, then studio executives and film financiers should try and produce the biggest films possible, right? 
Maybe that's exactly why we've seen a massive increase in budgets over the past 30 years.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_16-23-44-7a1c656b072897f661cc8efdfca94144.png'>


### R-Squared: Goodness of Fit

One measure of figuring out how well our model fits our data is by looking at a metric called `r-squared`. This is a good number to look at in addition to eyeballing our charts.

    # R-squared
    regression.score(X, y)
    0.5432025166693195

We see that our r-squared comes in at around 0.543. This means that our model explains about 55% of the variance in movie revenue. 
That's actually pretty amazing, considering we've got the simplest possible model, with only one explanatory variable. 
The real world is super complex, so in many academic circles, if a researcher can build a simple model that explains over 50% or so of what is actually happening, then it's a pretty decent model.

Remember how we were quite skeptical about our regression looking at the chart for our `old_films`? 

**Challenge**
Run a linear regression for the old_films. 
Calculate the `intercept`, `slope` and `r-squared`. 
How much of the variance in movie revenue does the linear model explain in this case?

    X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
    y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
    regression.fit(X, y)

    regression.intercept_
    array([21052829.55937172])

    regression.coef_
    array([[1.79898327]])

    regression.score(X, y)
    0.03493501415879341

Running the numbers this time around, we can confirm just how inappropriate the **linear model** is for the pre-1970 films. 
We still see a positive relationship between budgets and revenue, since the **slope** (our theta-one) is 1.8, but the **r-squared** is very low.

This makes sense considering how poorly our data points aligned with our line earlier.

<img src='https://img-c.udemycdn.com/redactor/raw/2020-10-16_16-43-08-86be88ceaa656f3a0c07f04d3cf0dac7.png'>

**Challenge**
You've just estimated the intercept and slope for the Linear Regression model. 
Now we can use it to make a prediction! 
For example, how much global revenue does our model estimate for a film with a budget of $350 million?

For a $350 million budget film, our model predicts a worldwide revenue of around $600 million! 
You can calculate this as follows:

22821538 + 1.64771314 * 350000000
Or, using the regression object, you could also work it out like this:

    budget = 350000000
    revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
    revenue_estimate = round(revenue_estimate, -6)
    print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')

(The colon : and dot . in a print statement is quite handy for controlling the number of digits you'd like to show up in the output)


## 8. Learning Points & Summary

Today was a pretty packed lesson where we introduced a lot of new concepts. In this lesson we looked at how to:
- Use nested loops to remove unwanted characters from multiple columns
- Filter Pandas DataFrames based on multiple conditions using both `.loc[]` and `.query()`
- Create bubble charts using the **Seaborn** Library
- Style Seaborn charts using the pre-built styles and by modifying Matplotlib parameters
- Use floor division (i.e., integer division) to convert years to decades
- Use Seaborn to superimpose a **linear regression** over our data
- Make a judgement if our regression is good or bad based on how well the model fits our data and the **r-squared** metric
- Run regressions with **scikit-learn** and calculate the coefficients.
