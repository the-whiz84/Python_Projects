from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        password = request.form['password']
        return render_template('login.html', name=user_name, passwd=password)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


