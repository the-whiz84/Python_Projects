# Day 07 - Hangman Logic and State Tracking

Today we're building Hangman, and this is the first beginner project that starts to feel like a real game loop instead of a short script. It combines random word selection, repeated guesses, lives, and a visible board state that changes over time. That makes it a strong introduction to two important ideas: keeping track of state and using a `while` loop when you do not know in advance how many turns the program will need.

## 1. Splitting Data and Logic into Separate Files

The first thing to notice in `main.py` is that the project no longer keeps everything in one file:

```python
import random
from hangman_art import logo, stages
from hangman_words import word_list
```

This is a useful step forward in project organization. The word list and ASCII art are data, not game logic, so moving them into `hangman_words.py` and `hangman_art.py` keeps `main.py` focused on the actual rules of play.

Even in a small project, separating responsibilities makes the main program easier to read.

## 2. Representing the Hidden Word as State

After choosing a random word, the script creates a display list filled with underscores:

```python
chosen_word = random.choice(word_list)
display = []

for _ in range(len(chosen_word)):
    display.append("_")
```

This `display` list is the central piece of game state. It starts as blanks, and each correct guess replaces one or more underscores with the matching letter.

That design matters because the program needs to remember progress from one turn to the next. A single print statement would not be enough. The game needs a data structure it can update over time.

## 3. Running the Game Until a Win or Loss

Hangman cannot use a fixed loop count because the number of guesses depends on the player. That is why the game uses a `while` loop:

```python
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
```

The loop continues until something changes `end_of_game` to `True`. There are two ways that happens:

- the player fills in every missing letter
- the player runs out of lives

Inside that loop, the script checks every position in the chosen word:

```python
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
```

That position-by-position update is what allows repeated letters to work correctly. If the word contains the same letter twice, both positions can be revealed.

## 4. Penalizing Wrong Guesses and Rendering Feedback

Wrong guesses cost a life:

```python
if guess not in chosen_word:
    lives -= 1
    print(f"Your guessed letter {guess}. This is not in the word. You lost a life")
    if lives == 0:
        end_of_game = True
        print(f"\n***********************YOU LOSE**********************")
```

This block shows how state connects different parts of the program:

- `guess` comes from user input
- `chosen_word` determines whether the guess is correct
- `lives` tracks the remaining attempts
- `stages[lives]` displays the right hangman graphic for that moment

That is the larger lesson of the project. Games work because the program keeps updating internal state and turning it into visible feedback.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Guess one letter at a time.
4. Verify that correct guesses reveal letters in `display` and wrong guesses reduce the life count and change the hangman stage.

## Summary

Day 07 introduces real stateful game logic. You import supporting data from separate modules, represent the hidden word as a mutable list, use a `while` loop to keep the game running, and update lives and display state after each guess. It is one of the first projects where the program has to remember what happened before and react differently on every turn.
