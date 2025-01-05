---
title: "Minification"
subtitle: "Not related to Minnie Mouse."
categories: [strategies, html]
tags: [strategies, html]
---

[References]

- [Minification | MDN Web Docs](https://developer.mozilla.org/en-US/docs/Glossary/Minification)
- [Minify Resources (HTML, CSS, and JavaScript) | Google Developers](https://developers.google.com/speed/docs/insights/MinifyResources)

Minification is the process of removing unnecessary data that won't affect the page being processed by the browser. It reduces file size and increases performance.

Code is minified by a minifier by removing comments, whitespace, shortening variable and function names.

## HTMLMinifier

HTML is minified by [HTMLMinifier](https://github.com/kangax/html-minifier). It can be installed using npm by :

```bash
npm install html-minifier
```

## CSS Optimizer

CSS is minified by [CSSO](https://github.com/css/csso). It can be installed using npm by :

```bash
npm install csso
```

It can be used in JS file :

```js
import { minify } from 'csso';
// CommonJS is also supported
// const { minify } = require('csso');

const minifiedCss = minify('.test { color: #ff0000; }').css;

console.log(minifiedCss);
// .test{color:red}
```

## UglifyJS

Finally, you could use [UglifyJS](https://github.com/mishoo/UglifyJS) for your JS code. It can be installed like this using npm :

```bash
npm install uglify-js
```
