# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def mail_merge():
    '''Given a list_of_names and starting_letter files in the Input folder, generate multiple letters for each name in the Output folder'''
    with open("./Input/Letters/starting_letter.txt") as example:
        letter = example.read()

    with open("./Input/Names/invited_names.txt") as names:
        list_of_names = names.readlines()

    for item in list_of_names:
        name = item.strip()
        new_letter = letter.replace("[name]", f"{name}")

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as outbound_letter:
            outbound_letter.write(f"{new_letter}")
    return 0

mail_merge()
