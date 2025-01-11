---
title: "Accessibility"
subtitle: "Designing to Enable"
header_type: splash
header_img: "https://images.unsplash.com/photo-1558981420-87aa9dad1c89?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
categories: [strategies, html]
tags: [strategies, html]
---

Making a website **accessible** is to design it to enable even disabled people interact with it.

## Types of disabilities

### Visual impairment

**Example:** Blindness, colour-blindness, low vision

**Tools they use:** Screen-readers, screen-magnification, Braille

**Affected by:** Digital products working poorly with screen-readers, graphs designed to differentiation based on colour only, no pinch-to-zoom in mobile sites, shitty colour contrast

### Mobile impairment

**Example:** Physical disabilities

**Tools they use:** Eye-trackers, speech-to-text, adaptive switches

**Affected by:** Elements requiring a mouse

### Hearing impairment

**Example:** Deafness

**Tools they use:** Hearing aids, video captions or transcripts

**Affected by:** Poor captions or no captions

### Cognitive impairment

**Example:** Dementia, Alzheimers, Autism, etc.

**Tools they use:** Screen-readers, text-highlighting, text-summarisation, text-prediction

**Affected by:** Busy UI, little whitespace, clashing fonts, small and hard-to-read fonts, justified paragraphs

### Seizure

**Example:** Epilepsy, etc.

**Tools they use:** Reduced motion switches

**Affected by:** Extreme flashing, parallax effects, auto-scroll and auto-play

### Speech impairment

**Example:** Stuttering, dumbness, etc.

**Tools they use:** Speech-generating devices

**Affected by:** Technology activated only through voice

## WCAG Principles

Web Content Accessibility Guidelines [WCAG] is a standard for web and mobile accessibility.

A - Not accessible
AA - Accessible
AAA - Very accessible

<img src="https://web.dev/static/learn/accessibility/measure/image/perceivable-operable-un-3ca2c38c67bb1.png" class="img-fluid" alt="Responsive image">

### Perceivable

User must be able to perceive all essential information on screen.

Eg: Adding captions to videos, ensuring colour isn't the only way to tell difference, adding text-alternative to images.

### Operable

User must be able to operate the product's interface. It may not have an interaction which they can't perform.

Eg: Giving users enough time to fill form, adding touchscreen and keyboard support for active elements.

### Understandable

User must be able to understand the information and how the interface works.

Eg: Using simple language, having clear error messages, predictable navigation.

### Robust

Product must support assistive technologies as the users and devices evolve.

Eg: Testing with various technologies, ensuring that content fits various screen sizes.

## Assistive Technology

- Some examples are screen readers, alternative input devices, speech-to-text, screen magnifiers, etc.
- They detect headings, links and form labels
- Proper tags are required for their maximum usage.

### Accessibility Tree

It represents how the browser interacts with assistive technology. Using proper tags and keyboard accessibility is a must.

- Accessibility can be tested using Lighthouse, contrast checkers, AI, Accessibility Inspector, etc.

### Colour contrast

[Website to check colour contrast](https://webaim.org/resources/contrastchecker/)

Contrast between a text's colour and its background.

Regular texts must've a colour-contrast ratio of 4.5:1 [or 7:1 for AAA check] and big texts and icons must have a colour-contrast ratio of 3:1 (4.5:1 for AAA check).

Big text must be about 24px or 18.5px bold text in size.

Logos and decorations are exempted.

### HSL model

HSL model is an alternative to RGB. It's closer to how humans perceive colours. HSLa means alpha measurement is added, which measures opacity.

- Hue : Qualitative way to describe a colour in the spectrum
- Saturation : Intensity of a colour
- Lightness : Brightness of a colour
  
### Types of colour blindness

**Deuteranopia / Green-blind :** Can't perceive red and green colours
**Tritanopia :** Can't perceive blue and yellow colours
**Protanopia :** Can only see in yellow and blue colours
**Achromatopsia :** Can't perceive colours at all

Use `@prefers-color-scheme` and `@prefers-contrast` media queries for dark-mode and this.

## Exercise 1

I have the following HTML document and CSS styles :

```html
<main>
    <p class="red">Contrast ratio: 3.32</p>
    <p class="orange">Contrast ratio: 6.72</p>
    <p class="yellow">Contrast ratio: 12.37</p>
    <p class="green">Contrast ratio: 3.57</p>
    <p class="blue">Contrast ratio: 1.54</p>
    <p class="purple">Contrast ratio: 1.41</p>
</main>
```

```css
main
{
    width: 100vw;
    height: 100vh;
    color: #0000aa;
}
.red { background-color: #ff0000; }
.orange { background-color: #ffa500; }
.yellow { background-color: #ffff00;}
.green { background-color: #129a0d; }
.blue { background-color: #0000ff; }
.purple { background-color: #800080; }
```

This gives me the colours of the rainbow with text in [#0000aa] colour. However, it's not good in terms of colour contrast.

So I use a tool like [Adobe colour constrast checker](https://color.adobe.com/create/color-contrast-analyzer).

Now here's my modified stylesheet :

```css
.red { background-color: #FEC8C0; }
.orange { background-color: #FFBA8A; }
.yellow { background-color: #ffff00;}
.green { background-color: #1EDA17; }
.blue { background-color: #9FCCFF; }
.purple { background-color: #FEBDE5; }
```
