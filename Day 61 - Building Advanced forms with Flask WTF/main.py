from flask import Flask, render_template
import os
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[Email(message='Please enter a valid email address')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')



app = Flask(__name__)
bootstrap = Bootstrap5(app)


WTF_CSRF_SECRET_KEY = os.environ.get("FLASK_KEY")
app.secret_key = WTF_CSRF_SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == os.environ.get("ADMIN_EMAIL") and login_form.password.data == os.environ.get("ADMIN_PASSWORD"):
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
