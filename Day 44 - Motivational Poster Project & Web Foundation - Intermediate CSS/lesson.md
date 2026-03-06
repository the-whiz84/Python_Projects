# Day 44 - Intermediate CSS: Box Model, Typography, and Positioning

Today we're going deeper into CSS. You've learned the basics—now it's time to master the box model, work with custom fonts, and understand how to position elements precisely on a page. These skills separate amateur web design from professional layouts.

The motivational poster project is the perfect vehicle for these concepts—you'll create a dramatic, cinematic poster with custom typography, a dark background, and perfectly centered content.

## The Box Model: Every Element is a Box

In CSS, everything is a rectangular box. Understanding this is crucial for every layout decision. Each box has four layers:

```
┌─────────────────────────────────────┐
│           margin (outside)          │
│  ┌─────────────────────────────────┐│
│  │       border (the edge)         ││
│  │  ┌─────────────────────────────┐ ││
│  │  │    padding (inside)        │ ││
│  │  │  ┌───────────────────────┐  │ ││
│  │  │  │    content (your       │  │ ││
│  │  │  │    text or image)      │  │ ││
│  │  │  └───────────────────────┘  │ ││
│  │  └─────────────────────────────┘ ││
│  └─────────────────────────────────┘│
└─────────────────────────────────────┘
```

### Margin

Space outside the border—separates this element from others:

```css
div {
    margin: 10%;
}
```

`margin` pushes other elements away. You can set all four sides at once, or individually:

```css
div {
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 10px;
    margin-left: 20px;
    
    /* Shorthand: top right bottom left */
    margin: 10px 20px 10px 20px;
    
    /* Or just two values: top/bottom left/right */
    margin: 10px 20px;
}
```

### Padding

Space inside the border—between the border and content:

```css
div {
    padding: 20px;
}
```

Padding adds space *inside* your element, making it larger. Margin adds space *outside*.

### Border

The edge of the box:

```css
img {
    border: 5px solid white;
}
```

Border sits between padding and margin. You can control width (5px), style (solid, dashed, dotted), and color.

### The Magic: Centering Horizontally

Here's the technique used in the motivational poster:

```css
div {
    width: 50%;
    margin-left: 25%;
}
```

If you set an element to 50% width, and give it a left margin of 25%, it centers perfectly. It's like math: 25% + 50% + 25% = 100%.

## Google Fonts: Custom Typography

The project uses Libre Baskerville from Google Fonts. This transforms the poster from a webpage to something that looks like a movie poster.

### Step 1: Link the Font

In your HTML `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
```

The `preconnect` links speed up the font loading. The final link actually imports the font.

### Step 2: Use the Font

In CSS:

```css
h1 {
    font-family: "Libre Baskerville", serif;
    font-weight: 400;
    font-style: normal;
}
```

### Font Weight and Style

```css
h1 {
    font-weight: 400;    /* Regular */
    font-weight: 700;   /* Bold */
    font-style: normal;  /* Normal */
    font-style: italic;  /* Italic */
}
```

### Why Google Fonts?

Web-safe fonts (Arial, Times New Roman, Georgia) are available on every computer. But if you want something unique, you need to import it. Google Fonts is free and easy—thousands of fonts at your fingertips.

## Text Transform: UPPERCASE without typing it

The poster uses `text-transform: uppercase` to make the heading all caps:

```css
h1 {
    text-transform: uppercase;
}
```

This is powerful because:
- You type naturally in HTML
- CSS handles the visual style
- Change it to `lowercase` or `capitalize` instantly
- Screen readers still read the original text

## Color: Backgrounds and Text

The motivational poster is dramatic because of its color scheme:

```css
html {
    background-color: black;
}

h1, p {
    color: white;
}
```

This creates the high-contrast, cinematic look.

## The Motivational Poster Project

Here's the complete CSS from the project:

```css
/* The entire page background */
html {
    background-color: black;
}

/* The container div centers content */
div {
    margin: 10%;
    text-align: center;
}

/* The heading uses our custom font */
h1 {
    font-family: "Libre Baskerville", serif;
    font-weight: 400;
    font-style: normal;
    text-transform: uppercase;
    color: white;
}

/* The quote text */
p {
    color: white;
}

/* The image with a border */
img {
    border: 5px solid white;
    width: 100%;
}
```

And the HTML:

```html
<div>
    <img src="./assets/images/daenerys.jpeg" alt="Dragon egg" />
    <h1>That Special Moment</h1>
    <p>When you find the perfect avocado at the supermarket</p>
</div>
```

## Common Layout Patterns

### Center Everything Horizontally and Vertically

This is notoriously difficult in CSS. Modern approach:

```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;  /* Full viewport height */
}
```

Flexbox (covered later) makes side-by-side layouts trivial.

## Debugging Layouts

When something looks wrong, use your browser's developer tools:

1. Right-click any element → Inspect
2. Look at the computed styles on the right
3. Hover over the element in the Elements panel to see its box

The computed tab shows you the actual values after all CSS rules combine—including defaults you didn't set.

## Try It Yourself

Open the motivational poster:

```bash
open "index.html"
```

Experiment with:
1. Change the font family to something else from Google Fonts
2. Adjust the margin percentage (try 5% or 20%)
3. Change the border color or width
4. Add more text or change the image
5. Try `text-align: left` instead of `center`

## Moving Forward

Today you learned the foundation of professional CSS layouts: the box model, typography with Google Fonts, and text transformation. These skills apply to every website you build.

Tomorrow we'll dive into web scraping, leaving web development temporarily before coming back to Flask.
