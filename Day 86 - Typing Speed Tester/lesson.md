# Day 86 - Typing Speed Metrics, Timers, and Desktop UI

This project turns a simple typing drill into a timed desktop app. The interesting part is not the word list itself. It is the way the app coordinates timing, live feedback, scrolling text, and score calculation inside one event-driven window.

That makes Day 86 a good lesson in UI state and timer-based logic.

## 1. Build the Test Around Explicit State

The PyQt app starts by initializing the values that control the whole test:

```python
self.start_time = None
self.time_limit = 60
self.timer_running = False
self.correct_words = 0
self.total_characters = 0
self.mistyped_words = 0
self.word_index = 0
self.current_words = []
```

This is what makes the app understandable. Instead of hiding progress inside widget text, it keeps the test state in named fields:

- current word position
- remaining time
- correct word count
- mistyped word count
- total characters

That is the right habit for any interactive program that updates over time.

## 2. Start the Timer on Real User Activity

The app does not start counting down when the window opens. It starts when the user begins typing:

```python
def start_timer(self):
    if not self.timer_running:
        self.start_time = time.time()
        self.timer_running = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
```

That is a better user experience than forcing the countdown immediately. It also means the test is linked to actual interaction, not to app launch.

The input field is wired to live checking through `textChanged`:

```python
self.text_input.textChanged.connect(self.check_character)
```

That event loop is the heart of the app.

## 3. Give Immediate Feedback While Typing

One of the nicer design choices is that the word display updates character by character:

```python
def apply_text_color(self, typed_text):
    current_word = self.current_words[self.word_index]
    formatted_text = ""

    for i, char in enumerate(typed_text):
        if i < len(current_word) and char == current_word[i]:
            formatted_text += f"<span style='color: green;'>{char}</span>"
        else:
            formatted_text += f"<span style='color: red;'>{char}</span>"
```

That gives the user immediate visual feedback instead of only scoring at the end. It also makes the app feel faster because mistakes appear as soon as they happen.

The display only shows a window of words rather than the full list:

```python
words_to_show = " ".join(
    self.current_words[self.word_index : self.word_index + 10]
)
```

That scrolling-window approach keeps the interface readable and focused.

## 4. Score the Test as Completed Words

When the user types a space, the app submits the current word:

```python
def submit_word(self):
    typed_word = self.text_input.text().strip()
    current_word = self.current_words[self.word_index]

    if typed_word == current_word:
        self.correct_words += 1
        self.total_characters += len(typed_word)
    else:
        self.mistyped_words += 1
```

This keeps the scoring logic simple:

- WPM is based on correct words
- CPM is based on correctly typed characters
- mistakes are tracked separately

At the end of the timer, the app disables the input field and shows the result:

```python
self.result_label.setText(
    f"Time's up!\\nCPM: {cpm}\\nWPM: {wpm}\\nMistyped Words: {self.mistyped_words}"
)
```

The reset path also matters. `reset_test()` restores the counters, enables the input again, resets the timer label, and rebuilds the visible word list for another attempt.

## How to Run the Typing Speed Tester

1. Install PyQt if it is not already available:
   ```bash
   pip install PyQt5
   ```
2. Run the app:
   ```bash
   python main.py
   ```
3. Start typing in the input box and confirm:
   - the timer begins on first input
   - characters are highlighted green or red
   - the visible word window advances as words are submitted
   - the result screen shows CPM, WPM, and mistyped words

## Summary

Today, you practiced coordinating multiple kinds of application state at once: timing, scoring, current word position, and live visual feedback. The project works because the app keeps those concerns explicit and updates them through a small number of clear event handlers rather than scattered widget logic.
