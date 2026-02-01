# 1. List Comprehension

# Until now, in order to create a new list from an existing list we used a for loop
# numbers = [1, 2, 3]
# new_list = []
#
# for n in numbers:
# 	add_1 = n + 1
# 	new_list.append(add_1)

# Using List comprehension, we turn 4 lines of code into just 1
# new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# name = "Angela"
# name_list = [letter for letter in name]
# print(name_list)

# Python Sequences:
# list
# range
# string
# tuple
# All of them can be used in List Comprehension
#
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)


# 2. Conditional List Comprehension
# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# ['Alex', 'Beth', 'Dave']

# Challenge - Take all names over 5 letters and turn them in Upper Case version
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)
# ['CAROLINE', 'ELEANOR', 'FREDDIE']

# Challenge - Update US States game using List Comprehension


# 3. Dictionary Comprehension

# It allows us to create a new dictionary from the values in a list or another dictionary
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
#
# # Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(40, 100) for student in names}
# print(students_scores)
# # {'Alex': 55, 'Beth': 74, 'Caroline': 62, 'Dave': 75, 'Eleanor': 42, 'Freddie': 40}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)
#
# {'Alex': 51, 'Beth': 47, 'Caroline': 73, 'Dave': 86, 'Eleanor': 47, 'Freddie': 95}
# {'Caroline': 73, 'Dave': 86, 'Freddie': 95}


# 4. Looping through a Panda DataFrame
# import pandas
# student_dict = {
# 	"student": ["Angela", "James", "Lilly"],
# 	"score": [56, 76, 98]
# }
# # Looping through dict
# # for (key, value) in student_dict.items():
# # 	print(value)
#
# student_df = pandas.DataFrame(student_dict)
# print(student_df)

# Loop through a DF
# for (key, value) in student_df.items():
# 	# print(key)
# # student
# # score
# 	print(value)
# 0    Angela
# 1     James
# 2     Lilly
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64

# This is not really readable or useful. Pandas as an in-built method for loop called iterrows():

# for (index, row) in student_df.iterrows():
# 	print(row)
# student    Angela
# score          56
# Name: 0, dtype: object
# student    James
# score         76
# Name: 1, dtype: object
# student    Lilly
# score         98
# Name: 2, dtype: object

# Each row is a Panda Series object
# 	print(row.student)
# Angela
# James
# Lilly
# 	print(row.score)

# for (index, row) in student_df.iterrows():
# 	if row.student == "Angela":
# 		print(row.score)
# 56

# 5. Dictionary Comprehension from a Panda dataframe
import pandas
student_dict = {
	"student": ["Angela", "James", "Lilly"],
	"score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

new_dict = {row.new_key:row.new_value for (index, row) in student_df.interrows()}