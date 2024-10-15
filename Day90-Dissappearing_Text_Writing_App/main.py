import tkinter as tk
from tkinter import messagebox
import time


class WritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        self.root.geometry("800x600")

        # Styling
        self.root.config(bg="black")

        # Timer settings
        self.time_limit = 10  # Time limit in seconds
        self.remaining_time = self.time_limit
        self.is_typing = False
        self.timer_running = False
        self.last_keypress_time = None

        # Countdown label for visual feedback
        self.timer_label = tk.Label(
            self.root,
            text=f"Time left: {self.remaining_time} seconds",
            font=("Helvetica", 16),
            bg="black",
            fg="white",
        )
        self.timer_label.pack(pady=5)

        # Text area (disabled initially until start button is pressed)
        self.text_area = tk.Text(
            self.root,
            font=("Helvetica", 16),
            wrap="word",
            bg="white",
            fg="black",
            state=tk.DISABLED,
        )
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Start button to activate typing
        self.start_button = tk.Button(
            self.root,
            text="Start Writing",
            command=self.start_writing,
            font=("Helvetica", 16),
            bg="white",
            fg="green",
        )
        self.start_button.pack(pady=10)

    def start_writing(self):
        # Enable typing and start countdown
        self.text_area.config(state=tk.NORMAL)
        self.text_area.focus()
        self.is_typing = True
        self.timer_running = True
        self.start_button.pack_forget()  # Hide start button after starting
        self.text_area.bind("<KeyPress>", self.on_key_press)
        self.last_keypress_time = time.time()
        self.countdown()

    def on_key_press(self, event=None):
        # Reset timer every time a key is pressed
        self.is_typing = True
        self.last_keypress_time = time.time()
        self.remaining_time = self.time_limit
        self.timer_label.config(
            text=f"Time left: {self.remaining_time} seconds", fg="white", bg="black"
        )

    def countdown(self):
        if self.timer_running:
            current_time = time.time()
            self.remaining_time = self.time_limit - (
                current_time - self.last_keypress_time
            )

            if self.remaining_time <= 0:
                self.remaining_time = 0
                self.timer_running = False
                self.text_area.delete(1.0, tk.END)  # Delete all text
                self.timer_label.config(
                    text="Text deleted! Start typing again.", fg="red", bg="black"
                )
                messagebox.showinfo("Time's up!", "Text deleted! Start typing again.")
                self.start_button.pack(pady=10)
                self.text_area.config(state=tk.DISABLED)
            else:
                self.timer_label.config(
                    text=f"Time left: {self.remaining_time:.0f} seconds"
                )
                if self.remaining_time <= 3:
                    self.timer_label.config(fg="red")
                else:
                    self.timer_label.config(fg="white")

                # Call this function again after 1 second
                self.root.after(1000, self.countdown)


# Initialize the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WritingApp(root)
    root.mainloop()
