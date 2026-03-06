# Day 69 - Capstone: The Relational Blog Architecture

Congratulations on reaching the summit of the Flask module! Over the last 15 days, you have transitioned from returning simple strings to building a collaborative, secure **Content Management System (CMS)**.

Today's Capstone project focuses on the final, most complex piece of the puzzle: **Relational Database Design**.

## 1. Relational Architecture: One-to-Many

In our previous projects, our tables were independent "islands." Today, we built bridges between them. We implemented **One-to-Many Relationships** (also called 1:N):

- **User <-> BlogPost**: One user (author) can write many posts.
- **User <-> Comment**: One user can leave many comments.
- **BlogPost <-> Comment**: One blog post can have many comments.

In SQLAlchemy, we achieve this through **Foreign Keys** and **Back-Populates**:

```python
class BlogPost(db.Model):
    # This ID links specifically to the 'id' column in the 'users' table
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # This allows us to call 'post.author' and get the full User object
    author: Mapped["User"] = relationship(back_populates="posts")
```

This relational design prevents data duplication. We don't save the author's name in the `blog_posts` table; we save their `author_id`. If the author changes their name in the `users` table, it is automatically updated across every single blog post they've ever written!

## 2. Granular Authorization: Custom Admin Decorators

Sometimes, `@login_required` is too broad. We need to differentiate between a **Member** and an **Admin**. We implemented **Role-Based Access Control (RBAC)** using custom Python decorators.

```python
from functools import wraps

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # We explicitly check for the 'Admin' ID (usually ID 1)
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403) # Return "Forbidden"
        return f(*args, **kwargs)
    return decorated_function
```

By stacking decorators (e.g., `@app.route` -> `@admin_only`), we create a "Guard" for our sensitive routes (Edit/Delete). The function inside only runs if the user passes the Admin check first.

## 3. UI/UX Polishing: Gravatar and Context

Professional applications shouldn't force users to upload profile pictures. We integrated **Gravatar**—a global service that provides profile pictures based on an MD5/SHA256 hash of a user's email address.

This teaches a crucial lesson in **UI Logic**: Instead of storing images on our server (which is slow and expensive), we generate a dynamic URL on-the-fly in the template:

```jinja
<img src="{{ gravatar_url(comment.comment_author.email) }}">
```

## How to Run the Capstone Blog

1.  **Dependencies**:
    ```bash
    pip install flask flask-sqlalchemy flask-login flask-ckeditor flask-bootstrap
    ```
2.  **Run**:
    ```bash
    python main.py
    ```
3.  **The Capstone Test**:
    - **Step 1**: Register a new user. You are ID #2. Verify you can read posts and leave comments but **cannot** see "Edit" or "Delete" buttons.
    - **Step 2**: Check `blog.db` with a viewer. Notice how the `posts` and `comments` tables now contain `author_id` and `post_id` links.
    - **Step 3**: Verify that only the user with ID #1 (the first user registered) can access the `/new-post` route.

## Summary: The Flask Masterclass

You have successfully built a full-stack platform involving:

- **Relational Database Design** (Solving 1:N links).
- **Custom Decorators** (Building a security middleware).
- **External Integration** (Using Gravatar for automated avatars).
- **Template Logic** (Dynamic UI based on user roles).

Tomorrow, we move from the Web to the Terminal to master **Git**—the version control system that will safeguard all the complex code you've written this month!
