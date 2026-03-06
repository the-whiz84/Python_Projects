# Day 17 - Classes, Objects, Attributes, and Methods

Today we're taking the idea from Day 16 and slowing it down a little. Instead of jumping straight into several ready-made classes, we build a simple class ourselves and then use the same thinking in a quiz app.

This folder has two parts that belong together. `main_creating_classes.py` teaches the raw syntax of creating objects, and the quiz project shows why that syntax matters once your program starts tracking state across multiple questions.

## Building your first class

Let's start with the smallest example, because this is where `__init__` and `self` usually stop feeling abstract. In `main_creating_classes.py`, we define a `User` class and give every new user an id, a username, and two counters:

```python
class User:

	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		self.followers = 0
		self.following = 0
```

When we create `user_1 = User("001", "angela")`, Python runs `__init__` for us and fills in those attributes on that specific object. That is the big shift today: instead of manually building related variables, we package them inside one object.

The `follow()` method is also a great example because it changes state in two places at once:

```python
	def follow(self, user):
		user.followers += 1
		self.following += 1
```

Read that slowly. `self` is the object calling the method, and `user` is the object being passed in. So when `user_1.follow(user_2)` runs, `user_1` starts following one more person, and `user_2` gains one follower. That is much easier to reason about than juggling separate dictionaries or parallel lists.

## Turning raw data into objects

Now the quiz app takes the same idea and makes it useful. In `question_model.py`, the `Question` class is intentionally tiny:

```python
class Question:

	def __init__(self, q_text, q_answer):
		self.text = q_text
		self.answer = q_answer
```

This class does not run the quiz. It just stores one question and one answer. That is a good design habit to build early. A class does not need to do everything. Sometimes its whole job is to hold clean, predictable data.

Then in `main.py`, we turn the raw dictionaries from `data.py` into real `Question` objects:

```python
question_bank = []

for entry in question_data:
	new_question = Question(entry["question"], entry["correct_answer"])
	question_bank.append(new_question)

quiz = QuizBrain(question_bank)
```

That loop is doing an important translation step. `data.py` gives us raw API-style data. Our app does not want to work with loose dictionaries forever, so we convert each one into a `Question` object. After that, the rest of the program can rely on `.text` and `.answer` without caring where the data originally came from.

## Letting one object run the quiz

The real control lives in `quiz_brain.py`. This class tracks which question we are on, asks the next one, and keeps score:

```python
def next_question(self):
	current_question = self.question_list[self.question_number]
	self.question_number += 1
	user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
	self.check_answer(user_answer, current_question.answer)
```

This is where objects start paying off. `QuizBrain` owns `question_number`, `question_list`, and `score`, so we do not need global variables floating around the program. Every time `next_question()` runs, the object updates its own state and moves the quiz forward.

The scoring method continues that pattern:

```python
def check_answer(self, user_answer, correct_answer):
	if user_answer.lower() == correct_answer.lower():
		self.score += 1
		print("You got it right.")
	else:
		print("That's wrong.")
	print(f"The correct answer was {correct_answer}.")
	print(f"Your current score is: {self.score}/{self.question_number}")
	print("\n")
```

Notice what stays inside the class: the current score and the current question number. That is the habit I want you to keep from this lesson. If a value belongs to one object, let that object own it.

## Why this day matters

If `self` still feels strange, that is normal. The easiest way to think about it is this: `self` is just Python's way of saying, "work with this specific object, not the class in general." Once that clicks, the rest of OOP becomes much less mysterious.

This day is really about responsibility. `Question` stores question data. `QuizBrain` runs the quiz. `User` tracks follower relationships. Each object has a clear job, and the program becomes easier to read because of it.

## Try it yourself

Run the quiz app first:

```bash
python "main.py"
```

Then run the smaller class demo and trace what happens to the follower counts after `user_1.follow(user_2)`:

```bash
python "main_creating_classes.py"
```
