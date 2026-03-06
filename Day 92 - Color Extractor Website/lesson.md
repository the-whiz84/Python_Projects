# Day 92 - Color Extraction, Image Uploads, and Flask UI Delivery

This project turns image analysis into a small Flask product. A user uploads an image, the app saves it, extracts a color palette, and renders those colors back into the page. The code is short, but it covers a complete web flow: form upload, file validation, storage, processing, and template rendering.

That makes it a good lesson in server-side image workflows.

## 1. Validate the Upload Before You Process It

The app starts with two important configuration values:

```python
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg"}
```

And a helper to enforce the extension policy:

```python
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )
```

That helper matters because uploads are one of the first places where a web app needs to become defensive. Even in a small demo project, it is worth checking that the filename looks like something the processing pipeline can handle.

## 2. Extract a Palette from the Saved Image

Once the file is accepted, the project delegates the color analysis to `ColorThief`:

```python
def extract_colors(image_path, num_colors=10):
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=num_colors)
    hex_colors = [
        "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2]) for color in palette
    ]
    return hex_colors
```

This helper is a good example of keeping the route thin. The Flask route should manage the request and the response. The actual image-processing logic belongs in a dedicated function.

The conversion to hex strings is especially useful because hex values are what templates and CSS can display directly.

## 3. Connect the Upload Request to the Template Response

The whole request flow lives in one route:

```python
@app.route("/", methods=["GET", "POST"])
def upload_file():
    colors = None
    filename = None
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(url_for("upload_file"))
        file = request.files["file"]
        if file.filename == "":
            return redirect(url_for("upload_file"))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            colors = extract_colors(filepath)
    return render_template("upload.html", colors=colors, filename=filename)
```

This route is doing exactly what a small Flask app should do:

- validate the request
- normalize the filename
- save the upload
- process the file
- render the result

The use of `secure_filename()` is also the right habit. Filenames from the browser should never be trusted as-is.

## 4. Let the App Prepare Its Own Storage Folder

At startup, the app ensures the upload directory exists:

```python
if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run()
```

That small check makes the project easier to run from a clean clone because the user does not need to create the folder manually first.

It is a small detail, but it improves the reliability of the whole workflow.

## How to Run the Color Extractor Website

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Flask app:
   ```bash
   python main.py
   ```
3. Open the local site, upload a `.png`, `.jpg`, or `.jpeg` file, and verify:
   - the file is saved into `static/uploads`
   - the dominant colors are extracted
   - the template renders the image and palette cleanly

## Summary

Today, you built a complete upload-and-process web flow. The app validates image extensions, saves the file, extracts a reusable color palette, and renders the result through Flask. The lesson is not only about color extraction. It is about how file uploads, backend processing, and template rendering fit together in a simple web product.
