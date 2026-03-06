# Day 25 - CSV Data Processing with Pandas and Coordinate-Based Quiz UI

Day 25 connects data processing to a graphical interface. The US states quiz uses a CSV file as its data source, then turns that data into visible labels on a map. This is also the first real pandas lesson in the course, so the important idea is not just “read a CSV.” It is learning how a DataFrame can act as the data layer behind an interactive program.

## 1. Loading Structured Data with Pandas

The project starts by reading `50_states.csv`:

```python
import turtle, pandas

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
```

`pandas.read_csv()` loads the whole table into a DataFrame, which behaves like a programmable spreadsheet. That is a major step up from reading lines manually because the columns stay named and structured.

The `all_states` list becomes the validation source for user guesses. In other words, pandas is not only loading data here. It is defining what counts as a valid answer.

## 2. Filtering the DataFrame to Find Coordinates

When a player guesses a state correctly, the program needs its map position:

```python
guessed_state = data[data["state"] == answer_data]
state_xcor = int(guessed_state["x"].item())
state_ycor = int(guessed_state["y"].item())
```

This is one of the most useful pandas patterns in the whole beginner section:

- filter rows based on a condition
- extract the values you need from the matching row

The filtered DataFrame acts like a lookup table. Once the correct state row is found, the code pulls the `x` and `y` coordinates and passes them into the turtle-based quiz UI.

## 3. Letting the Data Drive the Interface

The quiz loop ties the data layer to the map:

```python
while len(guessed_states) < 50:
    answer_data = screen.textinput(
        title=f"{quiz.score}/50 States Guessed",
        prompt="What's another state's name? "
    ).title()

    if answer_data in all_states:
        guessed_state = data[data["state"] == answer_data]
        state_xcor = int(guessed_state["x"].item())
        state_ycor = int(guessed_state["y"].item())
        quiz.add_state(answer_data, state_xcor, state_ycor)
```

This is the part that makes the project feel more substantial than a simple guessing game. The UI is not hardcoded with 50 labels. Instead, the code asks the dataset where each label belongs.

That design matters because it scales. If you had a different map with a different CSV, the same general pattern would still work.

## 4. Writing a New CSV from User Progress

The exit path is a second useful data workflow:

```python
if answer_data == "Exit":
    states_to_learn = [state for state in all_states if state not in guessed_states]
    pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
    break
```

This turns the player’s progress into a new dataset. The program is no longer only reading CSV files. It is generating one based on what the user did.

That makes the lesson more realistic. A lot of small data applications follow this pattern:

- read source data
- let the user interact with it
- write a smaller result file for later use

The squirrel examples in the folder reinforce the same idea from a different angle by counting rows that match specific fur colors.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Type state names into the prompt and confirm that correct guesses appear at the right place on the map.
4. Type `Exit` before finishing and check that `states_to_learn.csv` is created with the states you missed.

## Summary

Day 25 introduces pandas as a practical data tool inside an interactive app. The CSV becomes a DataFrame, the DataFrame powers validation and coordinate lookup, and the program writes a new CSV based on the user’s progress. It is an important bridge between basic Python scripting and data-driven programs.
