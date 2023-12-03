rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

# Start the game by asking the player:
# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out: 
# * How you will store the user's input.
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_images[player_choice])
# if player_choice == 0:
#     print(rock)
# elif player_choice == 1:
#     print(paper)
# elif player_choice == 2:
#     print(scissors)
# else:
#     print("Invalid input! Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")


# * How you will generate a random choice for the computer.
ai_choice = random.randint(0, 2)

print("Computer chose:\n")
print(game_images[ai_choice])
# if ai_choice == 0:
#     print(rock)
# elif ai_choice == 1:
#     print(paper)
# elif ai_choice == 2:
#     print(scissors)



# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
if player_choice >= 3 or player_choice < 0:
    print("You chose an invalid option, please try again!")
elif player_choice == ai_choice:
    print("It's a draw, try again!\n")
elif player_choice == 0 and ai_choice == 2:
    print("You win!")
elif player_choice == 2 and ai_choice == 0:
    print("You lose!")
elif player_choice < ai_choice:
    print("You lose!")
else:
    print("You win!")



# * And also how you will give feedback to the player. 