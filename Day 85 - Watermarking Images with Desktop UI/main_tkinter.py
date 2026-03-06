import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES  # For drag and drop functionality
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
from pathlib import Path
import os


class WatermarkApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("Watermark App")
        self.geometry("800x600")

        # Label for instructions
        self.label = tk.Label(
            self,
            text="Drag and drop an image here, or use the button below",
            font=("Arial", 14),
        )
        self.label.pack(pady=10)

        # Add a frame to show the dropped or selected image
        self.image_frame = tk.Frame(self, width=400, height=400, bg="gray")
        self.image_frame.pack(expand=True, fill="both")

        # Add a button for selecting images manually
        self.select_button = tk.Button(
            self, text="Select Image", command=self.select_image
        )
        self.select_button.pack(pady=10)

        # Allow dragging and dropping files
        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.on_drop)

        # Store the watermark image (assumed transparent PNG)
        self.watermark = Image.open("watermark.png")

    def on_drop(self, event):
        file_path = event.data.strip("{}")
        self.process_image(file_path)

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")],
            defaultextension=".jpg",
            initialdir=os.path.expanduser("~"),  # Start in the user's home directory
        )
        if file_path:
            self.process_image(file_path)

    def process_image(self, image_path):
        # Ensure it's an image file
        if image_path.lower().endswith((".png", ".jpg", ".jpeg")):
            self.add_watermark(image_path)
        else:
            messagebox.showerror("Invalid File", "Please select a valid image file.")

    def add_watermark(self, image_path):
        # Open the image
        image = Image.open(image_path)
        image_width, image_height = image.size

        # Resize the watermark to 15% of the image width
        watermark_ratio = 0.15
        watermark_width = int(image_width * watermark_ratio)
        watermark_height = int(
            self.watermark.height * (watermark_width / self.watermark.width)
        )
        resized_watermark = self.watermark.resize((watermark_width, watermark_height))

        # Apply 75% transparency to the watermark
        watermark = resized_watermark.convert("RGBA")
        watermark_data = watermark.getdata()
        new_data = []
        for item in watermark_data:
            # Change alpha to 50% transparency (128 out of 255)
            new_data.append((item[0], item[1], item[2], int(item[3] * 0.25)))

        watermark.putdata(new_data)

        # Paste the watermark in the bottom-right corner
        image = image.convert("RGBA")
        image.paste(
            watermark,
            (image_width - watermark_width, image_height - watermark_height),
            watermark,
        )

        # Save the watermarked image
        watermarked_image_path = Path(image_path).stem + "_watermarked.png"
        image.save(watermarked_image_path)

        # Display the watermarked image in the frame
        img = ImageTk.PhotoImage(image.resize((600, 400)))
        img_label = tk.Label(self.image_frame, image=img)
        img_label.image = img  # Keep a reference to avoid garbage collection
        img_label.pack()

        # Update the label to notify success
        self.label.config(text=f"Watermarked image saved as {watermarked_image_path}")


if __name__ == "__main__":
    app = WatermarkApp()
    app.mainloop()
