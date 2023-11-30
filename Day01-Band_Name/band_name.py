# Generate a band name by combining the name of a city and the name of your pet

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!\n")

#2. Ask the user for the city they grew up in.
CITY = input("What is the name of the city you grew in?\n")

#3. Ask the user for the name of a pet.
PET = input("What is the name of your first pet?\n")

#4. Combine the name of their city and pet and show them their band name.
BAND_NAME = CITY + " " + PET
print("Your band name could be:\n" + BAND_NAME)
#5. Make sure the input cursor shows on a new line, see the example at:
#  https://band-name-generator-end.appbrewery.repl.run/