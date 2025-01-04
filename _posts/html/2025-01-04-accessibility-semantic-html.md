---
title: "Semantic HTML"
subtitle: "Best practices for Accessibility"
categories: [strategies, html]
tags: [strategies, html]
---

Semantic HTML is necessary as certain elements have different properties which will help you [as well as other users].

You don't have to go through the trouble of messing around a `<div>` with additional CSS and JS to make it a button when a `<button>` tag will do just as fine.

Plus it makes your site score better in the search engine, but that's a different topic for now.

## Using clear language

Your content should be clear enough for the audience to understand.

- Don't use jargon or slang terms. If using, explain them at least somewhere in the document.
- Avoid dashes when a 'to' would suffice.
- Expand acronyms and abbreviations. When encountered again, use `<abbr>` tag to describe them.

## Page layout

A page may consist of the following

- `<header>` : This contains the logo or title of the website
- `<nav>` : Navbar
- `main` : Main content of the page
- `<article>` : Article or essay
- `<aside>` : Content in the sidebar
- `<footer>` : Content at the bottom of the page

## Lists

Consecutive items in code may either be in ordered or unordered lists, not as divs.

To remove list markers, use ``list-style-type: none``.

Eg : Navbar links, stats, social links on footer, etc.

## Headings

Be mindful of 3 things :

- Let heading numbers be consecutive : `<h1>` shouldn't come after `<h2>` but before it.
- Use only one `<h1>` per page.
- Use them for structure only. Style their sizes and appearance as you wish.

For example, the following code has an issue with the headings not being consecutive.

```html
<h1>Title</h1>
<p>Some content</p>

<h3>Sub-heading</h3>
```

You can instead change `<h3>` to `<h2>` and add an `id` selector for styling it instead.

```html
<h1>Title</h1>
<p>Some content</p>

<h2 id="subheading">Sub-heading</h2>
```

### Line spacing

Avoid using `<br>`. Screen readers *don't* do well with it.

### Font-size

Use adaptable unit like `rem` for `font-size`. The default `font-size` is 16px, which you can change in the `:root`.

## Images

Every image may have a proper alternative text defined using `alt` attribute. However, if the image is decorative, `alt` may be empty, or it should be made decorative using CSS.

## Links

Links opening in a new tab or windows may have a text indicating it. They may not be differentiated by colour alone.

### Skip link

It is an `<a>` placed next to the opening `<body>` element that allows you to bypass repeated content like website header, navbar, etc.

## Using JS to make websites touch-friendly

Use `click` for interactive actions.

## Hiding content

Instead of using `visibility` [or `display`], use ``opacity: 0;``, ``left: 100%;``, or ``transform: translate(100%, 0);``.
