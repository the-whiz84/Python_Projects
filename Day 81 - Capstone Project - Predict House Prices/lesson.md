# Day 81 - Machine Learning Capstone: House Price Prediction

This notebook is a capstone because it combines several ideas that used to appear separately: exploratory analysis, feature relationships, train/test splitting, linear regression, residual analysis, and model improvement through transformation of the target variable.

The project question is straightforward: can you estimate the value of a Boston home from its features? The useful part is not just training a model. It is learning how to inspect the model and decide whether it is behaving well.

## 1. Explore the Dataset Before Modeling

The notebook begins with a standard inspection pass:

```python
data = pd.read_csv('boston.csv', index_col=0)

data.shape
data.columns
data.head()
data.info()
print(f'Any NaN values? {data.isna().values.any()}')
print(f'Any duplicates? {data.duplicated().values.any()}')
```

That matters because regression is only useful when the feature table is trustworthy.

The first set of visualizations explores the target variable and the main feature relationships:

```python
sns.displot(data['PRICE'],
            bins=50,
            aspect=2,
            kde=True,
            color='#2196f3')
```

And then:

```python
sns.pairplot(data)

with sns.axes_style('darkgrid'):
    sns.jointplot(x=data.LSTAT,
                  y=data.PRICE,
                  height=7,
                  color='crimson',
                  joint_kws={'alpha': 0.5})
```

These plots do more than make the notebook look thorough. They help you spot skew, outliers, and strong relationships before you fit a model.

## 2. Split Features and Target the Right Way

The model uses `PRICE` as the target and everything else as features:

```python
target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=10)
```

This is the point where the notebook becomes a real machine-learning workflow rather than just a statistics exercise.

The split matters because you need a boundary between the data used to fit the model and the data used to evaluate it. Without that separation, performance numbers become far less trustworthy.

## 3. Fit the Linear Model and Inspect Residuals

Once the split is created, the notebook trains a linear regression model and compares predictions to actual values.

The most important visual checks come after fitting:

```python
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\\hat y_i$', fontsize=17)
```

And:

```python
plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
```

Residuals are where the notebook becomes educational instead of mechanical. A regression model is not only about getting an `r-squared` value. You also want to know:

- are predictions roughly aligned with actual values?
- do residuals fan out or cluster oddly?
- does the error distribution look reasonably centered?

That is why the notebook also plots the residual distribution:

```python
sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Residuals Skew ({resid_skew}) Mean ({resid_mean})')
```

## 4. Improve the Model by Transforming the Target

The notebook then makes a strong modeling move: it log-transforms the house prices.

```python
y_log = np.log(data['PRICE'])
sns.displot(y_log, kde=True)
plt.title(f'Log Prices. Skew is {y_log.skew():.3}')
```

That transformation matters because housing prices are often skewed. A linear model tends to behave better when the target is more symmetric.

The notebook retrains the model on log prices:

```python
new_target = np.log(data['PRICE'])
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features,
                                                            new_target,
                                                            test_size=0.2,
                                                            random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
```

Then it compares the residual behavior of the original and log-price models. This is one of the best habits in the notebook: do not stop at "the model trained." Compare whether the new specification is actually cleaner and more stable.

The final step turns the model into a valuation tool by building a `property_stats` row and predicting a price:

```python
log_estimate = log_regr.predict(property_stats)[0]
dollar_est = np.exp(log_estimate) * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')
```

That turns the notebook from an analysis project into an applied estimation model.

## How to Run the House Price Notebook

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open `Multivariable_Regression_and_Valuation_Model.ipynb`.
3. Run the notebook in order so the exploratory plots, train/test split, regression variables, and transformed targets build on each other correctly.
4. Verify the main checkpoints:
   - target distribution and feature relationships
   - `train_test_split()` output
   - actual vs predicted and residual plots
   - log-price model comparison
   - final property valuation example

## Summary

Today, you learned that a predictive model is only as useful as the diagnostics around it. You explored the Boston housing data, trained a multivariable regression model, checked the residual structure, improved the target distribution with a log transform, and turned the final model into a property valuation workflow.
