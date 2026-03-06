# Day 07 - Hangman Logic and State Tracking

Today we're building Hangman. It's the biggest project yet, and it brings together everything we've learned so far: variables, conditionals, for loops, and randomisation.

But it also introduces three massive new concepts: **while loops** (running code until a specific condition is met), **state tracking** (remembering what happened on previous turns), and **modules** (splitting your code across multiple files so it doesn't become a gigantic mess).

## The project

Wait, where did all the code go? If you look at `main.py`, you'll notice we aren't storing the giant list of words or the ASCII art for the hangman stages in the main file anymore.

```python
import random
from hangman_art import logo, stages
from hangman_words import word_list
```

This is how real Python projects are organized. We put the massive list of words in `hangman_words.py` and the ASCII art in `hangman_art.py`. Then we `import` them. This keeps `main.py` clean—it only contains the game logic, not the heavy data.

## Setting up the board

First, we pick a random word. But we don't want to show the user the word; we want to show them blanks (`_`).

```python
chosen_word = random.choice(word_list)
display = []

for _ in range(len(chosen_word)):
    display.append("_")
```

If the word is "apple", `display` becomes `['_', '_', '_', '_', '_']`. This list is our **state**. As the user guesses correctly, we'll swap out those underscores for real letters.

## The game loop

We don't know how many guesses it will take to win or lose. A `for` loop won't work here because we don't have a fixed number of iterations. We need a **while loop**.

```python
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    # ... game logic happens here ...
```

This loop runs forever until `end_of_game` gets flipped to `True`. When does that happen?

1. They run out of lives (they lose).
2. There are no more `"_"` characters in the `display` list (they win).

## Checking the guess

Inside the while loop, we check if the guessed letter is inside the word. We have to check every single position because the letter might appear twice (like the 'p's in "apple").

```python
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
```

If the guess is wrong, we subtract a life. The `in` keyword is a lifesaver here — it lets us check if a value exists inside a string or list without writing a manual loop:

```python
if guess not in chosen_word:
    lives -= 1
    print(f"Your guessed letter {guess}. This is not in the word. You lost a life")
    if lives == 0:
        end_of_game = True
        print(f"\n***********************YOU LOSE**********************")
```

Finally, we print the current hangman picture from our imported `stages` list. Because the list is ordered backwards (stage 6 is full health, stage 0 is dead), we just use `stages[lives]`.

## Try it yourself

```bash
python "main.py"
```

Play a few rounds. Notice how the screen clears after every guess (using `os.system('clear')`) to make it feel like a real terminal game instead of a scrolling log.
