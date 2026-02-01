# 1. Handling Errors and Exceptions
import json

# What happens if we try to open and read a file that does not exist

# with open("a_file.txt") as file:
# 	file.read()
#
# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

# KeyError

# a_dictionary = {"key": "value"}
# value = a_dictionary["wrong_key"]
# KeyError: 'wrong_key'

# IndexError

# fruit_list = ["Apple", "Pear", "Banana"]
# fruit = fruit_list[3]
# IndexError: list index out of range

# TypeError

# text = "abc"
# print(text + 5)
# TypeError: can only concatenate str (not "int") to str

# Catching Exceptions
# try: 		# Something that might cause an exception
# except:	# Do this if there WAS an exception
# else:		# Do this if there were NO exceptions
# finally:	# Do this no matter what happens

# FileNotFound
# try:
# 	file = open("a_file.txt")
# except:

# # 	print("There was an error")
# # There was an error
# 	file = open("a_file.txt", "w")
# 	file.write("Something was written")

# # Too broad exception clause
# try:
# 	file = open("a_file.txt")
# 	a_dict = {"key": "value"}
# 	print(a_dict["blabla"])
# except FileNotFoundError:
# 	file = open("a_file.txt", "w")
# 	file.write("Something was written")
#
# # print(a_dict["blabla"])
# #           ~~~~~~^^^^^^^^^^
# # KeyError: 'blabla'
# # except KeyError:
# # 	print("That key does not exist")
# #
# # # That key does not exist
# except KeyError as error_message:
# 	print(f"The key {error_message} does not exist.")
# The key 'blabla' does not exist.

# try:
# 	file = open("a_file.txt")
# 	a_dict = {"key": "value"}
# 	print(a_dict["key"])
# except FileNotFoundError:
# 	file = open("a_file.txt", "w")
# 	file.write("Something was written")
# except KeyError as error_message:
# 	print(f"The key {error_message} does not exist.")
# else:
# 	content = file.read()
# 	print(content)
# # value
# # Something was written
# finally:
# 	file.close()
# 	print("File was closed.")
# value
# Something was written
# File was closed.


# 2. Raise your own Exceptions:

# try:
# 	file = open("a_file.txt")
# 	a_dict = {"key": "value"}
# 	print(a_dict["key"])
# except FileNotFoundError:
# 	file = open("a_file.txt", "w")
# 	file.write("Something was written")
# except KeyError as error_message:
# 	print(f"The key {error_message} does not exist.")
# else:
# 	content = file.read()
# 	print(content)
# # finally:
# # 	raise KeyError
# # KeyError
# # value
# # Something was written
# finally:
# 	raise TypeError("This is a made up error.")
# value
# Something was written
# ....
#     raise TypeError("This is a made up error.")
# TypeError: This is a made up error.
#
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height >  3:
# 	raise ValueError("Human height cannot exceed 3 meters.")
# bmi = round(weight / height ** 2, 2)
# print(bmi)
# # Height: 45
# # Weight: 70
# # 0.0345679012345679
# ValueError: Human height cannot exceed 3 meters.
#
# Process finished with exit code 1


# 3. Working with JSON files - Upgrading the Password Manager App

# Write
# json.dump()
json.dump(data, data_file, indent=4)

# Read
# json.load()
data = json.load(data_file)

# Update data
# json.update()
#1. Reading old data
data = json.load(data_file)
#2. Updating old data with new data
data.update(new_data)
#3. Saving updated data
json.dump(data, data_file, indent=4)
