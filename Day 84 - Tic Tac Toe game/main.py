import tkinter as tk
from tkinter import messagebox

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

        self.player_turn = "X"
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6, bg="#fff", font=("Helvetica", 24))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit, bg="black", fg="red", font=("Helvetica", 16))
        self.quit_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def check_win(self):
        """
        Checks the game state for a win, draw or in progress.

        Returns True if there is a winner, "draw" if the game is a draw, or False if the game is still in progress.
        """
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        # Check for a draw
        if all(button['text'] != "" for row in self.buttons for button in row):
            return "draw"
        return False

    def reset_game(self):
        """
        Resets the game state to its initial state.

        Sets the player turn to "X" and clears the text from all buttons.
        The background color of the buttons is also reset to white.
        """
        self.player_turn = "X"
        for row in self.buttons:
            for button in row:
                button['text'] = ""
                button['bg'] = "#fff"  # Keep the background white

    def click(self, row, column):
        """
        Handles the button click event.

        Sets the text of the clicked button to the current player turn
        and updates the button's text color. If the game is over, a message box
        is shown to announce the result and the game is reset. If the game is a
        draw, a message box is shown to ask if the player wants to play again.
        The player turn is then switched.
        """
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.player_turn == "X":
                self.buttons[row][column]['fg'] = "#32CD32"  # Green color for X
            else:
                self.buttons[row][column]['fg'] = "#FF0000"  # Red color for O
            result = self.check_win()
            if result == True:
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.reset_game()
            elif result == "draw":
                messagebox.showinfo("Game Over", "It's a draw!")
                play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
                if play_again:
                    self.reset_game()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def run(self):
        """
        Starts the Tkinter main event loop.

        The main event loop is an infinite loop that waits for an event to occur
        and process the event as long as the window is not closed.
        """
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()