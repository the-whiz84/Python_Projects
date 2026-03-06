# Day 42 - Intermediate HTML: Lists, Links, Images, and Nesting

Day 42 expands the HTML toolbox beyond headings and paragraphs. The birthday invite project combines lists, images, links, and proper document structure, while the smaller exercises reinforce the idea that HTML elements can contain other elements in a meaningful hierarchy. The core lesson is nesting: pages become richer by combining simple tags correctly.

## 1. Building a Proper HTML Document Shell

The birthday invite starts with the standard page structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>It's My Birthday</title>
</head>
```

This shell matters because a webpage is not just body content. The browser also needs metadata, encoding information, and a title for the page.

That distinction becomes more important once pages grow beyond small demos.

## 2. Using Images, Lists, and Links for Richer Content

The main project combines three new element types:

```html
<img src="https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg" alt="birthday cake" />

<ul>
    <li>Balloons (I love balloons)</li>
    <li>Cake (I am really good at eating)</li>
    <li>An Appetite (There will be lots of food)</li>
</ul>

<a href="https://www.google.com/maps/...">Google Maps Link</a>
```

Each one has a different role:

- `<img>` brings external media into the page
- `<ul>` and `<li>` represent grouped items
- `<a>` connects this page to another location

The lesson here is that HTML has purpose-specific elements. You do not use the same tag for everything and style it later.

## 3. Understanding Nesting and Indentation

The burger and list exercises in the folder reinforce how elements sit inside one another. Nesting is not only about visual indentation in your editor. It reflects parent-child relationships in the document tree.

For example, list items belong inside a list, and text links belong inside anchor elements. That structure is what browsers parse and what CSS targets later.

Once nesting is wrong, the whole page becomes harder to style and reason about.

## 4. Why Intermediate HTML Still Focuses on Semantics

Even with more tags available, the goal is still semantic structure:

- headings introduce sections
- lists group related items
- images add media with descriptive `alt` text
- links create navigation or references

This keeps the page expressive without needing any styling yet.

## How to Run the Project

1. Open the birthday invite in a browser:

```bash
open index_birthday_invite_project.html
```

2. Open the smaller subfolder exercises if you want to review images, anchors, lists, and nesting in isolation.
3. Inspect the markup and confirm that each content type uses the appropriate HTML element.

## Summary

Day 42 extends HTML from simple text structure into richer page composition. The projects add images, lists, links, and document metadata while reinforcing correct nesting. The central lesson is still semantic structure, but the pages now start to feel like complete documents instead of text outlines.
