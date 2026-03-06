# Day 31 - Flashcard Program

Today we're building a flashcard app that helps you learn French words. You see a French word, try to remember the English translation, flip the card to check, and mark whether you knew it or not. Words you don't know stay in the deck; words you know are removed.

This combines Tkinter for the UI, Pandas for data handling, and the concept of filtering lists based on user actions.

## Loading and managing data

We start by loading the French words. If the user has used the app before, there's a `words_to_learn.csv` with words they haven't mastered yet. If that file doesn't exist, we fall back to the original word list:

```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

The `orient="records"` format turns each row into a dictionary, so we get a list like `[{"French": "bonjour", "English": "hello"}, ...]`.

## Flipping cards with timers

The card automatically flips after 3 seconds:

```python
def new_card():
    global current_card, flash_card
    window.after_cancel(flash_card)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flash_card = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
```

`window.after(3000, flip_card)` schedules the flip function to run after 3000 milliseconds. We store the timer ID so we can cancel it if the user clicks a button before the timer fires.

## Removing known words

When the user clicks the checkmark (known word), we remove that card from the list and save the updated list:

```python
def known_word():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_card()
```

This creates a spaced-repetition effect: words you struggle with keep appearing, words you've mastered get filtered out.

## Try it yourself

```bash
python "main.py"
```

Wait 3 seconds to see the English translation. Click the checkmark if you knew it, or the X to see it again later.
