# menu.py
import tkinter as tk
from tkinter import messagebox


class Menu:
    def __init__(self, start_game_callback):
        self.start_game_callback = start_game_callback
        self.window = tk.Tk()
        self.window.title("Breakout Game")
        self.window.geometry("400x300")
        self.window.configure(bg="#2c3e50")  # Dark background color

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.window,
            text="Breakout Game",
            font=("Courier", 24),
            bg="#2c3e50",
            fg="#ecf0f1",
        )
        title_label.pack(pady=20)

        rules_button = tk.Button(
            self.window,
            text="Game Rules",
            command=self.show_rules,
            font=("Courier", 16),
            bg="white",
            fg="red",
        )
        rules_button.pack(pady=10, padx=20)

        start_button = tk.Button(
            self.window,
            text="Start Game",
            command=self.start_game,
            font=("Courier", 16),
            bg="white",
            fg="green",
        )
        start_button.pack(pady=10, padx=20)

        # Adding a footer label
        footer_label = tk.Label(
            self.window,
            text="Enjoy the Game!",
            font=("Courier", 14),
            bg="#2c3e50",
            fg="#ecf0f1",
        )
        footer_label.pack(side="bottom", pady=20)

    def show_rules(self):
        rules = (
            "Welcome to Breakout!\n\n"
            "1. Use the left and right arrow keys to move the paddle.\n"
            "2. Break all the bricks to win!\n"
            "3. Score points for each brick based on its color:\n"
            "   Yellow = 1, Green = 3, Orange = 5, Red = 7\n"
            "4. If you lose all lives, the game is over.\n"
            "5. The paddle shrinks after reaching the top wall.\n"
            "6. The ball speed will increase after reaching the orange and red bricks.\n"
            "7. After clearing the first screen, a second screen will appear.\n"
            "8. Good luck!"
        )
        messagebox.showinfo("Game Rules", rules)

    def start_game(self):
        self.window.destroy()
        self.start_game_callback()

    def run(self):
        self.window.mainloop()
