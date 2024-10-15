import os
from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename
from colorthief import ColorThief

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg"}
Bootstrap5(app)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def extract_colors(image_path, num_colors=10):
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=num_colors)
    hex_colors = [
        "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2]) for color in palette
    ]
    return hex_colors


@app.route("/", methods=["GET", "POST"])
def upload_file():
    colors = None
    filename = None
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            colors = extract_colors(filepath)
    return render_template("upload.html", colors=colors, filename=filename)


if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run()
