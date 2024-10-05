# Getting Started

The oldest programming language still in use today is FORTRAN, which was developed in 1957. Since then many other programming languages have been developed. 
But which programming language is the most popular? Which programming language is the Kim Kardashian of programming languages; the one people just can't stop talking about? 

**StackOverflow** will help us answer this burning question. Each post on Stack OverFlow comes with a `Tag`. And this `Tag` can be the name of a programming language.
To figure out which language is the most popular, all we need to do is `count` the number of `posts` on Stack Overflow that are tagged with each language. 
The language with the most posts wins!

## 1. Preliminary Data Exploration

I hope the last steps were fairly straightforward. First, we import pandas and then we can call `read_csv()`, where we can provide some additional arguments, like the names for our columns.

    df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)


Setting the `header` row to **0** allows us to substitute our own column names.

Next, we use `.head()` and `.tail()` to look at the first and last 5 rows. This allows us to verify that our column naming worked as intended.

To check the dimensions of the **DataFrame**, we use our old friend `.shape`.
To count the number of entries in each column we can use `.count()`. 
Note that `.count()` will actually tell us the number of non-`NaN` values in each column.


## 2. Data Cleaning: Working with Time Stamps

### Selecting an Individual Cell

Let's take a closer look at the `'DATE'` column in our **DataFrame**. We can use the double square bracket notation to look at the second entry in the column: 

    df['DATE'][1]

Alternatively, for column names no spaces, we can also use the dot-notation:

    df.DATE[1]

I prefer the square bracket notation for column names since it's more flexible, but with the dot notation, you get to use autocomplete, which is also nice.

### Inspecting the Data Type

When we `type` check the contents of this cell, we see that we are not dealing with a `date` object, but rather with a `string`.
This is not very handy. Not only will the string format always show the unnecessary 00:00:00, but we also don't get the benefit of working with `Datetime` objects, which know how to handle dates and times. 
**Pandas** can help us convert the `string` to a `timestamp` using the `to_datetime()` method.

Here's how we can convert the entry in our cell and check that it worked:

    print(pd.to_datetime(df.DATE[1]))
    type(pd.to_datetime(df.DATE[1]))

Let's use Pandas' `to_datetime()` to convert the entire `df['DATE']` column.

    df.DATE = pd.to_datetime(df.DATE)
    df.head()


## 3. Data Manipulation: Pivoting DataFrames

### The .pivot() method

Sometimes you want to convert your **DataFrame** so that each category has its own column. For example, suppose you needed to take the table below and create a separate column for each `actor`, where each row is the `Age` of the `actor`:

How would you do this with the DataFrame below? 

    test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                            'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                            'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
    test_df

The easiest way to accomplish this is by using the `.pivot()` method in **Pandas**. Try the example for yourself. 

The thing to understand is how to supply the correct arguments to get the desired outcome. 
The `index` are the categories for the `rows`. The `columns` are the categories for the `columns`. And the `values` are what you want in the new cells. 

    pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
    pivoted_df

However, there's one very important thing to notice. What happens if a value is missing? In the example above there's no value for old **Sylvester**. In this case, the `.pivot()` method will insert a `NaN` value.


### Challenge

Here's how you pivot our existing DataFrame to get the outcome above:

    reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
    reshaped_df.columns

    Index(['assembly', 'c', 'c#', 'c++', 'delphi', 'go', 'java', 'javascript',
        'perl', 'php', 'python', 'r', 'ruby', 'swift'],
        dtype='object', name='TAG')


    reshaped_df.head()
    reshaped_df.count()

    TAG
    assembly      193
    c             193
    c#            194
    c++           193
    delphi        193
    go            178
    java          193
    javascript    193
    perl          193
    php           193
    python        193
    r             191
    ruby          193
    swift         184
    dtype: int64


When we count the number of entries per column we see that not all languages are the same. 
The reason is that the `.count()` method excludes `NaN` values. 

When we pivoted the **DataFrame** the `NaN` values were inserted when there were no posts for a language in that month (e.g., `Swift` in `July, 2008`).


### Dealing with NaN Values


In this case, we don't want to drop the `rows` that have a `NaN` value. Instead, we want to substitute the number `0` for each `NaN` value in the **DataFrame**. 
We can do this with the `.fillna()` method.

    reshaped_df.fillna(0, inplace=True) 

The `inplace` argument means that we are updating `reshaped_df`. Without this argument we would have to write something like this:

    reshaped_df = reshaped_df.fillna(0) 

Let's check if we successfully replaced all the `NaN` values in our **DataFrame**.
We can also check if there are any `NaN` values left in the entire **DataFrame** with this line:

    reshaped_df.isna().values.any()

Here we are using the `.isna()` method that we've used before, but we're chaining two more things: the `values` attribute and the `any()` method. 

This means we don't have to search through the entire **DataFrame** to spot if `.isna()` is `True`.

Now we're all set to create some charts and visualize our data. 

Using `df.pivot_table `allows you to use some updated `arguments`. for instance, you can use

    reshaped_df = df.pivot_table(index='Date', columns='Tag', values='Posts', fill_value=0)

to fill in missing values, and returning `0` instead of `NaN`.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html


## 4. Data Visualisation with Matplotlib

### Matplotlib

To create our first charts we're going to use a library called **Matplotlib**. 

There are many different libraries in Python to help us create charts and graphs. 
`Matplotlib` is an incredibly popular one and it works beautifully in combination with `Pandas`, so let's check it out.

First, we have to import Matplotlib.

    import matplotlib.pyplot as plt

### Mini Challenge

You can actually show a line chart for the popularity of a programming language using only a single line of code. 
Can you use the `.plot()` documentation to figure out how to do this? 
Try and plot the popularity of the `Java` programming language. 

### Solution

All you need to do is supply the values for the **horizontal axis** (the x-values) and the **vertical axis** (the y-values) for the chart. 

The x-values are our `dates` and the y-values are the number of `posts`. We can supply these values to the .`plot()` function by position like so:

    plt.plot(reshaped_df.index, reshaped_df.java)

or like so if you prefer the square bracket notation.

    plt.plot(reshaped_df.index, reshaped_df['java'])

### Styling the Chart

Let's look at a couple of methods that will help us style our chart:
`.figure()` - allows us to resize our chart
`.xticks()` - configures our x-axis
`.yticks()` - configures our y-axis
`.xlabel()` - add text to the x-axis
`.ylabel()` - add text to the y-axis
`.ylim()`   - allows us to set a lower and upper bound

To make our chart larger we can provide a `width` (16) and a `height` (10) as the `figsize` of the figure.

    plt.figure(figsize=(16,10)) 
    plt.plot(reshaped_df.index, reshaped_df.java)

This will make our chart easier to see. But when we increase the `size` of the chart, we should also increase the `fontsize` of the `ticks` on our axes so that they remain easy to read:

    plt.figure(figsize=(16,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt. plot(reshaped_df.index, reshaped_df.java)

Now we can add `labels`. Also, we're never going to get less than `0` posts, so let's set a lower limit of 0 for the y-axis with `.ylim()`.

    plt.figure(figsize=(16,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Posts', fontsize=14)
    plt.ylim(0, 35000)

    plt. plot(reshaped_df.index, reshaped_df.java, reshaped_df.python)


### Show multiple lines on same graph for Java and Python


But what if we wanted to plot all the **programming languages** on the same chart? 
We don't want to type out `.plot()` a million times, right? We can actually just use a `for-loop`:

    for column in reshaped_df.columns:
        plt.plot(reshaped_df.index, reshaped_df[column])

This will allow us to iterate over each column in the DataFrame and plot it on our chart. 
The final result should look like this:

But wait, which language is which? It's really hard to make out without a `legend` that tells us which `color` corresponds to each `language`. 

Let's modify the plotting code to add a label for each line based on the column name (and make the lines thicker at the same time using `linewidth`). 
Then let's add a `legend` to our chart:


### Smoothing out Time-Series Data

Looking at our chart we see that time-series data can be quite noisy, with a lot of up and down spikes. 
This can sometimes make it difficult to see what's going on.

A useful technique to make a trend apparent is to smooth out the observations by taking an `average`. 

By averaging say, 6 or 12 observations we can construct something called the `rolling mean`. 

Essentially we calculate the average in a window of time and move it forward by one observation at a time.

Since this is such a common technique, **Pandas** actually two handy methods already built-in: `rolling()` and `mean()`. 

We can chain these two methods up to create a **DataFrame** made up of the averaged observations.

    # The window is number of observations that are averaged
    roll_df = reshaped_df.rolling(window=6).mean()
    
    plt.figure(figsize=(16,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Posts', fontsize=14)
    plt.ylim(0, 35000)
    
    # plot the roll_df instead
    for column in roll_df.columns:
        plt.plot(roll_df.index, roll_df[column], 
                linewidth=3, label=column)
    
    plt.legend(fontsize=14)


## 5. Learning Points & Summary


Congratulations on completing another challenging data science project! Today we've seen how to grab some raw data and create some interesting charts using **Pandas** and **Matplotlib**. 
We've: 
- used `.groupby()` to explore the number of posts and entries per programming language
- converted `strings` to `Datetime` objects with `to_datetime()` for easier plotting
- reshaped our `DataFrame` by converting categories to columns using `.pivot()`
- used `.count()` and `isna().values.any()` to look for `NaN` values in our DataF**rame, which we then replaced using `.fillna()`
- created (multiple) line charts using `.plot()` with a `for-loop`
- styled our charts by changing the `size`, the `labels`, and the `upper` and `lower` `bounds` of our `axis`.
- added a `legend` to tell apart which line is which by `color`
- smoothed out our time-series observations with `.rolling().mean()` and plotted them to better identify trends over time.
