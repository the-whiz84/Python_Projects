# Day 68 - User Authentication with Flask-Login and Password Hashing

Day 68 adds one of the most important capabilities in the Flask section: user authentication. The app now supports registration, login, logout, protected routes, and access-controlled file downloads. That means the application is no longer only about data and templates. It now has user identity and session state.

This lesson benefits from keeping the security theory, because authentication is one of those topics where the "why" matters as much as the syntax. Password hashing, session cookies, and route protection are all foundational ideas that show up in real web applications.

## 1. The User Model Introduces Identity into the App

The project defines a `User` model that inherits from both `UserMixin` and `db.Model`:

```python
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(250))
    name: Mapped[str] = mapped_column(String(1000))
```

This is an important step because the app now has a persistent representation of a person, not just content. Once a user table exists, the rest of the application can start making decisions based on who is logged in.

That shift matters later in the course when user-specific ownership and permissions become part of the application design.

## 2. Passwords Are Hashed Before They Reach the Database

The registration route does not store the raw password:

```python
hashed_password = generate_password_hash(
    password=request.form.get('password'),
    method='scrypt',
    salt_length=8
)
```

This is a key security idea. The app never needs to know the original password again after registration. Instead, it stores a hash.

That distinction is worth keeping clear:

- plain-text storage is unsafe
- hashing stores a derived value instead of the original password
- login later works by checking whether a new password input produces a matching result

This is why password hashing is a standard security practice rather than an optional upgrade.

## 3. Salting Makes Identical Passwords Produce Different Stored Values

The `salt_length=8` argument matters because it means the hashing process includes random salt data. That helps protect against precomputed lookup attacks and makes duplicate user passwords less obvious in the stored database.

The big idea is simple: even if two users choose the same password, the stored result should not look identical.

That is one of the reasons modern password-storage helpers are so useful. They bundle the important security details into a safer default workflow.

## 4. Login Checks a Password Against the Stored Hash

The login route verifies the submitted password like this:

```python
elif not check_password_hash(user.password, entered_password):
    error = "Password incorrect, try again"
    return render_template('login.html', error=error)
else:
    login_user(user)
    return redirect(url_for('secrets'))
```

This is another important conceptual point. The app does not decrypt anything. It compares the entered password against the stored hash using a verification helper.

That is the normal login pattern in secure web apps:

1. look up the user by email
2. check the submitted password against the stored hash
3. establish a logged-in session if the check passes

## 5. Flask-Login Handles Session State

The app sets up Flask-Login with a login manager and user loader:

```python
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)
```

This is where authentication becomes more than one route. Flask-Login needs a way to rebuild the current user from the session data stored by the browser.

That is what the `user_loader` function does. When Flask-Login sees a remembered user ID in the session, it uses this function to load the corresponding user record from the database.

This is one of the core session-management ideas in Flask applications.

## 6. `login_user()` Marks the User as Authenticated

When registration or login succeeds, the app calls:

```python
login_user(new_user)
```

or:

```python
login_user(user)
```

This is the point where the app transitions from "credentials were correct" to "this browser now has an authenticated session." Flask-Login handles the session cookie machinery behind the scenes, while the app code stays focused on the user flow.

That is a good design tradeoff. Security-sensitive session handling is delegated to a well-known library rather than reinvented manually.

## 7. `@login_required` Protects Routes from Anonymous Access

The project guards the private routes with `@login_required`:

```python
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)
```

and:

```python
@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')
```

This is an important distinction between authentication and authorization.

- authentication answers: who is this user?
- authorization answers: may this user access this route?

In this project, the authorization rule is simple: only logged-in users may access the secrets page or the protected download.

## 8. `current_user` Makes the Logged-In Identity Available in Views

The secrets page route uses:

```python
current_user.name
```

This is a small line, but it shows the main payoff of authentication. Once the user is logged in, the application can personalize behavior and content based on the active identity.

That is what turns authentication from a pure security feature into an application feature. The app can now distinguish one user from another and respond accordingly.

## 9. Registration and Login Also Need Good Failure Paths

The app handles two important failure cases:

- login with an email that does not exist
- login with a wrong password

It also prevents duplicate registration by checking whether the email is already present before creating a new account.

That matters because authentication is not only about the success path. Clear error handling is part of making the flow usable and secure. The app should fail deliberately, not accidentally.

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Set the Flask secret key:

```bash
export FLASK_KEY="your_secret_key"
```

Run the app:

```bash
python main.py
```

Then test these routes:

- `http://127.0.0.1:5001/`
- `http://127.0.0.1:5001/register`
- `http://127.0.0.1:5001/login`
- `http://127.0.0.1:5001/secrets`
- `http://127.0.0.1:5001/download`

Try opening the protected routes before logging in so you can see the route protection behavior.

## Summary

Day 68 introduces full user authentication in Flask. The app stores hashed passwords instead of raw ones, verifies login attempts with `check_password_hash()`, creates authenticated sessions with Flask-Login, and protects private routes with `@login_required`. The key lesson is that authentication is both a security system and an application feature: it protects resources while also letting the app know who the current user is.
