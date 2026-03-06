# Day 41 - Introduction to HTML and Your First Web Pages

Today we're leaving Python behind and stepping into web development. HTML (HyperText Markup Language) is the foundation of every website you've ever visited. While Python handles the logic behind the scenes, HTML structures the content that appears in your browser.

This day introduces the building blocks of web pages: headings, paragraphs, and void elements. You'll create your first HTML documents and see them come alive in your browser.

## What is HTML?

HTML is not a programming language—it's a markup language. That means it describes the structure and content of a page, rather than executing logic. Think of it like the skeleton of a webpage: it tells the browser what content exists and how it's organized, but not how it looks (that's CSS's job, which we'll cover tomorrow).

The first websites were created using only HTML. They were simple—text, headings, and links—but they worked. As the web evolved, we added CSS for styling and JavaScript for interactivity, but HTML remains the bedrock everything else builds upon.

## Your First HTML Document

Every HTML document follows a basic structure:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My First Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is my first webpage.</p>
    </body>
</html>
```

Let's break down what's happening here:

- `<!DOCTYPE html>` tells the browser this is an HTML5 document
- `<html>` is the root element that wraps everything
- `<head>` contains metadata (title, character encoding, styles)
- `<body>` contains everything visible on the page
- `<h1>` is the main heading
- `<p>` is a paragraph

## Headings: Organizing Content

Headings create hierarchy in your content. HTML provides six levels:

```html
<h1>The Main Title</h1>
<h2>A Major Section</h2>
<h3>A Subsection</h3>
<h4>A Minor Subsection</h4>
<h5>Even Smaller Heading</h5>
<h6>The Smallest Heading</h6>
```

In the movie project, you'll see:

```html
<h1>Radu's Greatest Movies of All Time</h1>

<h2>Top 10 best movies I've watched</h2>

<hr />

<h3>The Shawshank Redemption</h3>
<p>
    This is the only movie I can gladly re-watch anytime.<br />
    One of the classic movies that everyone should watch at least once.
</p>
```

Notice how each heading level creates a clear structure. The `<h1>` is the most important (there should typically be only one per page), and the others create a hierarchy of information.

## Paragraphs and Line Breaks

The `<p>` element wraps text into paragraphs:

```html
<p>This is a paragraph of text. The browser will automatically add spacing above and below this block of text.</p>

<p>Here's another paragraph with a line break inside it.<br />
See how the break tag creates a new line without starting a new paragraph?</p>
```

The `<br /> tag is a void element—it doesn't have a closing tag because it doesn't wrap any content. It simply inserts a line break where you place it.

## Void Elements

HTML has several void elements that don't require closing tags:

- `<br />` - Line break
- `<hr />` - Horizontal rule (a divider line)
- `<img />` - Image (requires src attribute)
- `<input />` - Input field

The favorite movie project uses `<hr />` to create visual breaks between sections:

```html
<h1>Radu's Greatest Movies of All Time</h1>
<h2>Top 10 best movies I've watched</h2>

<hr />

<h3>The Shawshank Redemption</h3>
<p>Description of the movie...</p>
```

## Viewing Your HTML

To see your HTML in action, you have several options:

### Option 1: Open Directly in Browser
Simply double-click the HTML file in your file explorer, or right-click and choose "Open with" → your browser.

### Option 2: Use VS Code Live Server (Recommended)
If you're using VS Code, install the "Live Server" extension:
1. Open your HTML file in VS Code
2. Right-click and select "Open with Live Server"
3. Any changes you make will instantly refresh in the browser

This is incredibly useful as you build—see your changes immediately without manually refreshing.

## Semantic HTML: Why Structure Matters

Modern HTML is about semantics—using the right element for the right job. Instead of just `<div>` everywhere, we use elements that describe their content:

- `<header>` - Page or section header
- `<nav>` - Navigation links
- `<main>` - Main content area
- `<article>` - Self-contained content
- `<section>` - Thematic grouping
- `<footer>` - Page or section footer

While today's exercises use basic elements, keeping semantics in mind helps create maintainable code.

## Try It Yourself

Open `index_favorite_movie_project.html` in your browser. You'll see a list of great movies with headings and descriptions.

Try modifying it:
1. Change the main heading to your name
2. Add your own favorite movies using `<h3>` for the title and `<p>` for the description
3. Add `<hr />` elements between each movie
4. Use `<br />` within paragraphs when you want a line break without extra spacing

## How the Browser Parses HTML

Understanding how browsers read HTML helps debug issues:

1. The browser reads the document from top to bottom
2. It constructs the Document Object Model (DOM)—a tree of all elements
3. It applies default styles (every browser has built-in CSS)
4. It renders the visual result

If you forget a closing tag, the browser tries to guess what you meant. Sometimes it works; sometimes it creates unexpected results. This is why valid, well-structured HTML matters.

## Moving Forward

Today you learned the foundation. Tomorrow we'll add CSS to make things look beautiful. Later, we'll add JavaScript for interactivity. But it all starts here—with HTML telling the browser what content exists.

## Try It Yourself

```bash
open "index_favorite_movie_project.html"
```

Or if you're using VS Code with Live Server installed, right-click and select "Open with Live Server" to see changes update in real-time.
