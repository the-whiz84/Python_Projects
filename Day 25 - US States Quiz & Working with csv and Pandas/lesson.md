# Day 25 - CSV Data Processing with Pandas and Coordinate-Based Quiz UI

Today we're combining two things: reading real data from CSV files and displaying that data on a map. The US States Quiz shows a blank map of America, and you type in state names. When you guess correctly, the state name appears in the right location.

This is also the first day where we use Pandas, which is Python's most powerful library for working with tabular data.

## Reading CSV with Pandas

The old way to read a CSV was line-by-line with the `csv` module. Pandas makes it much easier:

```python
import pandas

data = pandas.read_csv("50_states.csv")
```

That one line loads the entire file into a DataFrame, which is like a programmable spreadsheet. Each column becomes accessible by name:

```python
all_states = data["state"].to_list()
```

Now we have a plain Python list of all 50 state names.

## Finding coordinates for a specific state

The magic happens when you want the X and Y coordinates for, say, Texas. You filter the DataFrame to find that row, then pull out the specific columns:

```python
guessed_state = data[data["state"] == answer_data]
state_xcor = int(guessed_state["x"].item())
state_ycor = int(guessed_state["y"].item())
```

The expression `data["state"] == answer_data` returns a filtered DataFrame containing only the row where the state matches. Then `.item()` pulls the single value out of that cell.

## The quiz loop

The main loop in `main.py` keeps asking until you've guessed all 50 states or type Exit:

```python
while len(guessed_states) < 50:
    answer_data = screen.textinput(title=f"{quiz.score}/50 States Guessed", prompt="What's another state's name? ").title()
    if answer_data == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break
    if answer_data in all_states:
        guessed_state = data[data["state"] == answer_data]
        state_xcor = int(guessed_state["x"].item())
        state_ycor = int(guessed_state["y"].item())
        quiz.add_state(answer_data, state_xcor, state_ycor)
        guessed_states.append(answer_data)
        quiz.increase_score()
```

If the user types Exit, we use a list comprehension to find which states they haven't guessed yet, then save those to a CSV file so they can practice later.

## Why Pandas matters

Pandas lets you work with data at scale. In the squirrel example from this folder, we count how many squirrels of each fur color exist:

```python
data = pandas.read_csv("squirrel_data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
```

That's the same filtering pattern—select rows where a column matches a value, then count or operate on the result.

## Try it yourself

```bash
python "main.py"
```

Guess all 50 states. When you're done (or type Exit to quit early), check the `states_to_learn.csv` file to see what you missed.
