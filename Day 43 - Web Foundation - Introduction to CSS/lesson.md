# 1. What is CSS - Cascading Style Sheets

# A Style Sheet is a type of language like Markup Language:
- CSS
- Sass - Syntaxilly Awesome Style Sheet
- Less - Leaner CSS

# The W3C Consortium launched HTML 3.2 in 1997 and introduced new tags like font, color, size etc that allowed further customization of HTML
# All of these are now Deprecated since HTML should only be used for the content of the website

# CSS was introduced instead for styling the webpages in 1996

https://appbrewery.github.io/just-add-css/  
# Example of how CSS changes a website aspect without modifying any of the code in the html file


# 2. How to add CSS

# There are 3 ways to add CSS to a website:

# Inline
<tag style="css" />

# Internal
<style>css</style>

# External
<link href="style.css"/>

# 2.1 Inline - it's added on the same line as thw HTML element

<html style="bacground: blue">
</html>
# style="bacground: blue" is the CSS part
# 'style' is a global attribute
# 'bacground' is the property we want to change
# 'blue' is the value of the property

# This method is cumbersome and not widely used because you need to add the 'style' to each element, even if it shares the same property: value

# 2.2 Internal - we use a special HTML element named <style>

<html>
    <head>
        <style>
            html{
                background: red;
            }
        </style>
    </head>
</html>

# The CSS is between the opening and closing tags <style>
# 'html' is a selector
# the properties are added between {}
# between <style> and </style> we can add as many elements/selectors as we need to customize

# This is a good option for one page website as it will not work for multi-page websites

# 2.3 External - it refers to a different file where everything is added

<html>
    <head>
        <link 
            rel="styleshhet"
            href="./styles.css"
        />
    </head>
</html>

# styles.css contains:
html{
    background: green;
}

# The link to the CSS file must be added to the <head> section of the html file
# 'rel' - relationship, what is the role of the file we are linking to our html
# 'href' - location of the file

# This is the most used way of using CSS in Web Development

# Inline - good for targeting a single Element
# Internal - good for targeting a single web page
# External - multi-page website


# 3. CSS Selectors

# 3.1 Element Selectors

  h1 {
#selector    
    color: blue
#property: value 
}

# h1 - a particular HTML element
# An element selector applies the CSS to ALL of the same elements


# 3.2 Class Selector

.red-heading {
    color: red
}
 #dot . then name of class, no spaces

# A class is an attribute that we can add to any HTML element

<h2 class="red-text">RED</h2>
<h2>BLUE</h2>
<h2>GREEN</h2>

# style.css
.red-text{
    color: red
}
# This will only change the style of the first h2 element

# We can use class selectors to style different elements

<h2 class="red-text">Heading 2</h2>
<h3>Heading 3</h3>
<p class="red-text">Paragraph</p>

# style.css
.red-text{
    color: red
}


# 3.3 Id Selector

#main {
    color: red
}

# The id selector uses the # with no space and the name of the id. It will then apply to the elements that have that id attribute

<h2 id="main">RED</h2>
<h2>BLUE</h2>
<h2>GREEN</h2>

# style.css
#main {
    color: red
}

# ID vs Class
# The Class selector can be applied to many elements while the Id should be applied to a single element in a html file. The Id should be unique to a single element.


# 3.4 Attribute Selector

p[draggable]{
    color: red
}

# As was discussed, an element can have many attributes
<h1 id= class= draggable= href= src= >

# 'p' is the html element we want to select
# [attribute] - the attribute we want to select
# This will select all elements of the same type with the specific attribute

<p draggable="true">Drag me</p>
<p>Don't drag me</p>
<p>Don't drag me</p>

# styles.css
p[draggable]{
    color: blue
}

# You can fine tune even more by selecting a specific value for the attribute

<p draggable="true">Drag me</p>
<p draggable="false">Don't drag me</p>
<p draggable="false">Don't drag me</p>

# styles.css
p[draggable="false"]{
    color: red
}


# 3.5 Universal selector

* {
    color: red
}

# This will select all elements on the html file

<h1 class="title">Hello</h1>
    <h2 id="heading">World</h2>
        <p draggable="true">This is a website</p>

# styles.css
* {
    color: red;
}


# 4. CSS Specifity

# In the CSS Selectors challenge we could see that list item 3 remained green even if changed the li[value] color to blue.
# This is because the order of importance is from specific to general, id targets only 1 element, while value covered 4 elements
