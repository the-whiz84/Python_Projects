# 1. Flask URL Paths and the Flask Debugger

# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. 

@app.route("/username/<name>")
def greet(name):
    return f"<p>Hello, {name}!</p>"

http://127.0.0.1:5000/username/Radu
Hello, Radu!

# We can notice that if we update the code, we need to stop and restart the server to see the changes.
# Flask has a Debug Mode that is by default set to OFF. 
# By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request.

To enable all development features, set the FLASK_ENV environment variable to development before calling flask run.

if __name__ == "__main__":
    app.run(debug=True)

# Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

Converter types:

string  - (default) accepts any text without a slash
int     - accepts positive integers
float   - accepts positive floating point values
path    - like string but also accepts slashes
uuid    - accepts UUID strings

@app.route("/username/<path:name>")
def greet(name):
    return f"<p>Hello, {name}!</p>"

http://127.0.0.1:5000/username/Radu/12
Hello, Radu/12!

# You can have multiple variables:

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello, {name}! You are {number} years old.</p>"

http://127.0.0.1:5000/username/Radu/40
Hello, Radu! You are 40 years old.


# 2. Rendering HTML elements with Flask

# By default, Flask accepts HTML in the return of the function like we saw in the Quickstart guide

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# We can even add inline CSS or multiple elements
@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1><p>This is a paragraph</p><img src='https://images.pexels.com/photos/1870376/pexels-photo-1870376.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500' />"

# This will create the HTML code on the page
<html>
<head></head>
<body>
    <h1 style="text-align: center">Hello, World!</h1>
    <p>This is a paragraph</p>
    <img src="https://images.pexels.com/photos/1870376/pexels-photo-1870376.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500">
</body>
</html>


# Challenge - Add CSS to HTML using Decorator function

def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

@app.route("/bye")
@make_bold
def bye():
    return "<h2>Bye!</h2>"


# 3. Advanced Python Decorator functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper():
        if user.is_logged_in == True:
            function()
    return wrapper
# We receive an error that user is not defined, because the functions is expecting an argument with user name
# So we need to give the function *args or **kwargs

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
        print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

