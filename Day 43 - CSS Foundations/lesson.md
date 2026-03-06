# Day 43 - CSS Foundations: Selectors, Colors, and Basic Styling

Day 43 introduces CSS as the styling layer that sits on top of HTML structure. The color vocabulary project is deliberately simple, which makes it a good place to learn how selectors target elements and how a stylesheet changes appearance without changing the document content itself.

## 1. Linking HTML to an External Stylesheet

The vocabulary page connects to `style.css` in the document head:

```html
<link rel="stylesheet" href="./style.css" />
```

This is the preferred starting pattern because it keeps presentation separate from markup. HTML describes the content. CSS describes how that content should look.

That separation is one of the most important habits in frontend work.

## 2. Using Selectors to Target the Right Elements

The stylesheet demonstrates both class and ID selectors:

```css
.color-title {
    font-weight: normal;
}

#red {
    color: red
}
```

In the HTML, those selectors map to:

```html
<h2 class="color-title" id="red">Rojo</h2>
```

This is the key CSS lesson:

- classes are useful for shared styling across many elements
- IDs are useful for one specific element

Once you understand that split, larger stylesheets become much easier to organize.

## 3. Styling Repeated Elements with One Rule

The image rule applies to every image on the page:

```css
img {
    width: 200px;
    height: 200px;
}
```

This is where CSS starts to feel powerful. One rule updates every matching element instead of repeating styling decisions over and over in the HTML.

That ability to define one rule and reuse it across the page is the basis of maintainable frontend styling.

## 4. Why CSS Starts with Small, Predictable Changes

The project keeps the styling scope narrow:

- change heading color with IDs
- normalize heading weight with a class
- size all images consistently

That is a good foundation. Before dealing with layout systems and more advanced styling, you want a clear mental model of how selectors match elements and how declarations affect appearance.

## How to Run the Project

1. Open the project in a browser:

```bash
open index_color_vocab_website.html
```

2. Edit `style.css` and refresh the page to see how changes in the stylesheet affect the HTML.
3. Compare the class selector for shared title styling with the ID selectors that apply individual colors.

## Summary

Day 43 introduces CSS as the presentation layer for HTML. The project uses an external stylesheet, class and ID selectors, and simple sizing and color rules to demonstrate how styles are applied across a page. The main lesson is learning how selectors map to document structure.
