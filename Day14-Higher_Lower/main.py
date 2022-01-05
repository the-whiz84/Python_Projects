from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls' if os.name == "nt" else 'cls')
    

print(logo)

score = 0
game_over = False

selection1 = random.choice(data)

while not game_over:
    selection2 = random.choice(data)
    while selection1 == selection2:
        selection2 = random.choice(data)
    #Make a list from the selection with only the provided values: name, description and country
    compare_a = [selection1[key] for key in ('name', 'description', 'country')]
    compare_b = [selection2[key] for key in ("name", "description", "country")]
    #Extract the follower count as integer for A and B
    followers_a = int(selection1['follower_count'])
    followers_b = int(selection2['follower_count'])

    print(f"Compare A: {compare_a[0]}, a {compare_a[1]} from {compare_a[2]}")
    print(vs)
    print(f"Against B: {compare_b[0]}, a {compare_b[1]} from {compare_b[2]}")
    # print(f"A has {followers_a} millions vs B who has {followers_b} millions")
    
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    print(logo)
    
    if player_choice == "a" and followers_a > followers_b:
        score += 1
        print(f"You are correct! Current score: {score}")
    elif player_choice == "b" and followers_b > followers_a:
        score += 1
        print(f"You are correct! Current score: {score}")
        selection1 = selection2
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        game_over = True
    
