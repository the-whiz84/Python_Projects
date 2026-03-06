# Day 84 - Tic-Tac-Toe Game State and Win-Condition Logic

This project is small enough to fit in one file, which makes it a good lesson in state management. Tic-tac-toe does not need a complex architecture, but it does need clear rules about whose turn it is, how moves are stored, when the game ends, and how the board resets.

That makes Day 84 a state-transition exercise disguised as a simple game.

## 1. Represent the Board Through UI State

The project creates a `3x3` grid of Tkinter buttons and stores them in a nested list:

```python
self.buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6, bg="#fff", font=("Helvetica", 24))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    self.buttons.append(row)
```

That is a practical choice for a small game. The UI element and the board cell are the same object. You do not need a second board array because each button already stores the current mark in its `text`.

The game also tracks the active player:

```python
self.player_turn = "X"
```

That one field drives every move transition in the game.

## 2. Centralize the Win and Draw Logic

The `check_win()` method is the core of the project:

```python
def check_win(self):
    for row in self.buttons:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            return True
    for column in range(3):
        if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
            return True
    if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
        return True
    if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
        return True
    if all(button['text'] != "" for row in self.buttons for button in row):
        return "draw"
    return False
```

This method is effective because it centralizes the rules:

- check each row
- check each column
- check both diagonals
- detect a full board with no winner

Keeping that logic in one place makes the click handler much easier to follow.

## 3. Update the Board Through One Move Handler

Every move flows through `click()`:

```python
if self.buttons[row][column]['text'] == "":
    self.buttons[row][column]['text'] = self.player_turn
    if self.player_turn == "X":
        self.buttons[row][column]['fg'] = "#32CD32"
    else:
        self.buttons[row][column]['fg'] = "#FF0000"
    result = self.check_win()
```

This handler does three jobs in order:

1. reject moves on occupied cells
2. write the current player's mark
3. check whether the move ended the game

That order matters. State updates are easier to trust when the app has one obvious place where they happen.

The rest of the function uses message boxes to announce wins or draws, then resets the game if needed.

## 4. Reset Cleanly Instead of Rebuilding the UI

The reset path is simple and correct:

```python
def reset_game(self):
    self.player_turn = "X"
    for row in self.buttons:
        for button in row:
            button['text'] = ""
            button['bg'] = "#fff"
```

This is a good reminder that resetting state is often cheaper than reconstructing the whole interface. The board layout does not change, so the project clears the marks and returns the player turn to `X`.

That keeps the control flow small and the user experience immediate.

## How to Run the Tic-Tac-Toe App

1. Tkinter ships with standard Python on most desktop installs.
2. Run the game:
   ```bash
   python main.py
   ```
3. Verify the main interactions:
   - turns alternate between `X` and `O`
   - a win is detected across rows, columns, and diagonals
   - a draw is detected on a full board
   - the board resets after the result dialog

## Summary

Today, you practiced keeping a small game honest through explicit state changes. The buttons double as the board, `check_win()` centralizes the rules, and `reset_game()` restores the app without rebuilding it. Tic-tac-toe is simple, but the lesson behind it is reusable: game logic gets easier when state transitions happen in one clear place.
