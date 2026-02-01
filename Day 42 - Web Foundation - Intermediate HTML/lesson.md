# 1. The HTML Boilerplate

- this gives the structure to the website
- it looks something like this
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Website</title>
    </head>

    <body>
        <h1>Hello World!</h1>
    </body>
</html>



<!DOCTYPE HTML>
# at the start of each HTML file we specify the doctype so it tells the browser which html version we are using, currently, html means 5

<html lang="en">

# the actual html content will be the root of the document
# everything else will go between the opening and closing tags

    <head>
# important info about our website is set but not displayed to the user
        <meta charset="UTF-8">
# all websites should have a meta tag that tells the browser the character set we used
        <title>My Website</title>
# the title is what is displayed in the browser tab when website is opened
    </head>

    <body>
# everything else on the website goes inside the body element
        <h1>Hello World!</h1>
    </body>
# closing tag for body

</html>

# closing tag for html

- we should indent our code properly so each element is clearly visible and we don't miss putting the closing tags for each element

# if we create a .html file in VsCode, we can generate the boilerplate by writing ! on the first line and selecting the options given
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

# tells the browser how the website should be displayed on the screen that is rendered on
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Document</title>
</head>
<body>
    
</body>
</html>


# 2. The List Elements

# 2.1 Unordered List and the list item
<ul>
    <li>Milk</li>
    <li>Eggs</li>
    <li>Bread</li>
</ul>

# will create a bullet point list


# 2.2 Ordered List
<ol>
    <li>Milk</li>
    <li>Eggs</li>
    <li>Bread</li>
</ol>

# will create a numbered list


# 3. Nesting and Indentation

# We can create nested lists by using indentation
<ul>
<li>Wake up and brush teeth</li>
<li>Drink 500mk of water</li>
<li>Make omelette:
    <ul>
        <li>Whisk eggs with milk</li>
        <li>Add butter to pan</li>
        <li>Add in eggs and stir</li>
        <li>When solid, add salt</li>
    </ul>
<li>Start work</li>
</ul>


# 4. Attributes and the Anchor element

<tag attribute=value>Content</tag>

# An attrinute adds additional information to the HTML element, such as the website where the link points to
<a href="www.google.com">This is a link</a>

# href is the url that the hyperlink should point to

# You can add as many attributes as needed separated by a space
<tag attribute=value anotherattribute=value>Content</tag>

# In addition to specific attributes that each element has, there are HTML Global Attributes that each element has access to.
- draggable - boolean
- hidden - boolean
<a href="www.google.com" draggable=true>This is a link to Google</a>


# 5. The Image Element

<img src="url" />

# Just like the anchor element requires the href attribute to function, the image element requires the source (src) or location of the image
# The image element is a Void element since it is self closing and has no content

# It is good practice to add also the alt (alternative text attribute) attribute for the image, giving it a description for screen readers.
<img src="https://picsum.photos/200" alt="forest at sunset" />
