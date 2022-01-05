#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+', '_']

print("Welcome to Wizard's Py Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passwd_letters = ''
for letter in range(nr_letters):
    letter = random.choice(letters)
    passwd_letters += letter
passwd_symbols = ''
for symbol in range(nr_symbols):
    symbol = random.choice(symbols)
    passwd_symbols += symbol
passwd_numbers = ''
for number in range(nr_numbers):
    number = random.choice(numbers)
    passwd_numbers += number
secure_password = str(passwd_letters + passwd_symbols + passwd_numbers)
# print(secure_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_number = nr_letters + nr_numbers + nr_symbols 
secure_shuffled_passwd = random.sample(secure_password, k=total_number)
random_passwd = ''.join(secure_shuffled_passwd)
print(f"Your randomly generated password is: {random_passwd}")
