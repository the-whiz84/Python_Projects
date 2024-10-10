import tkinter as tk
from tkinter import messagebox

# Morse code dictionaries
DECODE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", "-----": "0",
    ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6",
    "--...": "7", "---..": "8", "----.": "9"
}

ENCODE = {value: key for key, value in DECODE.items()}

def encode_to_morse(text):
    """
    Translates English text to Morse code.

    Args:
        text (str): The English text to be translated.

    Returns:
        str: The translated Morse code string.
    """
    try:
        words = text.split()
        morse_words = [' '.join(ENCODE[char.upper()] for char in word if char.upper() in ENCODE) for word in words]
        morse_code = '   '.join(morse_words)
        return morse_code
    except KeyError:
        messagebox.showerror("Error", "Invalid character in the text")
        return ""

def decode_to_english(morse):
    """
    Translates Morse code to English text.

    Args:
        morse (str): The Morse code string to be translated.

    Returns:
        str: The translated English text.
    """
    try:
        words = morse.split('   ')
        decoded_words = [''.join(DECODE[letter] for letter in word.split() if letter in DECODE) for word in words]
        english_text = ' '.join(decoded_words)
        return english_text
    except KeyError:
        messagebox.showerror("Error", "Invalid Morse code sequence")
        return ""

# GUI Application using Tkinter
class MorseTranslatorApp:
    """
    A simple GUI application for translating between English and Morse code.
    """
    def __init__(self, root):
        """
        Initializes the main application window and widgets.
        
        Args:
            root (Tk): The root window object for the application.
        """
        self.root = root
        self.root.title("Morse Code Translator")

        # Set window background color to teal
        self.root.configure(bg="#008080")  # Teal

        # Dropdown menu for mode selection
        self.mode_var = tk.StringVar(value="English to Morse")  # Default value

        # Dropdown menu label
        self.mode_label = tk.Label(root, text="Select Translation Mode:", font=("Roboto", 16, "bold"), bg="#008080", fg="white")
        self.mode_label.grid(row=0, column=0, padx=10, pady=10)

        # Dropdown menu
        self.mode_menu = tk.OptionMenu(root, self.mode_var, "English to Morse", "Morse to English")
        self.mode_menu.config(font=("Roboto", 14), bg="#FFA500", fg="black", bd=0)
        self.mode_menu.grid(row=0, column=1, padx=10, pady=10)

        # Create single input/output text area
        self.text_area = tk.Text(root, height=10, width=60, bg="#2F4F4F", fg="white", font=("Roboto", 16), bd=2, relief="solid")
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Translate and Clear buttons
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text,
                                          bg="white", fg="black", font=("Roboto", 16, "bold"), bd=0)
        self.translate_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_text,
                                      bg="white", fg="black", font=("Roboto", 16, "bold"), bd=0)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    # Translate based on selected mode
    def translate_text(self):
        """
        Translates the input text based on the selected mode (English to Morse or Morse to English).
        """
        input_text = self.text_area.get("1.0", tk.END).strip()

        if self.mode_var.get() == "English to Morse":
            translated_text = encode_to_morse(input_text)
        else:
            translated_text = decode_to_english(input_text)

        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, translated_text)

    # Clear the text area
    def clear_text(self):
        """
        Clears the content of the text area.
        """
        self.text_area.delete("1.0", tk.END)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MorseTranslatorApp(root)
    root.mainloop()