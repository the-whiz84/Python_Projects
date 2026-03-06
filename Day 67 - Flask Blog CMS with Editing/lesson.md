# Day 67 - Flask Blog CMS with Editing and Rich Text

Day 67 takes the earlier blog work and turns it into something closer to a small content management system. The app no longer just displays posts from a static data source or a simple database table. It now lets the user create posts, edit existing ones, delete entries, and write post bodies with a rich text editor.

This lesson deserves more depth because it combines several important ideas at once: database-backed blog posts, reusable form flows, route-driven CRUD operations, and rich text content stored in the database. By this point, the Flask projects are no longer simple demos. They are starting to behave like full applications.

## 1. The Blog Post Model Becomes the Core Content Object

The application defines a `BlogPost` model with the fields needed for a full article:

```python
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
```

This is worth highlighting because the app is now centered around one content model that supports a full publishing workflow. The `Text` type for `body` is especially important, since blog content is longer and more variable than the short form fields we handled in earlier lessons.

That change makes the app feel like a real content system rather than a form demo.

## 2. The Homepage Becomes a Database-Driven Post Index

The root route queries all posts and renders them on the homepage:

```python
@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars().all()
    return render_template("index.html", all_posts=posts)
```

This is a good example of how the blog architecture has matured. The homepage is not hand-built and it is not driven by static JSON. It is a live view of the current database state.

That means every create, edit, or delete action affects what the homepage shows next. The page is now a real read view on top of persistent application data.

## 3. Dynamic Routes Drive Individual Post Pages

Each post has its own detail route:

```python
@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)
```

This is a familiar Flask pattern by now, but it matters more here because the posts are user-created records. A single route structure can serve any article as long as the database contains it.

This is one of the strengths of model-driven Flask apps:

- the route pattern stays stable
- the database content changes over time
- the templates render whatever records exist

## 4. Rich Text Editing Changes What the Form Can Store

The `PostForm` uses `CKEditorField` for the post body:

```python
class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Enter your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')
```

This is a significant step forward from plain text input. A blog post body is not just a short string. It often needs paragraphs, formatting, links, and other rich content. CKEditor makes that possible by providing a WYSIWYG editing interface in the browser.

The important concept here is that the editor generates HTML content, and the app stores that HTML in the database. That means the database is not only storing plain text anymore. It is storing rendered content fragments that the template can later display as article content.

## 5. Creating a Post Follows the Standard Form-to-Database Pattern

The `/new_post` route handles creation:

```python
@app.route("/new_post", methods=['GET', 'POST'])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)
```

This route is useful because it combines many ideas already built in earlier lessons:

- Flask-WTF handles the form structure and validation
- the form fields become model attributes
- SQLAlchemy persists the new record
- the user is redirected back to the main listing

So Day 67 is not inventing an entirely new pattern. It is combining earlier patterns into a stronger application workflow.

## 6. Edit and Create Reuse the Same Form Class

The edit route uses the same `PostForm` class:

```python
edit_form = PostForm(
    title=post.title,
    subtitle=post.subtitle,
    img_url=post.img_url,
    author=post.author,
    body=post.body
)
```

This is a great design choice because the same data shape is needed for both creating and editing a post. Reusing the form class means the validation rules and field definitions stay consistent across both flows.

That is a good architectural lesson: if create and edit share the same fields, they should usually share the same form definition too.

## 7. The Template Is Reused for Both New and Edit Flows

The app also reuses the same `make-post.html` template for both operations. The template checks an `is_edit` flag:

```html
{% if is_edit %}
  <h1>Edit Post</h1>
{% else %}
  <h1>New Post</h1>
{% endif %}
```

This is one of the more important maintainability improvements in the project. Instead of maintaining separate templates for "new post" and "edit post," the app keeps one shared page and changes only the few parts that need to differ.

That reduces duplication in the same way shared partials reduced duplication in the earlier blog templates.

## 8. The Edit Route Updates an Existing Database Record

The `/edit-post/<int:post_id>` route loads a record, pre-fills the form, and writes updates back into the same object:

```python
if edit_form.validate_on_submit():
    post.title = edit_form.title.data
    post.subtitle = edit_form.subtitle.data
    post.date = date.today().strftime("%B %d, %Y")
    post.body = edit_form.body.data
    post.author = edit_form.author.data
    post.img_url = edit_form.img_url.data
    db.session.commit()
    return redirect(url_for('show_post', post_id=post_id))
```

This shows another useful ORM pattern. Editing a record is not about creating a replacement object. It is about loading the existing row, mutating its fields, and committing the session.

Because the create and edit forms share the same structure, the code paths stay conceptually aligned even though one creates and the other updates.

## 9. Delete Completes the CMS Workflow

The delete route makes the blog fully manageable:

```python
@app.route("/delete/<int:post_id>", methods=['GET', 'POST'])
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
```

At this point the app supports the full article lifecycle:

- list posts
- view one post
- create a new post
- edit an existing post
- delete a post

That is why calling this a small CMS is fair. The application now supports content management, not just content display.

## 10. CKEditor Integration Shows How Frontend Tools Can Feed Backend Storage

The template loads CKEditor with:

```html
{{ ckeditor.load() }}
{{ ckeditor.config(name='body') }}
```

This is worth emphasizing because it shows another important full-stack idea. A JavaScript-based browser tool can be integrated into a Flask form and still fit cleanly into the backend workflow. The frontend editor handles the writing experience, while the backend stores the submitted HTML content in the model.

That kind of division of responsibility becomes more common as the projects grow.

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

Then visit:

- `http://127.0.0.1:5003/`
- `http://127.0.0.1:5003/new_post`

Create a post, edit it, and then delete it to verify the full workflow.

## Summary

Day 67 turns the Flask blog into a small content management system. SQLAlchemy stores full blog posts, Flask-WTF handles the post form, CKEditor upgrades the body field to rich text, and the same form/template structure is reused for both creating and editing entries. The key lesson is application composition: earlier Flask, database, and form patterns are now working together in a single CRUD publishing workflow.
