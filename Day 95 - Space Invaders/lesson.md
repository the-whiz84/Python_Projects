# Day 95 - Space Invaders

This lesson is manually reconstructed from this day’s real project files. It focuses specifically on **Space Invaders** and avoids generic cross-day boilerplate.

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

You build **Space Invaders** as a day-specific project using `pygame`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `pygame`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `aliens.py`: Supporting module for project logic.
- `game.py`: Supporting module for project logic.
- `player.py`: Supporting module for project logic.
- `requirements.txt`: Project resource used by this day.

## 4. Implementation Walkthrough

1. Start from the main flow and trace how input becomes final output step by step.
2. Split repeated logic into helper functions to keep orchestration readable.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
```

## 6. How to Run

```bash
pip install -r requirements.txt
```
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

- **Space Invaders** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- This lesson was authored directly from day code and project artifacts where no prior lesson file existed.
