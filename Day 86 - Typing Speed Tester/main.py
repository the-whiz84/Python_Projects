import sys
import time
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt
from word_list import word_list


class TypingSpeedTestApp(QWidget):
    def __init__(self):
        """Initialize the Typing Speed Test app window and layout."""
        super().__init__()
        self.init_ui()

        self.start_time = None
        self.time_limit = 60  # Timer for 1 minute
        self.timer_running = False
        self.correct_words = 0
        self.total_characters = 0
        self.mistyped_words = 0

        self.word_index = 0  # To track the index of words
        self.current_words = []  # List of current words to be initialized later

        self.remaining_time = self.time_limit
        self.current_typed = ""
        self.new_word_list()  # Generate initial ordered word list
        self.update_word_display()

    def init_ui(self):
        """Set up the UI layout and components with styling."""
        self.setWindowTitle("Typing Speed Test")
        self.setGeometry(100, 100, 600, 400)

        # Set the main window background to teal
        self.setStyleSheet("background-color: #008080;")

        # Main layout
        self.layout = QVBoxLayout()

        # Header layout for timer and instructions
        self.header_layout = QHBoxLayout()

        # Instructions label
        self.instructions_label = QLabel("Begin typing to start the timer", self)
        self.instructions_label.setFont(QFont("Roboto", 14))
        self.instructions_label.setStyleSheet("color: white;")
        self.header_layout.addWidget(self.instructions_label)

        # Timer label (aligned to the right)
        self.timer_label = QLabel("Time Left: 60", self)
        self.timer_label.setFont(QFont("Roboto", 16))
        self.timer_label.setAlignment(Qt.AlignRight)
        self.timer_label.setStyleSheet("color: white;")
        self.header_layout.addWidget(self.timer_label)

        self.layout.addLayout(self.header_layout)

        # Words display (scrolling text with 10 words)
        self.word_display = QLabel(self)
        self.word_display.setFont(QFont("Roboto", 22))
        self.word_display.setStyleSheet(
            "background-color: #333333; color: white; border: 1px solid #000; padding: 10px;"
        )
        self.word_display.setFixedHeight(100)
        self.layout.addWidget(self.word_display)

        # Input field for typing
        self.text_input = QLineEdit(self)
        self.text_input.setFont(
            QFont("Roboto", 24)
        )  # Increase font size for better visibility
        self.text_input.setStyleSheet(
            "background-color: black; color: white; border: 1px solid #000; padding: 10px;"
        )
        self.text_input.setFixedHeight(50)
        self.layout.addWidget(self.text_input)
        self.text_input.textChanged.connect(self.check_character)

        # Result label
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Roboto", 16))
        self.result_label.setStyleSheet("color: white;")
        self.layout.addWidget(self.result_label)

        # Try Again button (hidden initially)
        self.try_again_button = QPushButton("Try Again", self)
        self.try_again_button.setVisible(False)
        self.try_again_button.setStyleSheet(
            "background-color: #f0ad4e; font-size: 16px; padding: 10px; color: white;"
        )
        self.try_again_button.clicked.connect(self.reset_test)
        self.layout.addWidget(self.try_again_button)

        self.setLayout(self.layout)

    def new_word_list(self):
        """Generate a new list of ordered words from the word list."""
        self.word_index = 0  # Reset the index for new attempt
        self.current_words = word_list[:100]  # Use the first 100 words in order

    def start_timer(self):
        """Start the countdown timer when typing begins."""
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_timer)
            self.timer.start(1000)  # Timer to tick every second

    def update_timer(self):
        """Update the countdown timer every second."""
        elapsed_time = time.time() - self.start_time
        self.remaining_time = self.time_limit - int(elapsed_time)

        if self.remaining_time > 0:
            self.timer_label.setText(f"Time Left: {self.remaining_time}")
        else:
            self.end_test()

    def update_word_display(self):
        """Display the current word list as scrolling text with only 10 visible words."""
        words_to_show = " ".join(
            self.current_words[self.word_index : self.word_index + 10]
        )  # Show only 10 words
        self.word_display.setText(words_to_show)

    def check_character(self):
        """Check each character as it is typed and color it green or red."""
        self.start_timer()  # Start the timer on first keypress if not already running

        typed_text = self.text_input.text()
        if len(typed_text) > 0 and typed_text[-1] == " ":
            self.submit_word()
        else:
            self.apply_text_color(typed_text)

    def apply_text_color(self, typed_text):
        """Apply character-level color formatting for correctness."""
        current_word = self.current_words[self.word_index]
        formatted_text = ""

        for i, char in enumerate(typed_text):
            if i < len(current_word) and char == current_word[i]:
                formatted_text += f"<span style='color: green;'>{char}</span>"
            else:
                formatted_text += f"<span style='color: red;'>{char}</span>"

        remaining_text = current_word[len(typed_text) :]
        formatted_text += remaining_text

        display_text = (
            formatted_text
            + " "
            + " ".join(self.current_words[self.word_index + 1 : self.word_index + 10])
        )
        self.word_display.setText(display_text)

    def submit_word(self):
        """Submit the typed word and move to the next word."""
        typed_word = self.text_input.text().strip()  # Strip trailing space
        current_word = self.current_words[self.word_index]

        if typed_word == current_word:
            self.correct_words += 1
            self.total_characters += len(typed_word)
        else:
            self.mistyped_words += 1

        self.word_index += 1  # Move to the next word

        # Check if we've reached the end of the current words
        if self.word_index < len(self.current_words):
            self.update_word_display()
            self.text_input.clear()  # Clear input field for the next word
        else:
            self.end_test()  # End the test if no more words are available

    def end_test(self):
        """End the test and display the CPM and WPM results."""
        self.timer.stop()
        self.text_input.setEnabled(False)
        self.timer_running = False

        # Calculate CPM and WPM
        cpm = self.total_characters
        wpm = self.correct_words

        self.result_label.setText(
            f"Time's up!\nCPM: {cpm}\nWPM: {wpm}\nMistyped Words: {self.mistyped_words}"
        )
        self.try_again_button.setVisible(True)

    def reset_test(self):
        """Reset the test for a new attempt."""
        self.correct_words = 0
        self.total_characters = 0
        self.mistyped_words = 0
        self.timer_running = False
        self.text_input.setEnabled(True)
        self.result_label.setText("")
        self.try_again_button.setVisible(False)
        self.text_input.clear()
        self.timer_label.setText("Time Left: 60")
        self.new_word_list()  # Generate a new ordered word list
        self.update_word_display()


def main():
    app = QApplication(sys.argv)
    window = TypingSpeedTestApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
