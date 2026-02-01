# 1. CSS Color Properties

html {
    bacground-color: red
}
h1 {
    color: blue
}

# Until now we have set the values to Named Colors (https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)

# We can also use Hex Code Colors like we used before in our projects from Color Hunt (https://colorhunt.co/palettes/popular)
h1 {
    color: #CBF1F5
}


# 2. Font Properties

h1 {
    color: blue
    font-weight: bold
    font-size: 20px
    font-family: sans-serif
}

# 2.1 Font size

# font-size is given usually in pixels, 1 pixel is 1/96 of an inch or about 0.26 mm
# Another way to represent size is a pt (point) 1/72 of an inch or 0.35 mm
# THe point is commonly used for word processors, a font of 12 in Word is 12pt

# There are other ways to represent font size:
# 1em - 100% of parent (pronounced m) - relative size
# 1rem - 100% of root (pronounced rm) - relative to the root element (most cases the html)

# 1em is 100% of the parent element

<body> 20px
    <h2> Hello</h2> 1em is 100% of body size, so 20px
# 2em is double the size of body

# it is recommended to use rem as it is not affected if an element's parent has a change of size during coding


# 2.2 Font weight

# usual ones like 'normal', 'bold' keywords
# relative to the parent: 'lighter', 'bolder'(- 100 or + 100 relative to the parent)
# using a number between 100 - 900


# 2.3 Font Family

h1 {
    font-family: Helvetica, sans-serif
            #Typeface specific to MacOS
            # we add a comma and a backup generic font type for all OS types, like sans-serif
}
h2 {
    font-family: "Times New Roman", serif
            # for multiple words fonts, we add quotes
}

# Custom free fonts can be found at www.fonts.google.com
# We can added them to the css by embedding them as a link so the page renders correctly for all users of the website


# 2.4 Font Alignment

h1 {
    text-align: center
}

# can be left, right, center, justify
# there is also 'start' and 'end' (eg for arabic text, start is from right and end is left)


# 3. CSS Inspection

# We use Google Chrome's built in Developer tools (F12) to make changes to the CSS of https://appbrewery.github.io/just-add-css/
# Challenge was done on https://appbrewery.github.io/css-inspection/


# 4. CSS Box Model

# Margin, Padding and Border Properties form an important CSS concept named the Box Model
# We can set the width and height of each element either in pixels or percentage

p{
    width: 600
    height: 600
}

# 4.1 We can also set a border around each element
p{
    border: 10px solid black;
}
# the border property takes can take 3 values separated by a space
#10px - thickness
#solid - style of the border: solid, dashed
#black - color of the border

# No matter how thick we make the border, the size of the element does not chage (widht and height)

# We can refine the border style by indenting other properties
p{
    border: 30px solid black;
        border-top: 0px;
}

# The border-width can take a maximum of 4 values:
p{
    border: 30px solid black;
        border-width: 0px 10px 20px 30ox;
        # cloclwise:  up, right, down, left
}
# if we provide 2 values, it sets 1+3 and 2+4

# 4.2 Padding

# Useful for text elements as it pushes the border out from the element and makes the text clearly visible
p {
    padding:20px;
    border: 20px solid black;
}
# The size of the element does not change, the padding goes between the element box and the border

# 4.3 The Margin

# goes outside the border
p {
    padding:20px;
    border: 20px solid black;
    margin: 10px
}

# The CSS Inspector in the Dev Tools in the browser shows the Box Model
https://appbrewery.github.io/box-model/

# Padding, margin and border-width all can take 4 values in clockwise direction


# 5. Content Division Element
<div></div>

# These elements are invisible unless you apply CSS to them
# Their purpose is to act as invisble boxes to group separate elements
https://appbrewery.github.io/box-model/

<body>
    <div>
        <p>Hello World</p>
        <img src="./world.png" />
    </div>
    <div>
        <p>Good Night World</p>
        <img src="./night-world.png" />
    </div>
</body>