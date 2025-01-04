---
title: "ARIA Live Regions"
subtitle: "Change content - one calamity at a time."
categories: [strategies, html]
tags: [strategies, html]
---

ARIA live regions are parts of a webpage which announce to its users if the content dynamically changes.

Eg : Instagram notifying you of likes while you scroll through its explore page, a sign-in form telling you that your email is invalid when you hit submit, etc.

`aria-controls` attribute is used to connect cause element and effect element.

`aria-live` is used to announce changes.

- `aria-live="off"` : Default
- `aria-live="polite"` : Used if the update is important, but it shouldn't be aggressive to be announced. For example, notifications, etc.
- `aria-live="assertive` : Used only for time-sensitive and critical notifications. For example, Amber alert, SOS, etc.

## Programmatic focus management

It's a technique to control a browser's focus in response to certain user actions [like opening a menu, etc.]
