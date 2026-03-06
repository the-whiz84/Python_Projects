# Day 62 - CSV Persistence and Form Workflows in Flask

Day 62 takes the form work from the previous lessons and adds persistence. Until now, user input mostly affected the current response, but the data did not survive beyond the request unless you manually sent it somewhere else. In this project, the submitted cafe data is written into a CSV file and later read back into the application for display.

That makes this lesson an important bridge between forms and databases. CSV is not a full database system, but it introduces the same basic idea: user input can be validated, stored, and loaded again later.

## 1. The Form Still Defines the Input Schema

The `CafeForm` class describes the data the application expects:

```python
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField("Cafe Location on Google Maps (URL)", validators=[URL(), DataRequired()])
    open_time = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')
```

This is a useful continuation of the Flask-WTF pattern. The form class is doing more than building inputs. It is defining the data shape for the application.

That matters more now because the data is about to be stored. Once user input becomes persistent, the quality and consistency of the input matters much more.

## 2. `SelectField` Helps Keep Stored Data Consistent

The rating fields are especially interesting because they use `SelectField` instead of free text:

```python
coffee_rating = SelectField("Coffee Rating", choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
```

This is a good design choice worth explaining. If users could type anything they wanted, the stored data would quickly become messy and inconsistent. By constraining input to predefined choices, the app keeps the CSV cleaner and easier to display later.

That is a general data-design lesson: when the application will store values long term, narrowing the allowed input can be just as important as validating it.

## 3. CSV Is a Simple Form of Persistence

The project writes new data into `cafe-data.csv`:

```python
with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
    csv_file.write(
        f"\n{form.cafe.data},"
        f"{form.location.data},"
        f"{form.open_time.data},"
        f"{form.closing_time.data},"
        f"{form.coffee_rating.data},"
        f"{form.wifi_rating.data},"
        f"{form.power_rating.data}"
    )
```

This is where the lesson really shifts from form handling into persistence. The application is serializing validated Python values into plain text and appending them to a file.

CSV is simple, but it teaches several useful ideas:

- data can outlive the request that created it
- stored data has to be written in a consistent format
- future code has to be able to read it back again

That is why this lesson works well as a transition before databases.

## 4. `validate_on_submit()` Protects the Write Step

The CSV write happens only inside:

```python
if form.validate_on_submit():
```

This matters because persistence raises the cost of bad input. If invalid data is only displayed for one request, it is annoying. If invalid data is written into a persistent store, it becomes part of the application's long-term state.

So Day 62 reinforces an important full-stack pattern:

1. validate input first
2. write it only after validation passes

That sequence is much safer than accepting anything and trying to clean it later.

## 5. Redirecting After a Successful POST Is a Good Pattern

After writing the new row, the route does this:

```python
return redirect(url_for('cafes'))
```

This is a good moment for a little general web theory. Redirecting after a successful form submission is a common pattern because it moves the user away from the POST request and onto a normal GET page.

That has two practical benefits:

- it gives the user a natural next page to view
- it reduces the chance of accidental re-submission if the user refreshes

This is often called the Post/Redirect/Get pattern, and it is worth understanding early because it appears in many Flask apps.

## 6. Reading the CSV Back In Completes the Cycle

The `/cafes` route reads the file back into memory:

```python
with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
return render_template('cafes.html', cafes=list_of_rows)
```

This is the second half of persistence. The app is not only saving records. It is also deserializing them so they can be rendered again.

That round trip is the real lesson:

- form data enters the app
- the data is validated
- the data is stored
- the stored data is loaded and displayed

Once you can see that full loop, moving to SQLite later feels natural instead of abrupt.

## 7. The Template Displays Tabular Data with Jinja

The [cafes.html](/Users/wizard/Developer/Python_Projects/Day%2062%20-%20Flask,%20WTForms,%20Bootstrap%20and%20CSV/templates/cafes.html) template loops through the rows and columns:

```html
{% for row in cafes %}
<tr>
  {% for item in row %}
    {% if item[0:4] == "http" %}
      <td><a href="{{ item }}">Maps Link</a></td>
    {% else %}
      <td>{{ item }}</td>
    {% endif %}
  {% endfor %}
</tr>
{% endfor %}
```

This is a useful Jinja example because the template is now doing simple presentation logic:

- loop over rows
- loop over fields inside each row
- render URLs differently from ordinary text

That keeps the route simple while still giving the page a readable table output.

## 8. The Project Shows the Limits of Flat Files

CSV is useful here, but the lesson also quietly shows why databases exist. The application writes rows by concatenating strings, assumes the order of fields, and loads the file back as raw lists.

That is acceptable for a small practice project, but it becomes awkward as the app grows. There is no query language, no schema enforcement, and no convenient way to update one record cleanly.

That is exactly why this lesson works so well before SQLite. It lets you feel both the value of persistence and the limitations of flat-file storage.

## 9. This Lesson Is Really About Moving from Input to Storage

The bigger idea in Day 62 is that form handling is no longer only about the current response. The application now has a storage layer, even if it is a simple one. That changes the role of validation, redirects, and rendering.

The app now behaves more like a stateful system:

- users submit new records
- records remain available afterward
- another route can display the accumulated data

That is a major step forward in the course.

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Set the secret key:

```bash
export FLASK_KEY="your_secret_key"
```

Run the app:

```bash
python main.py
```

Then visit:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/add`
- `http://127.0.0.1:5000/cafes`

Submit a new cafe, then open `cafe-data.csv` to see the appended row directly.

## Summary

Day 62 connects validated user input to persistent storage. Flask-WTF defines the schema, the form route writes validated values into a CSV file, and a second route reads that data back for display in a Bootstrap-styled table. The lesson introduces the full cycle of data entry, storage, and retrieval, which makes it the natural stepping stone toward real databases.
