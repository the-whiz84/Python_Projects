import requests, os, smtplib
from flask import Flask, render_template, request

MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASSWD = os.environ.get("MY_EMAIL_PASSWD")

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/7355269ada93b9890800").json()
# Replace with your own api URL


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message from Contact Form\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, EMAIL_PASSWD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

if __name__ == "__main__":
    app.run()