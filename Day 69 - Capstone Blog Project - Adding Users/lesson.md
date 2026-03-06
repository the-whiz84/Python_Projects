# Day 69 - Relational Blog Users, Comments, and Admin Controls

Day 69 is the capstone of the Flask blog section. The earlier blog app already supported posts, editing, and deletion, but this version adds registered users, author ownership, comments, login-aware behavior, and admin-only routes. The result is no longer just a single-user blog editor. It is a small multi-user publishing system.

This lesson needs more explanation because it is really a synthesis lesson. Authentication, SQLAlchemy relationships, decorators, forms, and template logic are all working together here.

## 1. The Database Now Models Relationships Between Users and Content

The biggest architectural change is relational structure. The app defines three connected models:

```python
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author: Mapped["User"] = relationship(back_populates="posts")
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    ...
    comments: Mapped[list["Comment"]] = relationship(back_populates='parent_post')

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ...
    posts: Mapped[list["BlogPost"]] = relationship(back_populates='author')
    comments: Mapped[list["Comment"]] = relationship(back_populates='comment_author')

class Comment(db.Model):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
```

This is the heart of the capstone. The app is no longer storing isolated records. It is storing connected records:

- a user can author many posts
- a user can leave many comments
- a post can have many comments

That shift matters because it makes the blog multi-user in a real relational sense.

## 2. Foreign Keys and Relationships Let the Models Point at Each Other

The `author_id` and `post_id` columns are foreign keys, while the `relationship(...)` declarations tell SQLAlchemy how to navigate between related objects.

That means the code can do things like:

- `post.author.name`
- `comment.comment_author.email`
- `post.comments`

This is one of the biggest benefits of using an ORM for relational data. Once the relationships are configured, the application can work with connected Python objects rather than manually joining tables by hand in every route.

## 3. Registration Still Uses the Authentication Foundations from Day 68

The register route hashes the password and creates a new `User`:

```python
hashed_password = generate_password_hash(
    password=register_form.password.data,
    method="scrypt",
    salt_length=16
)
new_user = User(
    email=register_form.email.data,
    name=register_form.name.data,
    password=hashed_password
)
db.session.add(new_user)
db.session.commit()
login_user(new_user)
```

This is a good reminder that the capstone is built from earlier lessons rather than replacing them. Password hashing, duplicate-email checking, and `login_user()` all come directly from the authentication work in Day 68.

What changes now is what that authenticated user can do inside a richer application.

## 4. Login and `current_user` Now Affect the Blog's Behavior

Once a user is logged in, the app can use `current_user` in multiple places:

- associating a new post with its author
- associating a new comment with its author
- deciding whether to show admin controls

That is important because user identity is no longer only about protecting one secret page. It now shapes the behavior of the blog itself.

This is when authentication starts feeling like part of the product, not just part of the security layer.

## 5. Comments Turn the Blog into a Multi-User System

The `show_post` route now includes comment handling:

```python
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
```

This is one of the most important functional additions in the project. A blog post is no longer just static content. Other users can interact with it.

That means the data model now supports conversation, not only publishing.

## 6. Relationship Assignment Makes the Code More Expressive

Notice how the comment is created:

```python
new_comment = Comment(
    text=comment_form.comment_text.data,
    comment_author=current_user,
    parent_post=requested_post
)
```

This is a really nice SQLAlchemy example. The code is assigning related objects directly, not manually setting `author_id` and `post_id` integers. SQLAlchemy understands the relationships and handles the foreign key values under the hood.

That makes the code more readable and reinforces why relationship mapping is useful.

## 7. The `admin_only` Decorator Adds a Permission Layer

The app defines a custom decorator for admin-only routes:

```python
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        else:
            return abort(403)
    return decorated_function
```

This is an important step beyond `@login_required`. Logging in answers whether the user is authenticated. The admin decorator answers whether the authenticated user has permission to perform a privileged action.

That is a useful distinction to preserve in the lesson:

- authentication: are you logged in?
- authorization: are you allowed to do this?

The capstone needs both.

## 8. Admin Controls Affect Create, Edit, and Delete

The privileged routes are all protected:

```python
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    ...

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    ...

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    ...
```

That gives the blog a meaningful permission model. Regular users can register, log in, and comment. The admin controls the publishing interface.

This is a strong capstone design because it introduces role-aware behavior without making the authorization system overly complicated.

## 9. Template Logic Now Depends on the Logged-In User

The [post.html](/Users/wizard/Developer/Python_Projects/Day%2069%20-%20Capstone%20Blog%20Project%20-%20Adding%20Users/templates/post.html) template shows the edit button only for the admin:

```html
{% if current_user.id == 1 %}
<div class="d-flex justify-content-end mb-4">
  <a class="btn btn-primary float-right" href="{{url_for('edit_post', post_id=post.id)}}">Edit Post</a>
</div>
{% endif %}
```

This is a good example of the frontend reflecting backend permissions. The route protection is still the real security boundary, but the template also adapts the interface so the user sees only the actions that make sense for their role.

That improves usability and keeps the UI aligned with the permission model.

## 10. Gravatar Is a Nice Example of Derived User Presentation

The app generates avatar URLs from user emails:

```python
def gravatar_url(email, size=100, rating='g', default='retro', force_default=False):
    hash_value = sha256(email.lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_value}?s={size}&d={default}&r={rating}&f={force_default}"
```

Then the template uses it for comment authors:

```html
<img src="{{ gravatar_url(comment.comment_author.email) }}" />
```

This is a nice capstone detail because it shows how user data can be transformed into richer presentation without storing another file locally. It is a lightweight example of integrating external conventions into the app experience.

## 11. The Capstone Is Really About Putting the Pieces Together

Day 69 works because it combines several earlier course ideas into one coherent system:

- Flask routes and templates
- WTForms and CKEditor
- SQLAlchemy models and relationships
- Flask-Login sessions
- password hashing
- custom decorators for permissions
- Jinja conditionals for role-aware UI

That is why this lesson matters. It shows how the earlier isolated concepts become a real multi-user application when they are composed together.

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

Then test these flows:

- register a user
- log in and add a comment on a post
- confirm only the admin account can access `/new-post`
- confirm admin-only buttons appear only for the admin user

## Summary

Day 69 is the Flask capstone because it turns the blog into a relational multi-user system. Users can register and log in, posts belong to authors, comments belong to both posts and users, and admin-only decorators protect the publishing controls. The most important lesson is synthesis: authentication, ORM relationships, forms, and template logic now work together as one application rather than as separate exercises.
