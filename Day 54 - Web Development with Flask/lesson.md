# 1. What is Full Stack Web Developer?

# Until now we learned about web development using HTML and CSS , which is frontend part of a website
# Full Stack Developer = Frontend + Backend 

# Frontend: HTML, CSS, Javascript
- HTML gives the website structure
- CSS gives it style
- JS allows it to have interactivity

# Backend: there are a lot of choices
- Javascript
- Java
- Python
- Ruby

# There are also different frameworks you can use for both frontend and backend:
- Front-End: Angular, React
- Back-End: Node, Flask, Django

# these are tools that come with a lot of the code pre-built for the common scenarios

# The Python backend has a miriad of options to built with:
- Flask
- Django
- Bottle
- Cherry Pie
- Pyramid
etc.

# The most popular ones are Flask and Django
- Flask is better suited to beginners and small projects
- Django is better suited for large commercial projects


# 2. What is the Backend?

# There are 3 main components:
- Client
- Server
- Database

# Client can be a user using a browser
# Server is the powerful computer that runs 24/7 and receives the requests and responds with the data
# Database is like the super spreadsheet that stores all the information related to the website


1. client ->    request    -> server
2. client <- html, css, js <- server
3. client -> request data  -> server -> request data -> database
4. client <- html, css, js with data <- server <- received data <- database


# 3. Getting started with Flask

#                   Library                             vs                          Framework
- set of reusable functions;                                - a piece of code that dictates the architecture of your project;

- you are in full control when you call a method            - the code never calls into a framework, instead the framework calls you;
from the library and the control is then returned;

- it's incorporated seamlessly into existing projects       - it cannot be seamlessly incorporated into an existing project. Instead it
to add functionality that you can access with an API;       can be used when a new project is started;

- they are important in program linking and binding         - they provide a standard way to build and deploy applications;
process;

- Ex: jQuery is a JavaScript library that simplifies        - Ex: AngularJS is a JavaScript-based framework for dynamic web applications. 
DOM manipulations.


# Examples

requests.get("https://www.google.com")  
# tapping into a library and giving it a command

def hello_world():
    return 'Hello, World!'
# we do not call the function but the framework calls it when it is needed


# Quickstart app with Flask
# file hello.py
from flask import Flask

app = Flask(__name__)


@app.route("/")

def hello_world():
    return "<h1>Hello, World!</h1>"

# flask --app hello run

# As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app.


# 3.1 __name__ and __main__ special Python attributes

# __name__ - the name of the class, function, method, descriptor or generator
# __main__ - is the name of the scope in which top level code executes.

# A module's __name__  is set equal to __main__ when read from standard input, a script or from an interactive prompt.

if __name__ == "__main__":
    # execute only if run as script
    main()

# The most common way flask is run is by using name and main:

app = Flask(__name__)
#print(__name__)
#__main__

@app.route("/")

def hello_world():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run()


# 4. Python Functions as First Class Objects: Passing & Nesting Functions

# 4.1 Python Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

# Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()


# 4.2 Python Decorators and the @ Syntax

@app.route("/") # we serve the function for the home page of the website ('/')
# decorator function

def hello_world():
    return "<h1>Hello, World!</h1>"

# A Decorator function gives additional functionality to an existing function


def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function()


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

# The @ sign add the decorator function to the say_hello function (no spaces between lines)
# The @ sign is known as syntactic sugar

# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()


# @delay_decorator
# def say_hello():
    print("Hello")


