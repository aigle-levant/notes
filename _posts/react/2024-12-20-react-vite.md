---
title: "Vite"
subtitle: "Vite comme ton esprit"
header_type: splash
header_img: "https://images.unsplash.com/photo-1558981420-87aa9dad1c89?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
categories: [frameworks, react]
tags: [js-frameworks, react, vite]
---

[Photo by Harley-Davidson on Unsplash](https://unsplash.com/@harleydavidson)

**Vite** is a build tool for web applications. It requires **Node.js** and **npm** to be installed in your machine.

## Getting started quickly

Go to the terminal [you can get it in VS Code by clicking the 3 dots beside View, going to Terminal and clicking 'New Terminal'] and type the following :

```bash
npm create vite@^4.0.0 --save-dev
```

It will ask the following questions :

- Project name
- Framework used [select React]
- Variant [select JavaScript]

A folder with the project name is created. Then it gives you a bunch of commands that you should run.

If the project name is sample...

```bash
cd sample
npm install
npm install @vitejs/plugin-react@^4.0.0 --save-dev
npm run dev
```

Since Vite v6 is insanely unstable at the point of writing, I'm using v4.
{: #myid .alert .alert-info .p-3 .mx-2 mb-3}
