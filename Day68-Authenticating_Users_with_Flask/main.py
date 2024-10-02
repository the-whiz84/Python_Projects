from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(250))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        error = None
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
        # User already exists
            error = "You've already signed up with that email, log in instead!"
            return render_template('login.html', error=error)
        else:
            hashed_password = generate_password_hash(
                password=request.form.get('password'), 
                method='scrypt', 
                salt_length=8
                )
            new_user = User(
                name=request.form.get('name'),
                email=request.form.get('email'),
                password=hashed_password
                )
            db.session.add(new_user)
            db.session.commit()
            # Log in and authenticate user after adding details to database.
            login_user(new_user)
            # Can redirect() and get name from the current_user
            return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        entered_email=request.form.get('email')
        entered_password=request.form.get('password')
        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == entered_email))
        user = result.scalar()
        if not user:
            error = "That email does not exist in the database, try again"
            return render_template('login.html', error=error)
        # Check stored password hash against entered password hashed.
        elif not check_password_hash(user.password, entered_password):
            error = "Password incorrect, try again"
            return render_template('login.html', error=error)
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Only logged-in users can down download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(port=5001)
