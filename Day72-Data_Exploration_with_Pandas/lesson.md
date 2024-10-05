## 1. Getting Set Up for Data Science

### Introducing the **Google Colab Notebook**

**PyCharm** is a fantastic **IDE**, but when we're exploring and visualizing a dataset, you'll find the **Python notebook** format better suited.

Open your first Google Colab Notebook in through your Google Drive. You can find the Python Notebook under New → More → Google Colaboratory

### The alternative for VsCode is the **Jupyter Extension** by Microsoft


## How to use a Python Notebook

The **notebook** is divided into **cells**. Each **cell** can be executed individually and the result is automatically printed out below. 
To execute a **cell** use the shortcut **Shift + Enter**.

Then import `pandas` into your **notebook** and read the **.csv** file. 

    import pandas as pd
    df = pd.read_csv('salaries_by_college_major.csv')


## 2. Preliminary Data Exploration and Data Cleaning with Pandas

Now that we've got our data loaded into our **DataDrame**, we need to take a closer look at it to help us understand what it is we are working with. 
This is always the first step with any data science project. 

Let's see if we can answer the following questions: 
- How many rows does our dataframe have? 
- How many columns does it have?
- What are the labels for the columns? Do the columns have names?
- Are there any missing values in our dataframe? Does our dataframe contain any bad data?


We've already used the `.head()` method to peek at the top 5 rows of our **dataframe**. To see the number of **rows** and **columns** we can use the `shape` attribute:

    df.shape
    (51, 6)

Do you see 51 rows and 6 columns printed out below the cell? 

We saw that each column had a `name`. We can access the column `names` directly with the `columns` attribute.

    df.columns

    Index([ 'Undergraduate Major', 'Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary', 'Mid-Career 90th Percentile Salary', 'Group'],
    dtype='object')


### Missing Values and Junk Data

Before we can proceed with our analysis we should try and figure out if there are any missing or junk data in our **dataframe**. 

That way we can avoid problems later on. In this case, we're going to look for `NaN` (Not A Number) values in our **dataframe**. 

`NaN` values are blank cells or cells that contain `strings` instead of `numbers`. Use the `.isna()` method and see if you can spot if there's a problem somewhere.

    df.isna()

Did you find anything? Check the last couple of rows in the dataframe:

    df.tail()

Aha! We have a row that contains some information regarding the source of the data with blank values for all the other other columns.

    50 Source: PayScale Inc.    NaN NaN NaN NaN

### Delete the Last Row

We don't want this `row` in our `dataframe`. There's two ways you can go about removing this row. 

The first way is to manually remove the `row` at `index` 50. The second way is to simply use the `.dropna()` method from `pandas`. 

Let's create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row:

    clean_df = df.dropna()
    clean_df.tail()


## 3. Accessing Columns and Individual Cells in a Dataframe

Find `College Major` with `Highest Starting Salaries`

To access a particular `column` from a data frame we can use the `square bracket` notation, like so:

    clean_df['Starting Median Salary']

You should see all the values printed out below the cell for just this column:

    0     46000.0
    1     57700.0
    2     42600.0
    3     36800.0
    4     41600.0
    5     35800.0
    ....
    45    40800.0
    46    35900.0
    47    34100.0
    48    36500.0
    49    34000.0
    Name: Starting Median Salary, dtype: float64

To find the highest starting salary we can simply chain the `.max()` method.

    clean_df['Starting Median Salary'].max()
    np.float64(74300.0)

The highest starting salary is **$74,300**. But which college major earns this much on average? 

For this, we need to know the row number or `index` so that we can look up the `name` of the major.

Lucky for us, the `.idxmax()` method will give us `index` for the `row` with the largest `value`.

    clean_df['Starting Median Salary'].idxmax()
    np.int64(43)

which is **43**. To see the `name` of the major that corresponds to that particular `row`, we can use the `.loc` (location) property.

    clean_df['Undergraduate Major'].loc[43]
    'Physician Assistant'

Here we are selecting both a column (`'Undergraduate Major'`) and a row at `index` 43, so we are retrieving the value of a particular cell. 

You might see people using the double square brackets notation to achieve exactly the same thing: 

    clean_df['Undergraduate Major'][43]

If you don't specify a particular column you can use the `.loc` property to retrieve an entire row:

    clean_df.loc[43]

    Undergraduate Major                  Physician Assistant
    Starting Median Salary                           74300.0
    Mid-Career Median Salary                         91700.0
    Mid-Career 10th Percentile Salary                66400.0
    Mid-Career 90th Percentile Salary               124000.0
    Group                                               STEM
    Name: 43, dtype: object


### Challenge

### The Highest Mid-Career Salary

    print(clean_df['Mid-Career Median Salary'].max())
    print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
    clean_df['Undergraduate Major'][8]

If you have multiple lines in the same cell, only the last one will get printed as an output automatically.

If you'd like to see more than one thing printed out, then you still have to use a `print` statement on the lines above.


### The Lowest Starting and Mid-Career Salary

    print(clean_df['Starting Median Salary'].min())
    clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

Here I've **nested** the code that we've seen in the previous lesson in the same line. We can also use the `.loc` property to access an entire `row`. 

Below I've accessed the `row` at the `index` of the smallest mid-career salary:

    clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

Sadly, `education` is actually the degree with the lowest mid-career salary and `Spanish` is the major with the lowest starting salary.


## 4. Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk

### Lowest Risk Majors

A **low-risk major** is a degree where there is a small difference between the lowest and highest salaries.

In other words, if the difference between the **10th percentile** and the **90th percentile** earnings of your major is small, then you can be more certain about your salary after you graduate.

How would we calculate the difference between the earnings of the 10th and 90th percentile? Well, **Pandas** allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:

    clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

    0     109800.0
    1      96700.0
    2     113700.0
    3     104200.0
    4      85400.0
    ....
    42    132500.0
    43     57600.0
    44    122000.0
    45    126800.0
    46     95400.0
    47     66700.0
    48     87300.0
    49     65400.0
    dtype: float64

Alternatively, you can also use the `.subtract()` method.

    clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

The output of this computation will be another **Pandas dataframe** column. We can add this to our existing dataframe with the `.insert()` method:

    spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
    clean_df.insert(1, 'Spread', spread_col)
    clean_df.head()

The first argument is the position of where the column should be inserted. In our case, it's at position 1, so the second column.


### Sorting by the Lowest Spread


To see which degrees have the smallest `spread`, we can use the `.sort_values()` method. 

And since we are interested in only seeing the **name** of the degree and the **major**, we can pass a `list` of these two column names to look at the `.head()` of these two columns exclusively.

    low_risk = clean_df.sort_values('Spread')
    low_risk[['Undergraduate Major', 'Spread']].head()

Does `.sort_values()` sort in `ascending` or `descending` order? To find out, check out the **Pandas** documentation: 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

You can also bring up the quick documentation with **shift + tab** on your keyboard directly in the Python notebook.

### Challenge

### Majors with the Highest Potential

    highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
    highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()


### Majors with the Greatest Spread in Salaries

    highest_spread = clean_df.sort_values('Spread', ascending=False)
    highest_spread[['Undergraduate Major', 'Spread']].head()

Notice how 3 of the top 5 are present in both. This means that there are some very high earning `Economics` degree holders out there, but also some who are not earning as much. 

It's actually quite interesting to compare these two rankings versus the degrees where the median salary is very high.


## 5. Grouping and Pivoting Data with Pandas


Often times you will want to `sum` rows that belong to a particular category. For example, which category of degrees has the highest average salary? 

Is it `STEM`, `Business` or `HASS` (Humanities, Arts, and Social Science)? 

To answer this question we need to learn to use the `.groupby()` method. This allows us to manipulate data similar to a **Microsoft Excel Pivot Table**.

We have three categories in the `'Group'` column: `STEM`, `HASS` and `Business`. Let's `count` how many majors we have in each category:

    clean_df.groupby('Group').count()


Now can you use the `.mean()` method to find the average salary by group? 

    clean_df.groupby('Group').mean()

#This works in Google Collab but not in VsCode
#Alternative solution is

    clean_df.groupby('Group')[list(clean_df.select_dtypes('number'))].mean()


### Number formats in the Output


The above is a little hard to read, isn't it? We can tell **Pandas** to `print` the numbers in our notebook to look like **1,012.45** with the following line:

    pd.options.display.float_format = '{:,.2f}'.format

Ah, that's better, isn't it?


## 6. Learning Points & Summary

Today's Learning Points
- Use `.head()`, `.tail()`, `.shape` and `.columns` to explore your **DataFrame** and find out the number of `rows` and `columns` as well as the column `names`
- Look for `NaN` (not a number) values with `.findna()` and consider using `.dropna()` to clean up your **DataFrame**
- You can access entire `columns` of a **DataFrame** using the square bracket notation: `df['column name']` or `df[['column name 1', 'column name 2', 'column name 3']]`
- You can access individual `cells` in a **DataFrame** by chaining square brackets `df['column name'][index]` or using `df['column name'].loc[index]`
- The largest and smallest `values`, as well as their `positions`, can be found with methods like `.max()`, `.min()`, `.idxmax()` and `.idxmin()`
- You can `sort` the **DataFrame** with `.sort_values()` and add new columns with `.insert()`
- To create an **Excel Style Pivot Table** by grouping entries that belong to a particular category use the `.groupby()` method
