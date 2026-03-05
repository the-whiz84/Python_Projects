# Day 17 - Classes, Objects, Attributes, and Methods
Day 17 introduces how to model real program state with classes so your logic is easier to extend than a single long script.

## Why This Day Matters
Until now, most days were procedural: variables + functions + loops. Here, you start packaging state and behavior together in objects. That shift is the foundation for larger games and apps in the next modules.

## Project Focus in This Folder
This day has two connected learning pieces:
- `main_creating_classes.py`: class syntax basics (`User` object with attributes and a method).
- Quiz app files (`main.py`, `question_model.py`, `quiz_brain.py`, `data.py`): practical class collaboration.

## Core Ideas You Practice
- Defining a class with `__init__` to set initial object state.
- Using `self` so each object keeps its own data.
- Creating methods that update state predictably.
- Passing objects between classes (`QuizBrain` consuming `Question` instances).

## How the Quiz App Is Structured
- `Question` (in `question_model.py`) stores one question text and one answer.
- `main.py` transforms raw dictionaries from `data.py` into a list of `Question` objects.
- `QuizBrain` (in `quiz_brain.py`) controls progression (`question_number`), scoring (`score`), and answer checking.

This separation is the key design lesson: data model (`Question`) and flow controller (`QuizBrain`) have different responsibilities.

## Real Day Snippets
From `main.py` (object creation from raw data):

```python
question_bank = []

for entry in question_data:
    new_question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
```

From `quiz_brain.py` (stateful method behavior):

```python
def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)
```

From `main_creating_classes.py` (method mutating two objects):

```python
def follow(self, user):
    user.followers += 1
    self.following += 1
```

## Beginner Pitfalls on This Day
- Forgetting `self` as the first method parameter causes `TypeError`.
- Treating class attributes and instance attributes as the same thing can share state unexpectedly.
- Incrementing `question_number` at the wrong time can skip a question or break score display.

## Run
```bash
python "main.py"
```

For the class syntax practice file:
```bash
python "main_creating_classes.py"
```
