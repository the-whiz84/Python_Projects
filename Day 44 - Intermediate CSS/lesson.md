# Day 44 - Intermediate CSS: Box Model, Typography, and Centered Composition

Day 44 moves from basic CSS rules into composition. The motivational poster project uses a small amount of code, but it introduces several ideas that matter in every web layout: container sizing, margins, text alignment, imported fonts, and image framing. The point is not complexity. It is learning how a few CSS decisions control the feel of an entire page.

## 1. Using a Container to Control Layout Width

The poster content sits inside one `<div>`:

```html
<div>
  <img src="./assets/images/daenerys.jpeg" alt="Daenerys from Game of Thrones holding a dragon egg" />
  <h1>That Special Moment</h1>
  <p>When you find the perfect avocado at the supermarket</p>
</div>
```

The CSS then styles that container:

```css
div {
    margin: 10%;
    text-align: center;
}
```

This is the first real layout lesson in the course. Wrapping related elements in a container gives CSS one place to control spacing and alignment for the whole composition.

## 2. Styling Typography with an Imported Font

The page imports Libre Baskerville from Google Fonts and applies it to the headline:

```css
h1 {
    font-family: "Libre Baskerville", serif;
    font-weight: 400;
    font-style: normal;
    text-transform: uppercase;
    color: white;
}
```

This shows how typography changes tone. The exact same HTML content feels much more like a poster once the font, case, and color are chosen intentionally.

That is the broader CSS lesson here: presentation changes perception even when the content stays the same.

## 3. Using Borders and Background Contrast to Frame the Image

The image styling is simple but effective:

```css
img {
    border: 5px solid white;
    width: 100%;
}
```

Combined with the black page background:

```css
html {
    background-color: black;
}
```

this creates the poster look immediately. The image fills the container, the border frames it, and the high contrast keeps the layout visually focused.

This is a strong reminder that basic CSS properties often do more design work than complex effects.

## 4. Why the Box Model Matters Even in a Small Project

The poster uses only a few elements, but spacing still matters. Margin, border, width, and text alignment all work together to create composition.

That is the real “intermediate CSS” step on this day. You stop thinking only about styling individual elements and start thinking about how those styled elements occupy space together.

## How to Run the Project

1. Open the poster page in a browser:

```bash
open index.html
```

2. Edit `style.css` and refresh the page to see how spacing, font choices, and borders affect the overall composition.
3. Pay particular attention to how the container, image width, and centered text work together.

## Summary

Day 44 uses a simple poster project to introduce layout composition in CSS. A container controls spacing, imported typography shapes the tone, and borders plus contrast create a framed visual. The important lesson is that CSS is now organizing the page as a composition, not just coloring individual elements.
