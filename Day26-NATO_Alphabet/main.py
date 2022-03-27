import pandas

data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

# user_word = input("Please type a word to get the NATO phonetic spelling:\n").upper()
# nato_letters = [nato_dict[letter] for letter in user_word]

# Updated code
# Catch the KeyError when a user enters a character that is not a letter.
# Provide feedback to the user when an incorrect character was entered.

invalid_char = True

while invalid_char:
    user_word = input("Please type a word to get the NATO phonetic spelling:\n").upper()

    try:
        nato_letters = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Please enter only letters from the alphabet.\n")
    else:
        print(f"\n{nato_letters}")
        invalid_char = False
