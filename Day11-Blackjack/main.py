############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
import os

def clear():
    os.system('cls' if os.name == "nt" else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(dealt_cards):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(dealt_cards)
    if len(dealt_cards) == 2 and score == 21:
        return 0      
    if 11 in dealt_cards and score > 21:
        dealt_cards.remove(11)
        dealt_cards.append(1)
    return score

def compare_scores(player_score, pc_score):
    """Take both the player and the computer's scores and compare them to establish the winner"""
    if player_score > 21:
        return "You lose!"
    elif pc_score > 21:
        return "You win!"
    elif player_score == 0 and pc_score == 0:
        return "You have Blackjack and computer has Blackjack. You lose!"
    elif player_score == pc_score:
        return f"Your score is {player_score} and computer's score is {pc_score}. It's a draw!"
    elif player_score == 0:
        return "Blackjack! You win!"
    elif pc_score == 0:
        return "Computer has Blackjack. You lose!"
    elif player_score > pc_score:
        return f"Your score is {player_score} and computer's score is {pc_score}. You win!"
    else:
        return f"Your score is {player_score} and computer's score is {pc_score}. You lose!"
 
def blackjack():
    print(logo)   
    player_cards = []
    ai_cards = []
    player_cards.extend([deal_card(), deal_card()])
    ai_cards.extend([deal_card(), deal_card()])

    print(f"Computer draws {ai_cards[0]}, X]")
    print(f"You draw {player_cards}")

    end_game = False
    
    while end_game == False:
        user_score = calculate_score(player_cards)
        ai_score = calculate_score(ai_cards)
        if user_score == 0 or ai_score == 0 or user_score > 21:
            end_game = True
        else:
            draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if draw_card == "y":
                player_cards.append(deal_card())
                print(f"You now have {player_cards}")
            elif draw_card == "n":
                end_game = True
            else:
                print("Invalid option selected, please try again.")
                end_game = True
    print(f"Computer has {ai_cards}")
    while ai_score != 0 and ai_score < 17:
        ai_cards.append(deal_card())
        ai_score = calculate_score(ai_cards)
        print("Computer draws a card")
        print(f"Computer now has {ai_cards}")

    print(compare_scores(user_score, ai_score))
    
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'n':
        return
    elif play_again == 'y':
        clear()
        blackjack()
    else:
        print("Invalid option selected")
        return
blackjack()
