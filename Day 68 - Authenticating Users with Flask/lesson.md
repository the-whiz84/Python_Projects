# Day 68 - Authentication: The Mechanics of Security

Yesterday, we built a functional blog, but it had a fatal flaw: anyone with the URL could edit your database. Today, we implement **Authentication** and **Authorization**—the two pillars of security.

We moved beyond simple "passwords" to industry-standard **Salting and Hashing** to ensure that even if our database was stolen, our users' data remains encrypted and safe.

## 1. The Mathematics of Hashing: Why MD5 is Dead

Modern security is a "one-way street." You should **never** store a user's password in plain text.
We use **Hashing**—a mathematical algorithm that turns any input into a unique, fixed-length "fingerprint" called a hash.

- **Encryption (Two-Way)**: You can "unscramble" it with a key.
- **Hashing (One-Way)**: You can _never_ un-hash it.

**The Modern Standard: Scrypt**:
In `main.py`, we used the `scrypt` method via the `Werkzeug` library. Unlike older algorithms (like MD5 or SHA-1), Scrypt is designed to be "expensive" for a computer to run. This prevents hackers from using massive supercomputers to "guess" millions of passwords per second (**Brute Force**).

## 2. Salting: Defeating "Rainbow Tables"

If ten users choose the password `password123`, they would all have the exact same hash fingerprint in your database. A hacker could use a pre-computed list of common hashes (**Rainbow Tables**) to instantly unmask them.

To fix this, we use **Salting**:

```python
hashed_password = generate_password_hash(
    password="my_password",
    method='scrypt',
    salt_length=16 # 16 characters of random noise added before hashing
)
```

By adding 16 characters of random "salt" to every password _before_ hashing, every user gets a unique fingerprint, even if their passwords are identical.

## 3. Session Management: Cookies and Claims

How does the server know you're still "logged in" when you go from the Login page to the Secrets page?

- **The Login Manager**: Flask-Login acts as a referee. When you log in, it gives your browser a **Session Cookie**.
- **The Cookie**: It's a small file stored on your computer. With every subsequent click, your browser sends this cookie back to the server.
- **The User Loader**: Flask-Login takes the ID from that cookie and calls our `user_loader` function to reconstruct the `current_user` object from the database.

## 4. Authentication vs. Authorization

- **Authentication**: "Are you who you say you are?" (Log in).
- **Authorization**: "Are you allowed to do this?" (Permissions).

We use the `@login_required` decorator to enforce authorization. If a logged-out user tries to access `/secrets`, the decorator intercepts them and redirects them to `/login` before the function even runs.

## How to Run the Authenticated App

1.  **Environment Configuration**:
    Authentication relies on a `FLASK_KEY` to sign session cookies. Never leave this blank!
    ```bash
    export FLASK_KEY="antigravity_security_protocol"
    ```
2.  **Dependencies**:
    ```bash
    pip install flask-login flask-sqlalchemy werkzeug
    ```
3.  **Run**:
    ```bash
    python main.py
    ```
4.  **Security Testing**:
    - Try to visit `http://127.0.0.1:5001/secrets` while logged out.
    - Verify that you are redirected to `/login`.
    - Register a user and verify that password in `users.db` is a long, scrambled Scrypt hash, not your plain text password.

## Summary

Today, you learned the difference between Hashing and Encryption, the necessity of Salting to prevent dictionary attacks, and the mechanics of Session management in web environments. You have evolved from a "Web Dev" to a "Security-Minded Developer."

Tomorrow, we combine everything—DBs, APIs, and Authentication—into our massive **Capstone Blog Project!**
