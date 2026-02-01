# 1. What is HTML? Hyper Text Markup Language

# The first websites were created using only HTML.
# HTML defines the construct and structure of the website. 

# Hyper Text is the text that links to another file, a hyperlink

# Markup Language
# "this is a quote" - the quotation is the mark that tells this is a quotation
# In ancient texts and manuscripts, the editors marked the parts that needed to be revised with circles, underlines etc.

# HTML markup is done with HTML tags, such as Headings, Paragraph, footer, select and so on


# 2. HTML Headings element

       <h1>   Hello World        </h1>
# opening tag    content      closing tag

# <Tag> vs Elements
# Anything that is inside an <> is called a tag
<h1> - opening tag
</h1> - closing tag

# Element is the entire line
<h1> Hello World! </h1>

# The heading are from 1 to 6
<h1>Heading1</h1>
<h2>Heading2</h2>
<h3>Heading3</h3>
<h4>Heading4</h4>
<h5>Heading5</h5>
<h6>Heading6</h6>

# 2.1 DO and DONTs
# Don't use more than 1 h1 heading in a page
<h1>Title</h1>
<h1>Another one</h1>

# Use
<h1>Title</h1>
<h2>Another one</h2>

# Don't skip a heading level
<h1>Title</h1>
<h3>Chapter one</h3>


# 3. The Paragraph Element <p>

<p> This is a paragraph </p>

# You will see many placeholder texts populated with what we call Lorem Ipsum, a piece of text invented by Cicero in Antiquity.
# We can generate the text according to our needs on https://lipsum.com


# 4. Void Elements

# A void element is an element where you are forbidden to put any content inside the tag

# 4.1 Horizontal Rule element - separate paragraphs by a line
<hr />

<p>This is a paragraph</p>
<hr />
<p>This is another paragraph</p>

# it will look like this

This is a paragraph

________________________________

This is another paragraph

# 4.2 Break Element - separate sentences into different lines according to a meaning, like a poem
<br />

<p>
To see a World in a Grain of Sand<br />
And a Heaven in a Wild Flower,<br />
Hold Infinity in the palm of your hand<br />
And Eternity in an hour.<br />
</p>
# William Blake

# 4.3 DO and DONTs

# Don't use break element to separate lines or paragraphs when not actually needed
<p>
Paragraph 1<br />
Paragraph 2<br />
</p>

# Use instead different paragraph elements as this is more compatible with screen readers
<p>Paragraph 1</p>
<p>Paragraph 2</p>

# While the html code is valid, it's not good practice to represent void elements like this
<hr>
<br>
# As of HTML5 the / is actually ignored inside the tag
