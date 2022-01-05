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

#Write your code below this line 👇
import random

print("Let's play Rock, Paper, Scissors!\nWhat do you choose?")
player_choice = int(input("Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
ai_choice = random.randint(0, 2)

if player_choice == 0:
    player_response = rock
elif player_choice == 1:
    player_response = paper
elif player_choice == 2:
    player_response = scissors
else:
    player_response = player_choice

if ai_choice == 0:
    ai_response = rock
elif ai_choice == 1:
    ai_response = paper
elif ai_choice == 2:
    ai_response = scissors

if player_choice >= 3 or player_response < 0:
    print("You chose an invalid option, please try again!")
elif player_choice == 0 and ai_choice == 2:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nYou win!")
elif player_choice == 2 and ai_choice == 0:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nComputer wins!")
elif player_choice > ai_choice:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nYou win!")
elif player_choice == ai_choice:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nIt\'s a draw!")
elif player_choice < ai_choice:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nComputer wins!")
