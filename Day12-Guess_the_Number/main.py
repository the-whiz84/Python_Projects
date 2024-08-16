
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

# Alternative solution:
# import random
#
# NUMBER_TO_GUESS = randint(1, 100)
# print(f"Pssst, the correct answer is {NUMBER_TO_GUESS}")

# attempts = 0
# game_over = False
#
# print(logo)
# print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# print(NUMBER_TO_GUESS)
#
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#
# if difficulty == "hard":
# 	attempts = 5
# 	print("You have 5 attempts remaining to guess the number.")
# elif difficulty == "easy":
# 	attempts = 10
# 	print("You have 10 attempts remaining to guess the number.")
# else:
# 	print("Invalid option selected. Please type 'easy' or 'hard")
# 	exit(1)
#
# guessed_number = int(input("Make a guess: "))
# attempts -= 1
#
# while not game_over:
# 	if attempts == 0:
# 		game_over = True
# 		print("You've run out of guesses, you lose.")
# 	elif guessed_number == NUMBER_TO_GUESS:
# 		game_over = True
# 		print(f"You got it! The answer was {guessed_number}")
# 	elif guessed_number < NUMBER_TO_GUESS:
# 		print("Too low.")
# 		print(f"You have {attempts} attempts remaining to guess the number.")
# 		guessed_number = int(input("Guess again: "))
# 		attempts -= 1
# 	else:
# 		print("Too high.")
# 		print(f"You have {attempts} attempts remaining to guess the number.")
# 		guessed_number = int(input("Guess again: "))
# 		attempts -= 1


# Instructor solution:
# from random import randint
# from art import logo


# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5


# # Function to check users' guess against actual answer
# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}")


# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS


# def game():
#     print(logo)
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")

#     turns = set_difficulty()

#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         # Let the user guess a number
#         guess = int(input("Make a guess: "))
#         # Track the number of turns and reduce by 1 if they get it wrong
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")

# game()