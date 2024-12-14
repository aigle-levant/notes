---
title: "Async-Await"
subtitle: "Making promises easier since 2017"
categories: [lang-notes, javascript, async-js]
tags: [high-level language, javascript, async]
---

## Async

`async` is a keyword used with functions. It makes it return a promise.

I grabbed a function from the [Promises notes](2024-12-09-js-promise.md) that I had written before :

```js
function funct()
{
  return Promise.resolve("Hello");
}
```

Now if we re-write this using `async` keyword :

```js
async function funct()
{
    return "Hello";
}
```

Let's try using this in the `isEven()` program.

First, we define an `async` function and throw the 'defining a random number' part inside it. We then use a ternary operator to check if our number would be even or not, and by that way, we create a Promise!

```js
async function isEven()
{
  let n = Math.floor(Math.random() * 100);
  console.log("Number: " + n);
  //always resolving part
  return (n % 2 === 0) ? 1 : 0;
}
```

The return part is always `resolving`, as in it doesn't return 0 in the first place. We need it to make it throw an error for odd numbers :

```js
async function isEven()
{
  let n = Math.floor(Math.random() * 100);
  console.log("Number: " + n);
  if (n % 2 === 0)
    return 1; //resolve
  else
    throw "Odd"; //reject
}
```

Now we modify the 2nd part of it :

```js
isEven().then(
    (value) =>
    {
        console.log("This is even, see: " + value);
    },
    (error) =>
    {
        console.log("This is odd, see: " + error);
    }
);
```

Here is the final program :

```js
async function isEven()
{
  let n = Math.floor(Math.random() * 100);
  console.log("Number: " + n);
  if (n % 2 === 0)
    return 1; //resolve
  else
    throw "Odd"; //reject
}

isEven().then(
    (value) =>
    {
        console.log("This is even, see: " + value);
    },
    (error) =>
    {
        console.log("This is odd, see: " + error);
    }
);
```

## Await

`await` is another keyword that has co-dependency issues with `async`. Simply put, **`await` can only be used with an `async` function**. Any other function and it'll run for the hills.

```js
let someVar = await asyncFunction();
```

It makes the function pause the execution, chill around for a while and continue after the async function returns a `Promise` object.

It also means that you don't need to chain a hundred functions in `.then()`.

We see this in our previous `isEven()` function's previous version :

```js
async function isEven()
{
  let n = Math.floor(Math.random() * 100);
  console.log("Number: " + n);
  return (n % 2 === 0) ? 1 : 0;
}
```

Now we add another function which waits for `isEven()` to finish executing and then gives the final judgement :

```js
async function check()
{
  let final = await isEven();
  if (final===1)
    console.log("Even");
  else
    console.log("Odd");
}
check();
```

So our entire program barely takes a few line [even less if simplified]!

```js
async function isEven()
{
  let n = Math.floor(Math.random() * 100);
  console.log("Number: " + n);
  return (n % 2 === 0) ? 1 : 0;
}

async function check()
{
  let final = await isEven();
  (final===1) ? console.log("Even") : console.log("Odd");
}
check();
```
