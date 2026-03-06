# Day 42 - Intermediate HTML: Lists, Images, Links, and Nesting

Today we move beyond basic paragraphs and headings into the elements that make websites truly interactive and useful. You'll learn how to create lists of items, embed images, add links to other pages, and most importantly, understand how HTML elements nest inside each other.

This is where HTML starts becoming powerful—because real websites aren't just headings and paragraphs. They're collections of things (lists), visual content (images), connections to other pages (links), and carefully structured hierarchies of elements.

## The HTML Boilerplate

Every HTML document follows a standard structure. You've seen simple examples, but let's look at a complete, production-ready boilerplate:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Webpage</title>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

Let's break down each part:

- `<!DOCTYPE html>` — Declares this as an HTML5 document
- `<html lang="en">` — The root element, with language attribute
- `<head>` — Container for metadata
- `<meta charset="UTF-8">` — Character encoding (allows for all languages and symbols)
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` — Makes the page responsive on mobile devices
- `<title>` — What shows in browser tabs and search results

The birthday invite project demonstrates this perfectly:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>It's My Birthday</title>
</head>
<body>
    <h1>It's My Birthday</h1>
    <h2>On the 12th of October</h2>
    <img src="https://example.com/cake.jpg" alt="birthday cake" />
    <!-- More content -->
</body>
</html>
```

## Ordered and Unordered Lists

Lists are everywhere on the web—navigation menus, product features, to-do items, ingredient lists. HTML provides two main types:

### Unordered Lists (`<ul>`)
Use when the order doesn't matter:

```html
<h3>What to bring:</h3>
<ul>
    <li>Balloons (I love balloons)</li>
    <li>Cake (I am really good at eating)</li>
    <li>An Appetite (There will be lots of food)</li>
</ul>
```

The `<ul>` tag creates the list, and each `<li>` (list item) is a bullet point.

### Ordered Lists (`<ol>`)
Use when sequence matters:

```html
<h3>How to make coffee:</h3>
<ol>
    <li>Boil water</li>
    <li>Add coffee grounds to filter</li>
    <li>Pour hot water over grounds</li>
    <li>Wait and enjoy</li>
</ol>
```

The browser automatically numbers each item.

You can also nest lists—put one list inside another:

```html
<ul>
    <li>Main item
        <ul>
            <li>Sub-item</li>
            <li>Another sub-item</li>
        </ul>
    </li>
    <li>Another main item</li>
</ul>
```

## Images

Images make websites alive. The `<img>` tag is a void element (no closing tag):

```html
<img src="https://example.com/cake.jpg" alt="birthday cake" />
```

Two attributes are essential:

- `src` — The image source (URL or file path)
- `alt` — Alternative text (shows if image fails to load, and for screen readers)

The birthday invite shows this in action:

```html
<img src="https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg" alt="birthday cake" />
```

You can use:
- Full URLs: `https://example.com/image.jpg`
- Relative paths: `images/photo.jpg` (file in images folder)
- Base64 encoded images (less common, mostly for small icons)

## Anchor Elements (Links)

Links are what make the web a web—they connect pages to each other. The `<a>` tag creates hyperlinks:

```html
<a href="https://www.google.com">Click here to go to Google</a>
```

The `href` attribute (hypertext reference) specifies where the link goes.

The birthday invite includes a real Google Maps link:

```html
<a href="https://www.google.com/maps/@35.7040744,139.5577317,3a,75y,289.6h,87.01t,0.72r/data=!3m6!1e1!3m4!1sgT28ssf0BB2LxZ63JNcL1w!2e0!7i13312!8i6656">
    Google Maps Link
</a>
```

You can also:
- Link to other pages in your site: `href="about.html"`
- Link to sections on the same page: `href="#section-id"`
- Open links in new tabs: `target="_blank"`

## Nesting and Indentation

This is the most important concept in HTML. Elements can contain other elements—you nest them. The burger.html file demonstrates this beautifully:

```html
<bun type="sesame">
    <sauce flavor="spicy">
        <cheese>Cheddar</cheese>
    </sauce>
    <prickles>
        <bacon>Not Burnt</bacon>
    </prickles>
    <lettuce>
        <meat type="Black Angus">Well Done</meat>
    </lettuce>
</bun>
```

Notice the pattern: when you open a tag, everything inside is indented. When you close the tag, you dedent. This visual hierarchy shows the parent-child relationships.

### Why Nesting Matters

1. **Structure**: The browser builds a tree from this—parents have children, children have parents
2. **Styling**: CSS can target elements based on their position in this tree
3. **Semantics**: Proper nesting tells the browser what content means

### Common Nesting Mistakes

The most common error is forgetting to close tags in the right order:

```html
<!-- WRONG: Tags overlapping incorrectly -->
<p>This is a paragraph <strong>with bold text</p></strong>

<!-- CORRECT: Tags properly nested -->
<p>This is a paragraph <strong>with bold text</strong></p>
```

Think of nesting like parentheses in mathematics—each opening must have its matching closing, in the right order.

## A Complete Example

Here's what a typical Day 42 project looks like—the birthday invitation:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>It's My Birthday</title>
</head>
<body>
    <h1>It's My Birthday</h1>
    <h2>On the 12th of October</h2>
    
    <img src="cake-image-url" alt="birthday cake" />
    
    <h3>What to bring:</h3>
    <ul>
        <li>Balloons</li>
        <li>Cake</li>
        <li>An Appetite</li>
    </ul>
    
    <h3>This is where you need to go:</h3>
    <a href="https://maps.google.com">Google Maps Link</a>
</body>
</html>
```

This combines everything: proper document structure, headings, images, lists, and links.

## Viewing Your Work

Open the HTML files in your browser:

```bash
open "index_birthday_invite_project.html"
```

Or use VS Code Live Server for real-time updates as you edit.

## Try It Yourself

Modify the birthday invitation:
1. Change the date to your birthday
2. Add more items to the "What to bring" list
3. Replace the image URL with another image
4. Change the link to point to your actual location

## Moving Forward

Today you learned the core building blocks of HTML. These elements—lists, images, links—are in every website you visit. Master these, and you can build anything.

Tomorrow we'll add CSS to make everything look beautiful.
