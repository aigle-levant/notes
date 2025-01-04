---
title: "ARIA"
subtitle: "Not the Meloetta you're looking for."
categories: [strategies, html]
tags: [strategies, html]
---

Accessible Rich Internet Applications [ARIA] is a set of attributes that you can add to elements to provide more context to assistive technologies.

> ARIA is also known as WAI-ARIA [Web Accessibility Initiative ARIA].

One of its first rule is to ensure that you *avoid* using ARIA. It means, don't make up custom elements for doing stuff when a semantic element will just do as fine.

### So when should I use ARIA?

- Use it if you need to replicate certain semantic elements [like `<nav>`] or make it even more functional [like adding search, tab, etc. to it].
- To make your webpage keyboard-accessible.

## ARIA attributes

[Here's a list of ARIA roles from MDN Docs](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)

`role` defines the role of an element. Some examples are `role="banner"`, `role="search`, etc.

ARIA properties are used to give elements extra meaning. For example, `aria-required="true"` means a form input is to be filled compulsorily.

States are properties defining the current condition of the element. For example, `aria-disabled="true"` means the form input is disabled.
