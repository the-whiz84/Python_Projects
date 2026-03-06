# Day 80 - Statistical Testing, Distributions, and Inference

Today, the notebook moves from descriptive analysis to evidence. The Semmelweis dataset is still a data-visualization project on the surface, but it introduces a deeper question: when the death rate drops after handwashing is introduced, is that just a visual pattern or is it strong enough to support an actual statistical claim?

That is why this lesson matters. It connects plotting, distributions, and hypothesis testing in one workflow.

## 1. Measure the Death Rate Before You Try to Explain It

The notebook starts with two tables:

```python
df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
df_monthly = pd.read_csv('monthly_deaths.csv', parse_dates=['date'])
```

The yearly table is useful for comparing clinics. The monthly table is useful for looking at change over time around the handwashing intervention.

The notebook quickly converts raw counts into a more meaningful metric:

```python
death_perc = df_yearly.deaths / df_yearly.births * 100

df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births
```

That is a crucial move. Raw deaths alone are not enough because the number of births changes too. A death rate is what lets you compare one clinic or one month fairly against another.

## 2. Use Time-Series Charts to See the Intervention

The yearly charts show that clinic 1 and clinic 2 behave very differently, especially once you compare death proportions rather than only birth counts.

```python
line = px.line(df_yearly,
               x='year',
               y='pct_deaths',
               color='clinic',
               title='Proportion of Yearly Deaths by Clinic')

line.show()
```

The monthly table then becomes the more important one, because it lets the notebook draw a line at the exact point where handwashing became mandatory:

```python
handwashing_start = pd.to_datetime('1847-06-01')

df_monthly['pct_deaths'] = df_monthly.deaths / df_monthly.births
before_soap = df_monthly[df_monthly.date < handwashing_start]
after_soap = df_monthly[df_monthly.date >= handwashing_start]
```

That split turns one timeline into a natural before-and-after experiment. The notebook then plots those two periods with a rolling average to make the shift visible:

```python
moving_average_line, = plt.plot(roll_df.index,
                                roll_df.pct_deaths,
                                color='crimson',
                                linewidth=3,
                                linestyle='--',
                                label='6m Moving Average')
```

This is a good use of smoothing. The raw monthly points still matter, but the rolling line makes the direction of change much easier to read.

## 3. Compare Distributions, Not Just Averages

The notebook does compute average death rates before and after handwashing:

```python
avg_prob_before = before_soap.pct_deaths.mean() * 100
avg_prob_after = after_soap.pct_deaths.mean() * 100

mean_diff = avg_prob_before - avg_prob_after
times = avg_prob_before / avg_prob_after
```

That gives you the headline result: the monthly death proportion drops sharply after the intervention.

But averages are only one part of the story. The notebook also looks at the shape of the two distributions using box plots, histograms, and kernel density estimates:

```python
box = px.box(df_monthly,
             x='washing_hands',
             y='pct_deaths',
             color='washing_hands',
             title='How Have the Stats Changed with Handwashing?')

hist = px.histogram(df_monthly,
                    x='pct_deaths',
                    color='washing_hands',
                    nbins=30,
                    opacity=0.6,
                    barmode='overlay',
                    histnorm='percent',
                    marginal='box')
```

This is where the notebook becomes more than a charting exercise. It stops asking only "did the average change?" and starts asking "did the whole distribution shift?"

The KDE plots push that idea further:

```python
sns.kdeplot(before_soap.pct_deaths, fill=True, clip=(0,1))
sns.kdeplot(after_soap.pct_deaths, fill=True, clip=(0,1))
```

The `clip=(0,1)` part is a small but important detail. Death rates cannot go below zero, so the notebook prevents the smoothed distribution from suggesting impossible values.

## 4. Use a t-Test to Support the Claim

This is the statistical heart of the lesson:

```python
t_stat, p_value = stats.ttest_ind(a=before_soap.pct_deaths,
                                  b=after_soap.pct_deaths)
print(f'p-palue is {p_value:.10f}')
print(f't-statstic is {t_stat:.4}')
```

The independent-samples t-test asks whether the difference between the two groups is large enough relative to their variation that it is unlikely to have happened by chance alone.

In plain language:

- `t_stat` measures the strength and direction of the difference
- `p_value` measures how surprising that difference would be if there were really no effect

That is why this day matters so much. It turns a visible drop in the chart into a statistically supported conclusion.

## How to Run the Semmelweis Notebook

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open `Dr_Semmelweis_Handwashing_Discovery.ipynb`.
3. Run the notebook in order so the derived columns and `before_soap` / `after_soap` tables exist before the distribution and t-test cells.
4. Verify the main outcomes:
   - yearly clinic comparison
   - before/after handwashing split
   - distribution shift in the histograms and KDE plots
   - final `ttest_ind()` result

## Summary

Today, you learned that a persuasive chart is not the same as statistical evidence. You converted raw deaths into rates, separated the data into pre- and post-handwashing periods, compared the distributions, and used a t-test to support the conclusion that Semmelweis was seeing a real change rather than random fluctuation.
