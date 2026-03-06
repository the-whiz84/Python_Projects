# Day 34 - Building the Quizzler App

Today we're building a graphical quiz app that fetches questions from an API and displays them one at a time. You answer True or False, get immediate feedback, and see your score update.

This brings together everything we've learned: class-based architecture, API calls, and GUI programming. We also introduce type hints as a way to document what kind of data functions expect.

## Type hints

Type hints let you specify what type of data a function expects:

```python
def greeting(name: str) -> str:
    return "hello" + name

def police_check(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False
```

The `: str` after `name` says we expect a string. The `-> str` after the parentheses says the function returns a string. These hints don't change how Python runs the code, but they make it easier to understand what a function does and help tools catch mistakes.

## Fetching questions from an API

The quiz pulls questions from the Open Trivia Database:

```python
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
```

Each question comes as a dictionary with the question text, correct answer, and incorrect answers. We extract what we need and build Question objects.

## The Question model

The `Question` class stores one question and its answer:

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

Simple data classes like this are the backbone of well-organized programs.

## The QuizBrain

The quiz logic lives in its own class:

```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        return False
```

We use `html.unescape()` because the API returns HTML-encoded characters (like `&quot;` for quotation marks).

## Building the UI

The UI class wraps Tkinter and connects buttons to the quiz brain:

```python
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
```

When the user clicks True or False, the UI calls `quiz.check_answer()` and updates the display.

## Try it yourself

```bash
python "main.py"
```

Answer the questions by clicking the True or False buttons. The app fetches fresh questions each time it runs.
