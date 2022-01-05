
import random
from art import logo
import os

def clear():
    os.system('cls' if os.name == "nt" else 'clear')
    

chosen_number = random.randint(1, 100)

def check_number(guessed_number, lives):
    if guessed_number > 100:
        print("Invalid option, try again")
        return lives
    elif guessed_number > chosen_number:
        print("Too high")
        return lives - 1
    elif guessed_number < chosen_number:
        print("Too low")
        return lives - 1
    elif guessed_number == chosen_number:
        print(f"You got it! The chosen number was {chosen_number}")
        return 0

def numbers_game():
    print(logo)
    print("Welcome to Guess the Number game\nI am thinking of a number between 1 and 100, can you guess it?\n") 

    difficulty = input("Choose your difficulty. Type 'normal' or 'hard': ")

    if difficulty == "normal":
        turns_remaining = 10
    elif difficulty == "hard":
        turns_remaining = 5
    else:
        return "Invalid option"


    while turns_remaining > 0:
        player_guess = int(input("Guess the number: "))
        turns_remaining = check_number(player_guess, turns_remaining)
        if turns_remaining > 0:
            print(f"You got {turns_remaining} tries left")
        elif turns_remaining == 0 and player_guess != chosen_number:
            print("You did not guess the number. Game over!")
        
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == "y":
        clear()
        numbers_game()
    elif play_again == "n":
        return

numbers_game()
