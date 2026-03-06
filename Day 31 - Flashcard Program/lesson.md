# Day 31 - Flashcard State Management and Data-Driven UI

Day 31 builds a flashcard app that keeps track of what the user still needs to study. That makes it more than a simple card-flipping interface. The app combines Tkinter for presentation, pandas for data loading and saving, and timed callbacks for automatic card flipping. The most important idea is that the study deck changes based on user actions, so the dataset becomes part of the app state.

## 1. Loading Either the Original Deck or the Saved Progress File

The app starts by trying to load a smaller progress file:

```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

This is a strong design pattern:

- if progress exists, resume from there
- otherwise, start from the original dataset

The call to `to_dict(orient="records")` matters because it turns each row into a dictionary. That gives the rest of the app a simple list of cards to work with instead of a DataFrame that would be awkward to mutate one card at a time.

## 2. Using a Timer to Flip the Card Automatically

The app shows the French word first, then flips to English after three seconds:

```python
def new_card():
    global current_card, flash_card
    window.after_cancel(flash_card)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flash_card = window.after(3000, flip_card)
```

This is a good extension of the scheduling idea from the Pomodoro project. `after()` is not only for countdown timers. It is a general way to delay an action inside a GUI app.

`after_cancel(flash_card)` is just as important as the new timer. If the user skips to another card before the old timer finishes, the previous scheduled flip must be canceled or the interface will fall out of sync.

## 3. Letting User Feedback Change the Dataset

When the user marks a word as known, the app removes it from the study list:

```python
def known_word():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_card()
```

This is the heart of the project. The app is not only displaying data. It is using the user’s answer to reshape the next session.

That makes the project feel more like a learning tool than a simple GUI. The dataset evolves as the user improves.

## 4. Why the Interface and Data Model Work Together

The visual side of the app is simple:

- a canvas for the card image and text
- one button for “known”
- one button for “show another card”

But the app only feels useful because those controls are wired to the data model. Clicking the wrong button gives you another card without changing the dataset. Clicking the right button removes the current card and saves the new study list.

That connection between interface events and persistent data is the real step forward on this day.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Wait for a card to flip automatically after a few seconds.
4. Click the correct-answer button and confirm that the app saves the updated learning list to `data/words_to_learn.csv`.

## Summary

Day 31 combines timed GUI behavior with persistent learning state. The app loads either the original dataset or saved progress, uses `after()` to flip cards automatically, and rewrites the study list when the user marks a word as known. The project works well because the interface is directly tied to the evolving dataset.
