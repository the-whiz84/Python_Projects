# Day 67 - RESTful Blog: Building a Professional CMS

Yesterday, we built a pure Data API. Today, we bring those RESTful principles back to the browser. We are building a professional **Content Management System (CMS)**.

No more "hardcoding" posts. We implemented **Rich Text Editing**, **Dynamic Route Parameterization**, and the most efficient architectural pattern in Flask: **Form Reuse**.

## 1. CKEditor: The Rich Text Pipeline

In professional blogging, users expect to format text with **Bold**, _Italics_, Lists, and Hyperlinks. A standard HTML `<textarea>` can't do this.

We integrated **CKEditor**, an industrial-grade "What You See Is What You Get" (WYSIWYG) editor.

- **Frontend**: CKEditor injects a JavaScript-powered toolbar into the page.
- **Backend**: We use the `CKEditorField` in WTForms.
- **The Pipe**: When the user clicks "Submit", CKEditor converts the formatted text into raw HTML strings and sends them to Flask. Flask then saves this HTML directly into our database's `Text` column.

## 2. DRY Architecture: The "Form Reuse" Pattern

One of the most powerful ways to keep your code **DRY (Don't Repeat Yourself)** is to use the same WTForm class and the same HTML template for both **Creating** and **Updating** resources.

In `main.py`, we implemented this by passing a flag to the template:

```python
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    # 1. Pre-populate the form with existing data
    edit_form = PostForm(
        title=post.title,
        body=post.body,
        # ...
    )
    # 2. Logic to distinguish between "Create" (POST) and "Initial Load" (GET)
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        # ... update ...
        db.session.commit()

    # 3. Pass is_edit=True so the same template knows to show "Edit Post" header
    return render_template("make-post.html", form=edit_form, is_edit=True)
```

By reusing `make-post.html`, we ensure that any UI changes (like adding a new field) only need to be made in one file, reducing the risk of bugs and maintainability debt.

## 3. Dynamic Routing: The ID Pattern

Professional websites don't have routes like `/post1`, `/post2`. They use **Dynamic Path Variables**.

```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=post)
```

The `<int:post_id>` part tells Flask: "Any number that comes after `/post/` should be captured and passed into my function as a variable." This allows one single route to handle millions of different blog posts dynamically.

## How to Run the RESTful Blog

1.  **Dependencies**:
    ```bash
    pip install Flask Flask-Bootstrap Flask-CKEditor Flask-SQLAlchemy Flask-WTF
    ```
2.  **Run**:
    ```bash
    python main.py
    ```
3.  **Interaction**:
    - Visit `http://127.0.0.1:5003/`.
    - Use the "Create New Post" button to see the CKEditor in action.
    - Submit the post and click the "Edit" button to verify the **Form Reuse** pattern populates the data correctly.

## Summary

Today, you transitioned from building "Pages" to building a "Platform." You learned how to handle complex Rich Text data, how to reuse logic for Create/Update operations to keep your code DRY, and how to use dynamic path variables to scale your routing architecture.

Tomorrow, we tackle the final challenge of any professional app: **Security**. We'll learn how to keep unauthorized users away from your "Delete" buttons by adding a full Login system!
