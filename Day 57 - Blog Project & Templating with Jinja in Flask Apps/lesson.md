# 1. URL building and templating with Jinja

# Jinja is a templating language built for Python. It is bundled with the Flask framework.
# It uses specific syntax that can specify inside the HTML file which part is evaluated as Python code.

<body>
    <h1>3 * 5</h1>
</body>
# It will just render an H1 with the string


<body>
    <h1>{{ 3 * 5 }}</h1>
</body>
# It will be interpreted as Python code and will render an H1 with the string 15.


<body>
    <h1 style="text-align: center;color: blue;">Hello World!</h1>
    <h2>{{ 5 * 6 }}</h2>
    <h3>Random number: {{ num }}</h3>
</body>

# if we neeed an import like random, we need to write our code inside server.py instead of index.html
@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)

# render_template function accepts **kwargs after the location of the file, so we can give it as many arguments as we want.
# We need to specify a name and a value for them so we can refer to them in our html file.


# 2. Multiline Statements with Jinja

# When we have a multiline statement, we need to use {% for beggining of each line that is not HTML and %} for the end of each line.
# To specify the end of the multi line statement we use {% endfor %}

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url).json()
    
    return render_template("blog.html", posts=blog_response)

<body>
    {% for blog_post in posts: %}
        <h1>{{ blog_post["title"] }}</h1>
        <h2>{{ blog_post["subtitle"] }}</h2>
    {% endfor %}
</body>


# Same with if statements

{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny!  You bastard!!!
{% else %}
    Kenny looks okay --- so far
{% endif %}

https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-control-structures


# 3. URL building with Flask

# To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule.

<body>
    <h1 style="text-align: center;color: blue;">Hello World!</h1>
    <h2>{{ 5 * 6 }}</h2>
    <h3>Random Number: {{ num }}</h3>
    <a href="{{ url_for('get_blog') }}">Go to Blog</a>
</body>

