from operator import index
import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

# Alternative way to create the dictionary using built in methods set_index() and to_dict()
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html

# nato_dict = data_frame.set_index("letter")["code"].to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Initial code
# user_word = input("Please type a word to get the NATO phonetic spelling:\n")
# word_letters = [letter.upper() for letter in user_word]
# nato_letters = [nato_dict[letter] for letter in word_letters]

# Optimized code
user_word = input("Please type a word to get the NATO phonetic spelling:\n").upper()
nato_letters = [nato_dict[letter] for letter in user_word]

print(f"\n{nato_letters}")
