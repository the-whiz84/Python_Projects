# Day 84 - Tic Tac Toe game

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Tic Tac Toe game** and avoids generic cross-day boilerplate.

## Table of Contents

- [1. What You Build](#1-what-you-build)
- [2. Core Concepts](#2-core-concepts)
- [3. Project Structure](#3-project-structure)
- [4. Implementation Walkthrough](#4-implementation-walkthrough)
- [5. Day Code Snippet](#5-day-code-snippet)
- [6. How to Run](#6-how-to-run)
- [7. Common Pitfalls and Debug Tips](#7-common-pitfalls-and-debug-tips)
- [8. Practice Extensions](#8-practice-extensions)
- [9. Key Takeaways](#9-key-takeaways)

## 1. What You Build

You build **Tic Tac Toe game** as a day-specific project using `tkinter`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `tkinter`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.

## 4. Implementation Walkthrough

1. Create UI widgets, bind callbacks, and keep state updates deterministic.
2. Add targeted checks for edge cases and invalid paths before final output.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
class TicTacToe:
    def __init__(self):
        """
        Initializes the Tic Tac Toe game window with 3x3 grid of buttons.
        The window has a light blue background and the buttons are white.
        The game starts with player "X" and the buttons are labeled with
        commands to call the click method when clicked.
        The window also has a quit button at the bottom.
        """
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")
        self.window.configure(bg="#ADD8E6")  # Light blue background
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- Keep state updates in one place; desynchronized UI/game state causes subtle bugs.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Tic Tac Toe game** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
