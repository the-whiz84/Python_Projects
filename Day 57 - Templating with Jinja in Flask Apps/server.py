from flask import Flask, render_template
import random, requests
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    your_name = "Radu Chiriac"
    return render_template("index.html", num=random_number, year=current_year, name=your_name)


@app.route("/guess/<name>")
def guess(name):
    gender_data = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = gender_data["gender"]
    age_data = requests.get(f"https://api.agify.io?name={name}").json()
    age = age_data["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url).json()
    
    return render_template("blog.html", posts=blog_response)



if __name__ == "__main__":
    app.run(debug=True)
