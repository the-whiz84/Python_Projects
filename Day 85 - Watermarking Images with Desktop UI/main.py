import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QDragEnterEvent, QDropEvent
from PIL import Image
from pathlib import Path

# Constant for default save path (user's home directory / Pictures)
DEFAULT_SAVE_PATH = os.path.join(Path.home(), "Pictures")


class WatermarkApp(QWidget):
    def __init__(self):
        """Initialize the WatermarkApp window and layout."""
        super().__init__()
        self.initUI()

    def initUI(self):
        """Set up the user interface components and layout."""
        self.setWindowTitle("Watermark App")
        self.setGeometry(
            100, 100, 900, 700
        )  # Adjusted window size for better image display

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Styling for the image label and the layout
        self.setStyleSheet(
            """
            QLabel#DropLabel {
                border: 2px dashed #555;
                background-color: #f0f0f0;
                padding: 10px;  /* Reduced padding */
                color: #777;
                font-size: 16px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )

        # Label for drag and drop area
        self.drop_label = QLabel(
            'Drag an image here or use the "Select Image" button below.', self
        )
        self.drop_label.setObjectName("DropLabel")
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setFixedHeight(500)  # Increased height for better image display
        self.layout.addWidget(self.drop_label)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()

        # Button for manually selecting an image
        self.select_button = QPushButton("Select Image", self)
        self.select_button.clicked.connect(self.open_file_dialog)
        button_layout.addWidget(self.select_button)

        # Button to choose save location
        self.save_button = QPushButton("Choose Save Location", self)
        self.save_button.clicked.connect(self.choose_save_location)
        button_layout.addWidget(self.save_button)

        # Clear Button to remove the image
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_image)
        button_layout.addWidget(self.clear_button)

        self.layout.addLayout(button_layout)

        # Enable drag and drop
        self.setAcceptDrops(True)
        self.image_loaded = False  # Flag to track if an image is loaded
        self.save_path = DEFAULT_SAVE_PATH  # Default save path to the Pictures folder

    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle the drag event to accept image files."""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        """Handle the drop event to process the dropped image."""
        if event.mimeData().hasUrls():
            file_url = event.mimeData().urls()[0]
            file_path = file_url.toLocalFile()
            if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
                self.process_image(file_path)
            else:
                self.drop_label.setText(
                    "Unsupported file type. Please drop a .png, .jpg, or .jpeg file."
                )
        event.accept()

    def open_file_dialog(self):
        """Open a file dialog to manually select an image."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.process_image(file_path)

    def choose_save_location(self):
        """Choose a custom save location for the watermarked image."""
        chosen_folder = QFileDialog.getExistingDirectory(
            self, "Select Folder", DEFAULT_SAVE_PATH
        )
        if chosen_folder:
            self.save_path = chosen_folder
            print(f"Save path set to: {self.save_path}")
        else:
            print("No folder selected, using default save path.")

    def process_image(self, image_path):
        """Process the selected image by adding a watermark and save it to the specified path.

        Args:
            image_path (str): The path of the image to process.
        """
        # Load and process the image
        image = Image.open(image_path)
        image_width, image_height = image.size

        # Load the watermark image (change this to the path of your watermark image)
        watermark_path = "watermark.png"
        watermark = Image.open(watermark_path)

        # Resize the watermark to 15% of the image width
        watermark_ratio = 0.15
        watermark_width = int(image_width * watermark_ratio)
        watermark_height = int(watermark.height * (watermark_width / watermark.width))
        resized_watermark = watermark.resize((watermark_width, watermark_height))

        # Apply 75% transparency to the watermark
        watermark = resized_watermark.convert("RGBA")
        watermark_data = watermark.getdata()
        new_data = []
        for item in watermark_data:
            # Set alpha to 25% transparency (64 out of 255)
            new_data.append((item[0], item[1], item[2], int(item[3] * 0.25)))
        watermark.putdata(new_data)

        # Paste the watermark in the bottom-right corner
        image = image.convert("RGBA")
        image.paste(
            watermark,
            (image_width - watermark_width, image_height - watermark_height),
            watermark,
        )

        # Save the watermarked image in the selected path
        output_filename = f"{Path(image_path).stem}_watermarked.png"
        watermarked_image_path = os.path.join(self.save_path, output_filename)
        image.save(watermarked_image_path)

        # Show confirmation message
        QMessageBox.information(
            self, "Success", f"Watermarked image saved to:\n{watermarked_image_path}"
        )

        # Update the label to show the watermarked image
        self.show_image(watermarked_image_path)
        self.image_loaded = True  # Mark that an image is loaded

    def show_image(self, image_path):
        """Display the processed image in the label.

        Args:
            image_path (str): The path of the image to display.
        """
        # Load and display the image
        image = QImage(image_path)
        pixmap = QPixmap.fromImage(image)
        self.drop_label.setPixmap(
            pixmap.scaled(850, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )  # Increased size

    def clear_image(self):
        """Clear the displayed image and reset the label."""
        if self.image_loaded:
            self.drop_label.clear()
            self.drop_label.setText(
                'Drag an image here or use the "Select Image" button below.'
            )
            self.image_loaded = False


def main():
    """Run the Watermark App."""
    app = QApplication(sys.argv)
    window = WatermarkApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
