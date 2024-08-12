import random
from hangman_art import logo,stages
from hangman_words import word_list
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)
# print(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(stages[6])

print(f"{' '.join(display)}\n")

while not end_of_game:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Please guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You already guessed {guess}. Please choose another letter: ")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Your guessed letter {guess}. This is not in the word. You lost a life")
        if lives == 0:
            end_of_game = True
            print(f"\n***********************YOU LOSE**********************")
            print(f"Correct word: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\n****************************YOU WIN****************************")
    
    print(stages[lives])
