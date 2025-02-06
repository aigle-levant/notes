---
title: "CSS animations"
subtitle: "Animate like you would in clip-art"
header_type: hero
header_img: "https://images.unsplash.com/photo-1524666643752-b381eb00effb?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
categories: [css]
tags: [css, ui-ux]
---

CSS Animations let you animate transitions from one style to another.

They consist of 2 components :

- Style describing the animation.
- `@keyframes` indicating the start, end [and possible in-between] states.

## `@keyframes`

You've to specify styles inside this rule in a specific format.

Say, I want to set an animation to rotate an image. I'd first set up the `@keyframes` to rotate an image from 0 degrees to 360 degrees [spinning it around].

```css
@keyframes rotator
{
    from { rotate: 0deg; }
    to { rotate: 360deg; }
}
```

Then I set up the `img` style to include this rule and set its duration. `animation-delay` here means the animation will start after 2 seconds.

```css
img
{
    rotate: 0deg;
    animation-name: rotator;
    animation-duration: 3s;
    animation-delay: 2s;
}
```

> If the animation-duration property is not specified, no animation will occur, because the default value is 0s (0 seconds).

We can also make it rotate awkwardly then revert back to normal with percentages :

```css
@keyframes rotator
{
    0% { rotate: 0deg; }
    25% { rotate: 30deg; }
    50% { rotate: 60deg; }
    75% { rotate: 90deg; }
    100% { rotate: 0deg; }
}
```

> If we set `animation-delay` to negative values, the animation plays as if it has been playing for 2 seconds already.

`animation-iteration-count` sets the no. of times the animation is to be played. Setting it `infinite` makes it run forever.

`animation-direction` lets you specify the direction of the animation - forward, reverse, etc.

- `normal` : Default.
- `reverse` : Animation played in reverse direction.
- `alternate` : Animation is played normally at first, then changes to reverse.
- `alternate-reverse` : Animation is played reverse at first, then changes to normal.
