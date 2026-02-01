import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_to_resolve = input("Provide a word: ").upper()
word_letters = [phonetic_dict[letter] for letter in word_to_resolve]
print(word_letters)