import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

with open("./nato_phonetic_alphabet.csv") as data_file:
    alphabet_df = pandas.read_csv(data_file)

nato_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Please type a word to get the NATO phonetic spelling:\n")

word_letters = [letter.upper() for letter in user_word]

nato_letters = [nato_dict[letter] for letter in word_letters]

print(f"\n{nato_letters}")
