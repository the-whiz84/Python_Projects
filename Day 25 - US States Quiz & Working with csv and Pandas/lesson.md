# Day 25 - CSV Data Processing with Pandas and Coordinate-Based Quiz UI
Day 25 teaches how to move from raw CSV files to DataFrame-driven logic, then use that data inside an interactive turtle quiz.

## What You Learn
- Reading CSV files with `pandas.read_csv(...)`.
- Converting DataFrame columns to Python lists for membership checks.
- Filtering DataFrames by conditions to retrieve row-level values.
- Writing computed results back to CSV files.
- Combining data logic with UI prompts in a game loop.

## Projects in This Day
- `main.py`: US states quiz over a blank map image using turtle + pandas.
- `main_working_with_csv_and_pandas.py`: pandas fundamentals and CSV output practice.
- `squirrel_main.py`: grouped counting by fur color and summary export.

## US States Quiz Flow (`main.py`)
1. Load `50_states.csv` into a DataFrame.
2. Ask the user for state names repeatedly.
3. If correct, locate that state’s `(x, y)` and write it on the map.
4. On `Exit`, compute missing states and write `states_to_learn.csv`.

```python
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

if answer_data in all_states:
    guessed_state = data[data["state"] == answer_data]
    state_xcor = int(guessed_state["x"].item())
    state_ycor = int(guessed_state["y"].item())
    quiz.add_state(answer_data, state_xcor, state_ycor)
```

## Data Aggregation Example (`squirrel_main.py`)

```python
data = pandas.read_csv("squirrel_data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
```

This shows the core pandas pattern for Day 25: filter rows by condition, then aggregate.

## Common Pitfalls
- State matching fails because of casing/spaces: normalize input (`.title()` is already used here).
- `.item()` errors when multiple/no rows are returned: validate filters before extracting scalar values.
- CSV paths fail when run from another folder: execute scripts from the Day 25 directory.

## Run
```bash
python "main.py"
# data practice scripts
python "main_working_with_csv_and_pandas.py"
python "squirrel_main.py"
```
