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


def deal_card():
	"""Returns a random card from the deck."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card


def calculate_score(card_list):
	"""Takes a list of cards and returns the score calculated."""
	score = sum(card_list)
	if score == 21 and len(card_list) == 2:
		return 0

	if score > 21 and 11 in card_list:
		card_list.remove(11)
		card_list.append(1)

	return score


def compare(u_score, c_score):
	"""Get the score of user and computer and return the winner"""
	if c_score == 0:
		return "Computer has Blackjack. You lose!"
	elif u_score == 0:
		return "You have Blackjack. You win!"
	elif c_score == u_score:
		return "It's a Draw"
	elif u_score > 21:
		return "You went over. You lose!"
	elif c_score > 21:
		return "Computer went over. You win!"
	elif u_score > c_score:
		return "You win!"
	else:
		return "You lose!"


def play_game():
	print(logo)
	user_hand = []
	pc_hand = []
	pc_score = -1
	user_score = -1
	end_game = False

	for _ in range(2):
		user_hand.append(deal_card())
		pc_hand.append(deal_card())

	while not end_game:
		user_score = calculate_score(user_hand)
		pc_score = calculate_score(pc_hand)
		print(f"Your cards: {user_hand}, current score: {user_score}")
		print(f"Computer's first card: {pc_hand[0]}")

		if pc_score == 0 or user_score == 0 or user_score > 21:
			end_game = True
		else:
			draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
			if draw_card == "y":
				user_hand.append(deal_card())
			else:
				end_game = True

	while pc_score != 0 and pc_score < 17:
		pc_hand.append(deal_card())
		pc_score = calculate_score(pc_hand)

	print(f"Your final hand is: {user_hand}, final score: {user_score}")
	print(f"Computer final hand is: {pc_hand}, final score: {pc_score}")
	print(compare(user_score, pc_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
	print("\n" * 50)
	play_game()
