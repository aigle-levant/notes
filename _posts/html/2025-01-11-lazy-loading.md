---
title: "Lazy loading"
subtitle: "Wait until it loads"
categories: [strategies, html]
tags: [strategies, html]
---

Refer -> [What is lazy loading? | Cloudflare](https://www.cloudflare.com/en-gb/learning/performance/what-is-lazy-loading/) & [Browser-level image lazy loading for the web | web.dev](https://web.dev/articles/browser-level-image-lazy-loading)

**Lazy loading** is a technique where the browser doesn't request certain resources until the user interacts with them [requests them whenever needed].

> It is called 'lazy' loading as the browser procrastinate to load these contents.

## Eager loading

Your normal website loads 'eagerly' - meaning, it loads all the resources at the same time.

Websites and applications using this technique utilise a loading screen.

Complex and heavy applications like games use eager loading. Eager loading is always used in images that are visible when you first load a website [these images are called LCP images].

## Above and below the fold

The part that the user sees is called 'above the fold'.

The part that the user doesn't see yet is called 'below the fold'.

> It is like a person wearing a hood. The thing you can see [the hood] is 'above the fold'. Their face is hidden beneath the hood and so, it's 'below the fold'.

## Implementing lazy loading for images

Use the attribute `loading="lazy"` in the `<img>` tag. Also, give the image dimensions with `width` and `height` attributes.

```html
<img src="photo.png" alt="some image." width="200px" height="200px" loading="lazy" id="image">
```

JavaScript libraries like Angular, React, etc are used for sophisticated lazy loading.

[Check out lazy loading in React](https://react.dev/reference/react/lazy)

## Modularisation for the win?

JS and CSS are render-blocking resources. This means the browser can't render the page until they are loaded.

You can split your JS and CSS file into multiple modules that can be loaded when needed instead.

This is done by having a main file with sub-files as imports, then including this main file in your HTML document.

## Advantages and disadvantages

### Advantages

- Faster page load
- No unnecessary content

### Disadvantages

- If the user scrolls down quickly in a page, they might have to wait for the images to load.
- Browser might've to send multiple HTTP requests to the server. This is mitigated by using a CDN.
- Additional code for processing.
