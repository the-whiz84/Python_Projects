# 1. Inheriting Templates Using Jinja2

# Previously, we saw that we can inject a header.html and footer.html using Jinja and the code might look something like this:

{% include "header.html" %}
Web page content
{% include "footer.html" %}


# This is a really flexible way of using Jinja to Template a website. It means that if your header and footer stay the same then you can just insert them into all your webpages.

# Template Inheritance
# However, often you'll find that you actually want to use the same design template for your entire website, but you might need to change some code in your header or footer. In these cases, it's better to use Template Inheritance instead.

# Template inheritance is similar to Class inheritance, you can take a parent template and extend its styling in your child web pages.

# For example, if we create a base.html file that has the following code:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

# It has predefined areas (or blocks) where new content can be inserted by a child webpage inheriting from this template.

1. We could re-write the success.html page to inherit from this base.html template:

# 1.
{% extends "base.html" %}
# 2.
{% block title %}Success{% endblock %}
# 3.
{% block content %}
   <div class="container">
      <h1>Top Secret </h1>
      <iframe src="https://giphy.com/embed/Ju7l5y9osyymQ" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <p><a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a></p>
   </div>
{% endblock %}

# 1. This line of code tells the templating engine (Jinja) to use "base.html" as the template for this page.
# 2. This block inserts a custom title into the header of the template.
# 3. This block provides the content of the website. The part that is going to vary between webpages.


# 2. Super Blocks

# When we inherit from Python classes, you often see super.init()
# The super keyword refers to the parent that the child is inheriting from. e.g If Simba inherits from Mufasa, then Mufasa is the super.
# When we are inheriting templates. Sometimes, there's some part of the template that we want to keep, but we also want to add to it. So we can use super blocks in this case.

3. Add the following code to your base.html:

<style>
{% block styling %}
body{
    background: purple;
}
{% endblock %}
</style>

# I named this block "styling" but you can call it anything you want.
# Just make sure that you close all blocks with {% endblock %}
# Now if you reload your website, you should see that both the success page and the denied page will have a purple background. 


# 3. Using Bootstrap-Flask as an Inherited Template

# The way that we're going to quickly improve the appearance of our website is of course through that super useful tool we learnt about on Day 58 - Bootstrap. Previously we saw that we could simply include a link to the Bootstrap CSS code in the header of our website. But there's an even easier way. We can use the Bootstrap-Flask Python extension.

