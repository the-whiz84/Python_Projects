# Day 34 - API-Driven Quiz App with Classes and UI Separation

Day 34 turns the earlier quiz ideas into a full app pipeline. Questions come from an external API, get converted into `Question` objects, move through a quiz engine, and are displayed by a Tkinter interface. The most important lesson is architecture: the data source, the quiz logic, and the UI are all separate pieces, which makes the app easier to extend and reason about.

## 1. Fetching and Preparing Question Data from an API

The quiz data is loaded in `data.py`:

```python
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
```

This is a good example of treating an API as a raw data source. The response is still just a list of dictionaries at this point. The app does not use it directly in the UI because raw API payloads usually are not the cleanest structure for the rest of the program.

That is why the next step matters.

## 2. Converting Raw Dictionaries into Question Objects

`main.py` builds a question bank from the API data:

```python
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
```

This translation step is important because it gives the rest of the program a stable internal model. The `Question` class is small, but it creates a consistent shape for every quiz item:

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

The app is no longer tied directly to the exact structure of the API response once that conversion is complete.

## 3. Keeping Quiz State Inside `QuizBrain`

The quiz logic is isolated in `quiz_brain.py`:

```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
```

This class owns the state that changes during the quiz:

- which question is current
- how many questions have been asked
- how many answers were correct

Its methods keep that logic out of the UI layer:

```python
def next_question(self):
    self.current_question = self.question_list[self.question_number]
    self.question_number += 1
    q_text = html.unescape(self.current_question.text)
    return f"Q.{self.question_number}: {q_text} (True/False): "
```

The call to `html.unescape()` is a small but important data-cleaning step. API responses often contain encoded characters, and the quiz engine cleans them before the interface displays the text.

## 4. Letting the UI Focus Only on Presentation and Feedback

The Tkinter interface wraps the presentation layer:

```python
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
```

When a button is pressed, the UI does not decide whether the answer is correct by itself. It asks the quiz engine:

```python
def true_pressed(self):
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)
```

Then it uses the result to update the interface:

```python
def give_feedback(self, is_right):
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)
```

This separation is what makes the project strong. `QuizBrain` knows quiz rules. `QuizInterface` knows how to show those rules to the user. Each part stays focused on one job.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Answer the True/False questions using the buttons.
4. Confirm that the score updates, the card flashes green or red for feedback, and the buttons become disabled when the quiz ends.

## Summary

Day 34 is a strong architecture lesson disguised as a quiz app. The API supplies raw question data, `Question` objects normalize that data, `QuizBrain` manages quiz state and answer checking, and `QuizInterface` handles display and user feedback. The app works well because each layer has a clear responsibility.
