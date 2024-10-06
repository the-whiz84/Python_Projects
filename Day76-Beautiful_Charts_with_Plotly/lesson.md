# Google Play Store Analytics

## 1. Data Cleaning: Removing NaN Values and Duplicates

The first step as always is getting a better idea about what we're dealing with.

### Preliminary Data Exploration

**Challenge:** How many rows and columns does `df_apps` have? What are the column names? What does the data look like? 
Look at a random sample of 5 different rows with `.sample()`

**Solution**

Compared to the previous projects we are working with a fairly large DataFrame this time.

```
# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

df_apps = pd.read_csv('apps.csv')

df_apps.shape
(10841, 12)

df_apps.head()

df_apps.sample(5)
```

We can already see that there are some data issues that we need to fix. 
In the Ratings and Type columns there are `NaN` (Not a number values) and in the Price column we have dollar signs that will cause problems.

The `.sample(n)` method will give us n random rows. This is another handy way to inspect our **DataFrame**.

**Challenge:** Remove the columns called `Last_Updated` and `Android_Version` from the **DataFrame**. We will not use these columns.

**Challenge:** How many rows have a `NaN` value (not-a-number) in the `Rating` column? 
Create DataFrame called `df_apps_clean` that does not include these rows.

**Solution:** Dropping Unused Columns and Removing `NaN` Values

To remove the unwanted columns, we simply provide a list of the column names [`'Last_Updated'`, `‘Android_Ver'`] to the `.drop()` method. By setting `axis=1` we are specifying that we want to drop certain columns.

```
df_apps.drop(columns=['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
df_apps.head()
```

To find and remove the rows with the `NaN` values we can create a subset of the **DataFrame** based on where `.isna()` evaluates to `True`. We see that `NaN` values in `ratings` are associated with no reviews (and no installs). That makes sense.

We can drop the `NaN` values with `.dropna()`:

```
df_apps.Rating.isna()

0         True
1         True
2         True
3         True
4         True
         ...  
10836    False
10837    False
10838    False
10839    False
10840    False
Name: Rating, Length: 10841, dtype: bool

df_apps_clean = df_apps.dropna()
df_apps_clean.isna()
```

This leaves us with 9,367 entries in our DataFrame. But there may be other problems with the data too:

**Challenge:** Are there any duplicates in data? Check for duplicates using the `.duplicated()` function. 
How many entries can you find for the "`Instagram`" app? Use `.drop_duplicates()` to remove any duplicates from `df_apps_clean`.

**Solution:** Finding and Removing Duplicates

There are indeed duplicates in the data. We can show them using the `.duplicated()` method, which brings up 476 rows:

    df_apps_clean.duplicated()

    21       False
    28       False
    47       False
    82       False
    99       False
            ...  
    10836    False
    10837    False
    10838    False
    10839     True
    10840    False
    Length: 9367, dtype: bool

    duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
    print(duplicated_rows.shape)
    duplicated_rows.head()

We can actually check for an individual app like `‘Instagram’` by looking up all the entries with that name in the `App` column.

    df_apps_clean[df_apps_clean.App == "Instagram"].head()

So how do we get rid of duplicates? Can we simply call `.drop_duplicates()`?

    df_apps_clean = df_apps_clean.drop_duplicates()

Not really. If we do this without specifying how to identify duplicates, we see that 3 copies of `Instagram` are retained because they have a different number of `reviews`. 
We need to provide the `column names` that should be used in the comparison to identify duplicates. For example:

    df_apps_clean.drop_duplicates(subset='App', keep='first', inplace=True)

This leaves us with 8,199 entries after removing duplicates. Huzzah! 💪

### What else should I know about the data?

So we can see that 13 different features were originally scraped from the Google Play Store.
- Obviously, the data is just a sample out of all the Android apps. It doesn't include all Android apps of which there are millions.
- I’ll assume that the sample is representative of the App Store as a whole. This is not necessarily the case as, during the web scraping process, this sample was served up based on geographical location and user behavior of the person who scraped it - in our case Lavanya Gupta.
- The data was compiled around 2017/2018. The pricing data reflect the price in USD Dollars at the time of scraping. (developers can offer promotions and change their app’s pricing).
- I’ve converted the app’s size to a floating-point number in MBs. If data was missing, it has been replaced by the average size for that category.
- The installs are not the exact number of installs. If an app has 245,239 installs then Google will simply report an order of magnitude like 100,000+. I’ve removed the '+' and we’ll assume the exact number of installs in that column for simplicity.


## 2. Preliminary Exploration: The Highest Ratings, Most Reviews, and Largest Size

**Challenge:** Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?

**Challenge:** What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you think there could be a limit in place or can developers make apps as large as they please?

**Challenge:** Which apps have the highest number of reviews? Are there any paid apps among the top 50?

**Solution:** Preliminary Data Exploration

This challenge should have been fairly straightforward if you remembered to use the `.sort_values()` function.

    df_apps_clean.sort_values("Rating", ascending=False).head()

Only apps with very few reviews (and a low number on installs) have perfect 5 star ratings (most likely by friends and family).

    df_apps_clean.sort_values("Size_MBs", ascending=False).head()

Here we can clearly see that there seems to be an upper bound of 100 MB for the size of an app. 
A quick google search would also have revealed that this limit is imposed by the Google Play Store itself. 
It’s interesting to see that a number of apps actually hit that limit exactly.

    df_apps_clean.sort_values("Reviews", ascending=False).head(50)

If you look at the number of reviews, you can find the most popular apps on the Android App Store. These include the usual suspects: Facebook, WhatsApp, Instagram etc. 
What’s also notable is that the list of the top 50 most reviewed apps does not include a single paid app! 🤔


## 3. Data Visualization with **Plotly**: Create Pie and Donut Charts

All Android apps have a content rating like `“Everyone”` or `“Teen”` or `“Mature 17+”`. 
Let’s take a look at the distribution of the content ratings in our dataset and see how to visualize it with `plotly` - a popular data visualization library that you can use alongside or instead of `Matplotlib`.

First, we’ll count the number of occurrences of each rating with `.value_counts()`

    ratings = df_apps_clean.Content_Rating.value_counts()
    ratings

    Content_Rating
    Everyone           6619
    Teen                912
    Mature 17+          357
    Everyone 10+        305
    Adults only 18+       3
    Unrated               1
    Name: count, dtype: int64

The first step in creating charts with plotly is to import `plotly.express`. This is the fastest way to create a beautiful graphic with a minimal amount of code in **plotly**.

    import plotly.express as px

To create a pie chart we simply call `px.pie()` and then `.show()` the resulting figure. **Plotly** refers to all their figures, be they line charts, bar charts, or pie charts as `graph_objects`.

    fig = px.pie(labels=ratings.index, values=ratings.values)
    fig.show()

Let’s customize our pie chart. Looking at the <a href="https://plotly.com/python-api-reference/generated/plotly.express.pie.html">.pie() documentation </a> we see a number of parameters that we can set, like `title` or `names`.

If you’d like to configure other aspects of the chart, that you can’t see in the list of parameters, you can call a method called `.update_traces()`. 
In plotly lingo, `“traces”` refer to graphical marks on a figure. Think of “traces” as collections of attributes. 
Here we update the traces to change how the text is displayed.

    fig = px.pie(labels=ratings.index, values=ratings.values, title="Content Rating", names=ratings.index)
    fig.update_traces(textposition='outside', textinfo='percent+label')
    
    fig.show()

To create a donut 🍩 chart, we can simply add a value for the `hole` argument:


## 4. Numeric Type Conversions for the Installations & Price Data


**Challenge**
How many apps had over 1 billion (that's right - BILLION) installations? How many apps just had a single install?
- Check the datatype of the Installs column.
- Count the number of apps at each level of installations.
- Convert the number of installations (the Installs column) to a numeric data type. Hint: this is a 2-step process. You'll have to make sure you remove non-numeric characters first.

**Solution:** Data Cleaning & Converting Data to Numeric Types

To check the data types you can either use `.describe()` on the column or `.info()` on the DataFrame.
```
df_apps_clean.Installs.describe()

count          8197
unique           19
top       1,000,000
freq           1417
Name: Installs, dtype: object

df_apps_clean.info()

<class 'pandas.core.frame.DataFrame'>
Index: 8197 entries, 21 to 10835
Data columns (total 10 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   App             8197 non-null   object 
 1   Category        8197 non-null   object 
 2   Rating          8197 non-null   float64
 3   Reviews         8197 non-null   int64  
 4   Size_MBs        8197 non-null   float64
 5   Installs        8197 non-null   object 
 6   Type            8197 non-null   object 
 7   Price           8197 non-null   object 
 8   Content_Rating  8197 non-null   object 
 9   Genres          8197 non-null   object 
dtypes: float64(2), int64(1), object(7)
memory usage: 962.5+ KB
```

Both of these show that we are dealing with a non-numeric data type. In this case, the type is `"object"`.

If we take two of the columns, say `Installs` and the `App` name, we can count the number of entries per level of installations with `.groupby()` and `.count()`. 
However, because we are dealing with a non-numeric data type, the ordering is not helpful. 
The reason Python is not recognizing our installs as numbers is because of the comma `(,)` characters.

    df_apps_clean[['App', 'Installs']].groupby('Installs').count()

We can remove the comma (`,`) character - or any character for that matter - from a **DataFrame** using the string’s `.replace()` method. 
Here we’re saying: “replace the `,` with an empty string”. This completely removes all the commas in the `Installs` column. 
We can then convert our data to a number using `.to_numeric()`.

    df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
    df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
    df_apps_clean[['App', 'Installs']].groupby('Installs').count()

Let's examine the Price column more closely.

**Challenge**
Convert the `price` column to numeric data. Then investigate the top 20 most expensive apps in the dataset.

Remove all apps that cost more than $250 from the `df_apps_clean` DataFrame.

Add a column called '`Revenue_Estimate`' to the DataFrame. This column should hold the `price` of the app times the number of `installs`. 
What are the top 10 highest-grossing paid apps according to this estimate? Out of the top 10, how many are games?

**Solution:** Finding the most Expensive Apps and Filtering out the Junk

If you look at the data type of the price column:

    df_apps_clean.Price.describe()

You also see that is of type object. The reason is the dollar `$` signs that we’ve spotted before. 
To convert the price column to numeric data we use the `.replace()` method once again, but this time we filter out the dollar sign.

    df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
    df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
    
    df_apps_clean.sort_values('Price', ascending=False).head(20)

What’s going on here? There are 15 I am Rich Apps in the Google Play Store apparently. They all cost $300 or more, which is the main point of the app. 
The story goes that in 2008, Armin Heinrich released the very first I am Rich app in the iOS App Store for $999.90. 
The app does absolutely nothing. It just displays the picture of a gemstone and can be used to prove to your friends how rich you are. 
Armin actually made a total of 7 sales before the app was hastily removed by Apple. 
Nonetheless, it inspired a bunch of copycats on the Android App Store, but if you search today, you’ll find all of these apps have disappeared as well. 
The high installation numbers are likely gamed by making the app was available for free at some point to get reviews and appear more legitimate.

Leaving this bad data in our dataset will misrepresent our analysis of the most expensive 'real' apps. 
Here’s how we can remove these rows:

    df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
    df_apps_clean.sort_values('Price', ascending=False).head(5)

When we look at the top 5 apps now, we see that 4 out of 5 are medical apps.

We can work out the highest grossing paid apps now. All we need to do is multiply the values in the `price` and the `installs` column to get the number:

    df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
    df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]

This generously assumes of course that all the installs would have been made at the listed price, which is unlikely, as there are always promotions and free giveaways on the App Stores.

The top spot of the highest-grossing paid app goes to … **Minecraft** at close to **$70 million**. 
It’s quite interesting that Minecraft (along with Bloons and Card Wars) is actually listed in the Family category rather than in the Game category. 
If we include these titles, we see that 7 out the top 10 highest-grossing apps are games. 
The Google Play Store seems to be quite flexible with its category labels.


## 5. Plotly Bar Charts & Scatter Plots: The Most Competitive & Popular App Categories

If you were to release an app, would you choose to go after a competitive category with many other apps? 
Or would you target a popular category with a high number of downloads? Or perhaps you can target a category which is both popular but also one where the downloads are spread out among many different apps. 
That way, even if it’s more difficult to discover among all the other apps, your app has a better chance of getting installed, right? 
Let’s analyze this with bar charts and scatter plots and figure out which categories are dominating the market.

We can find the number of different categories like so:

    df_apps_clean.Category.nunique()

Which shows us that we there are 33 unique categories.

To calculate the number of apps per category we can use our old friend `.value_counts()`

    top10_category = df_apps_clean.Category.value_counts()[:10]
    top10_category
    
    Category
    FAMILY             1606
    GAME                910
    TOOLS               718
    PRODUCTIVITY        301
    PERSONALIZATION     298
    LIFESTYLE           297
    FINANCE             296
    MEDICAL             291
    PHOTOGRAPHY         263
    BUSINESS            262
    Name: count, dtype: int64

To visualize this data in a bar chart we can use the plotly express (our `px`) <a href="https://plotly.com/python-api-reference/generated/plotly.express.bar.html#plotly.express.bar"> bar()</a> function:

    bar = px.bar(x = top10_category.index, y = top10_category.values)
    
    bar.show()

Based on the number of apps, the `Family` and `Game` categories are the most competitive. 
Releasing yet another app into these categories will make it hard to get noticed.

But what if we look at it from a different perspective? What matters is not just the total number of apps in the category but how often apps are downloaded in that category. 
This will give us an idea of how popular a category is. 
First, we have to group all our apps by category and sum the number of installations:

    category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
    category_installs.sort_values('Installs', ascending=True, inplace=True)

Then we can create a horizontal bar chart, simply by adding the orientation parameter:

    h_bar = px.bar(x = category_installs.Installs,
                y = category_installs.index,
                orientation='h')
    
    h_bar.show()

We can also add a custom title and axis labels like so:

    h_bar = px.bar(x = category_installs.Installs,
                y = category_installs.index,
                orientation='h',
                title='Category Popularity')
    
    h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
    h_bar.show()

Now we see that `Games` and `Tools` are actually the most popular categories. If we plot the popularity of a category next to the number of apps in that category we can get an idea of how concentrated a category is. 
Do few apps have most of the downloads or are the downloads spread out over many apps?

**Challenge**

As a challenge, let’s use plotly to create a scatter plot that looks like this:

Create a **DataFrame** that has the number of `apps` in one column and the number of `installs` in another:

Then use the plotly express examples from the documentation alongside the `.scatter()` API reference to create scatter plot that looks like the chart above.

**Hint:** Use the `size`, `hover_name` and `color` parameters in `.scatter()`. To scale the y-axis, call `.update_layout()` and specify that the y-axis should be on a log-scale like so: `yaxis=dict(type='log')`


**Solution:** Create a scatter plot with Plotly

First, we need to work out the number of apps in each category (similar to what we did previously).

    cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})

Then we can use `.merge()` and combine the two DataFrames.

    cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
    print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
    cat_merged_df.sort_values('Installs', ascending=False)

Now we can create the chart. Note that we can pass in an entire DataFrame and specify which columns should be used for the x and y by column name.

    scatter = px.scatter(data_frame=cat_merged_df, # data
                        x='App', # column name
                        y='Installs',
                        title='Category Concentration',
                        size='App',
                        hover_name=cat_merged_df.index,
                        color='Installs')
    
    scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                        yaxis_title="Installs",
                        yaxis=dict(type='log'))
    
    scatter.show()

What we see is that the categories like `Family`, `Tools`, and `Game` have many different apps sharing a high number of downloads. 
But for the categories like `video players` and `entertainment`, all the downloads are concentrated in very few apps.


## 6. Extracting Nested Column Data using `.stack()`

Let’s turn our attention to the `Genres` column. This is quite similar to the categories column but more granular.

**Challenge**
How many different types of genres are there? Can an app belong to more than one genre? 
Check what happens when you use `.value_counts()` on a column with nested values? 
See if you can work around this problem by using the `.split()` function and the DataFrame's `.stack()` method.

**Solution:** Working with Nested Column Data

If we look at the number of unique values in the `Genres` column we get 114. But this is not accurate if we have nested data like we do here. 
We can see this using `.value_counts()` and looking at the values that just have a single entry. 
There we see that the semi-colon (;) separates the genre names.

    # Number of Genres?
    len(df_apps_clean.Genres.unique ())
    114

    # Problem: Have multiple categories separated by ;
    df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5]

    Genres
    Lifestyle;Pretend Play      1
    Strategy;Education          1
    Adventure;Education         1
    Role Playing;Brain Games    1
    Tools;Education             1
    Name: count, dtype: int64

We somehow need to separate the genre names to get a clear picture. This is where the string’s `.split()` method comes in handy. 
After we’ve separated our genre names based on the semi-colon, we can add them all into a single column with `.stack()` and then use `.value_counts()`.

    # Split the strings on the semi-colon and then .stack them.
    stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
    print(f'We now have a single column with shape: {stack.shape}')
    num_genres = stack.value_counts()
    print(f'Number of genres: {len(num_genres)}')

    We now have a single column with shape: (8562,)
    Number of genres: 53

**Challenge**
Can you create this chart with the Series containing the genre data?
Generated using the named color scale: "Agsunset"

Try experimenting with the built-in `colour` scales in Plotly. You can find a full list <a href="https://plotly.com/python/builtin-colorscales/"> here</a>.
- Find a way to set the colour scale using the `color_continuous_scale` parameter.
- Find a way to make the colour axis disappear by using `coloraxis_showscale`.

**Solution:** Working with Colour Scales in Plotly

    bar = px.bar(x = num_genres.index[:15], # index = category name
                y = num_genres.values[:15], # count
                title='Top Genres',
                hover_name=num_genres.index[:15],
                color=num_genres.values[:15],
                color_continuous_scale='Agsunset')
    
    bar.update_layout(xaxis_title='Genre', yaxis_title='Number of Apps', coloraxis_showscale=False)
    
    bar.show()


## 7. Grouped Bar Charts and Box Plots with Plotly

Now that we’ve looked at the total number of apps per category and the total number of apps per genre, let’s see what the split is between free and paid apps.

    df_apps_clean.Type.value_counts()

    Type
    Free    7593
    Paid     589
    Name: count, dtype: int64

We see that the majority of apps are free on the Google Play Store. But perhaps some categories have more paid apps than others. 
Let’s investigate. We can group our data first by Category and then by Type. 
Then we can add up the number of apps per each type. Using `as_index=False` we push all the data into columns rather than end up with our Categories as the index.

    df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
    df_free_vs_paid.head()

Unsurprisingly the biggest categories have the most paid apps. 
However, there might be some patterns if we put the numbers of a graph!

**Challenge**

Use the plotly express bar chart examples and the `.bar()` API reference to create this bar chart:

You'll want to use the `df_free_vs_paid` DataFrame that you created above that has the total number of free and paid apps per category.

See if you can figure out how to get the look above by changing the `categoryorder` to `'total descending'` as outlined in the documentation <a href="https://plotly.com/python/categorical-axes/#automatically-sorting-categories-by-name-or-total-value"> here</a>.

**Solution:** Contrasting Free vs. Paid Apps per Category

The key is using the `color` and `barmode` parameters for the `.bar()` method. To get a particular order, you can pass a dictionary to the axis parameter in `.update_layout()`.

    g_bar = px.bar(data_frame=df_free_vs_paid,
                x='Category',
                y='App',
                title='Free vs Paid Apps by Category',
                color='Type',
                barmode='group')
    
    g_bar.update_layout(xaxis_title='Category',
                        yaxis_title='Number of Apps',
                        xaxis={'categoryorder':'total descending'},
                        yaxis=dict(type='log'))
    
    g_bar.show()

What we see is that while there are very few paid apps on the Google Play Store, some categories have relatively more paid apps than others, including `Personalization`, `Medical` and `Weather`. 
So, depending on the category you are targeting, it might make sense to release a paid-for app.

But this leads to many more questions:
- How much should you charge? What are other apps charging in that category?
- How much revenue could you make?
- And how many downloads are you potentially giving up because your app is paid?

Let’s try and answer these questions with some Box plots. 
Box plots show us some handy descriptive statistics in a graph - things like the median value, the maximum value, the minimum value, and some quartiles. 

**Challenge**
Create a box plot that shows the number of Installs for free versus paid apps. 
How does the median number of installations compare? Is the difference large or small?

Use the <a href="https://plotly.com/python/box-plots/"> Box Plots Guide</a> and the <a href="https://plotly.com/python-api-reference/generated/plotly.express.box.html">.box API reference</a> to create the chart above.


**Solution:** Create Box Plots for the Number of Installs

From the hover text in the chart, we see that the median number of downloads for free apps is 500,000, while the median number of downloads for paid apps is around 5,000! This is massively lower.

    box = px.box(df_apps_clean,
                y='Installs',
                x='Type',
                color='Type',
                notched=True,
                points='all',
                title='How Many Downloads are Paid Apps Giving Up?')
    
    box.update_layout(yaxis=dict(type='log'))
    
    box.show()

But does this mean we should give up on selling a paid app? Let’s see how much revenue we would estimate per category.

**Challenge**
See if you can generate the chart below:


Looking at the hover text, how much does the median app earn in the Tools category? 
If developing an Android app costs $30,000 or thereabouts, does the average photography app recoup its development costs?

**Hint**: I've used 'min ascending' to sort the categories.


**Solution:** App Revenue by Category

If an Android app costs **$30,000** to develop, then the average app in very few categories would cover that development cost. 
The median paid photography app earned about $20,000. Many more app’s revenues were even lower - meaning they would need other sources of revenue like advertising or in-app purchases to make up for their development costs. 
However, certain app categories seem to contain a large number of outliers that have much higher (estimated) revenue - for example in `Medical`, `Personalization`, `Tools`, `Game`, and `Family`.

So, if you were to list a paid app, how should you price it? To help you decide we can look at how your competitors in the same category price their apps.

**Challenge**

What is the median price for a paid app? Then compare pricing by category by creating another box plot. 
But this time examine the prices (instead of the revenue estimates) of the paid apps. I recommend using `{categoryorder':'max descending'}` to sort the categories.

**Solution:** App Pricing by Category

The median price for an Android app is $2.99.

    df_paid_apps.Price.median()

However, some categories have higher median prices than others. This time we see that `Medical` apps have the most expensive apps as well as a median price of $5.49. 
In contrast, `Personalization` apps are quite cheap on average at $1.49. 
Other categories which higher median prices are `Business` ($4.99) and `Dating` ($6.99). 
It seems like customers who shop in these categories are not so concerned about paying a bit extra for their apps.


## 8. Learning Points & Summary

In this lesson we looked at how to:
- Pull a random sample from a **DataFrame** using `.sample()`
- How to find duplicate entries with `.duplicated()` and `.drop_duplicates()`
- How to convert `string` and `object` data types into numbers with `.to_numeric()`
- How to use `plotly` to generate beautiful pie, donut, and bar charts as well as box and scatter plots

Well done on completing today's lessons! 👏👏👏 I hope you enjoyed today’s Google Play Store analysis. It's incredible how much more of a clear picture we can get about the app ecosystem just by looking into some scraped website data for the Google Play Store.
