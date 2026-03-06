# Day 85 - Watermarking Images with Desktop UI

This project is a good example of desktop software that does one concrete job well: take an image, place a watermark in the bottom-right corner, and save the result. The folder even contains two UI implementations, one in PyQt and one in Tkinter, which makes the day more interesting than a single-script utility.

The main application path is the PyQt version in `main.py`.

## 1. Build a Desktop Workflow Around File Input

The PyQt app supports two ways to load an image:

- drag and drop
- manual file selection

The drag-and-drop path is handled through event methods:

```python
def dragEnterEvent(self, event: QDragEnterEvent):
    if event.mimeData().hasUrls():
        event.accept()
    else:
        event.ignore()
```

and:

```python
def dropEvent(self, event: QDropEvent):
    file_url = event.mimeData().urls()[0]
    file_path = file_url.toLocalFile()
    if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        self.process_image(file_path)
```

That dual input model is what makes the app feel like a real desktop tool instead of just a script with a button.

## 2. Resize and Blend the Watermark Intelligently

The actual image-processing logic happens in `process_image()`:

```python
image = Image.open(image_path)
image_width, image_height = image.size

watermark_path = "watermark.png"
watermark = Image.open(watermark_path)
```

The watermark is then resized relative to the image width:

```python
watermark_ratio = 0.15
watermark_width = int(image_width * watermark_ratio)
watermark_height = int(watermark.height * (watermark_width / watermark.width))
resized_watermark = watermark.resize((watermark_width, watermark_height))
```

This is a better design than hardcoding a fixed watermark size. A watermark that works on a small image will look tiny on a large one unless you scale it proportionally.

The code also applies transparency by rewriting the alpha channel:

```python
watermark = resized_watermark.convert("RGBA")
watermark_data = watermark.getdata()
new_data = []
for item in watermark_data:
    new_data.append((item[0], item[1], item[2], int(item[3] * 0.25)))
watermark.putdata(new_data)
```

That keeps the watermark visible without dominating the original image.

## 3. Save the Result as a New Artifact

Once the watermark is ready, the app pastes it into the image and saves a new file:

```python
image = image.convert("RGBA")
image.paste(
    watermark,
    (image_width - watermark_width, image_height - watermark_height),
    watermark,
)

output_filename = f"{Path(image_path).stem}_watermarked.png"
watermarked_image_path = os.path.join(self.save_path, output_filename)
image.save(watermarked_image_path)
```

This is a sensible workflow because it preserves the original file and writes a derived output with a predictable suffix.

The app also lets the user choose the save location, which turns a one-off script into something closer to a reusable desktop utility.

## 4. Compare the Two UI Approaches in the Folder

There is also a second implementation in `main_tkinter.py`. It uses drag-and-drop via `TkinterDnD`, applies the same basic watermarking idea, and previews the result inside a Tkinter frame.

That makes the folder useful beyond the main app. You can compare the same product idea across two GUI frameworks:

- PyQt version with a more polished desktop feel
- Tkinter version with a lighter-weight approach

This is a useful engineering lesson. The image-processing core is portable even when the UI framework changes.

## How to Run the Watermark App

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main PyQt application:
   ```bash
   python main.py
   ```
3. Drag an image into the window or use `Select Image`.
4. Optionally choose a custom save folder, then confirm the watermarked file is created with the `_watermarked` suffix.

## Summary

Today, you built a real desktop image workflow rather than a pure command-line script. The project scales the watermark to the image, applies alpha blending, saves a derived output, and wraps the whole process in a drag-and-drop UI. The bigger lesson is that a small amount of image processing becomes much more useful once it is embedded in a clear user flow.
