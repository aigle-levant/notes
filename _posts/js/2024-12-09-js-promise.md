---
title: "Promise"
subtitle: "Promise me that this will go okay"
categories: [lang-notes, javascript, async-js]
tags: [high-level language, javascript, async]
---

`Promise` is an object returned by an asynchronous function after starting the operations. It represents the current state of a program's operations.

You can attach event handlers to this object, which can be executed when operations succeed or fail.

## Syntax

> *A callback used to initialize the promise. This callback is passed two arguments: **a resolve callback** used to resolve the promise with a value or the result of another promise, and **a reject callback** used to reject the promise with a provided reason or error.* - VS Code definition of a `Promise` object

A `Promise` has two parts - the producing part and the consuming part.

Like the above definition, the producing part consists of creating an object with a function as its argument. This functions returns either `whenSuccess(result)` or `whenFailure(errorObject)` as its result.

```js
const fetchMeAPromise = new Promise(
someFunction(whenSuccess, whenFailure)
{
    whenSuccess();
    whenFailure();
});
```

And the consuming part that waits for the `Promise` to be `resolved`. `then` simply means, do this after the producing part is done doing something :

```js

fetchMeAPromise.then(
someFunction(args)
{
    //definition
}
someFunction(errorArgs)
{
    //definition
}
)
```

### Example

Say, we have a function to check if a number is even :

```js
function isEven(n)
{
  return (n % 2 == 0) ? 1 : 0;
}
```

We create a `Promise` object, which has a function with the two parameters. In it, we create a variable with a random value.

```js
let promiseMe = new Promise(
function(ifSuccess, ifFailure)
{
  let randomNumber = Math.floor(Math.random() * 100);
  console.log("Number: " + randomNumber);

  if (isEven(randomNumber)===1)
    ifSuccess(randomNumber);
  else
    ifFailure(randomNumber);
});
```

We use a conditional to check if the value returned by `isEven()` is 1 or not. If yes, we call `ifSuccess()` with that number as argument. If not, we call `ifFailure()`. With this, we finish the producing part.

In the consuming part, we use the `then()` method, which takes 2 functions as arguments [remember, they're called callbacks].

One returns something when `isEven` is 1 [the `Promise` is `fulfilled`]. Another returns something when `isEven` is 0 [the `Promise` is `rejected`].

```js
promiseMe.then(
  function(value)
  {
    console.log("This is even, see: " + value);
  },
  function(error)
  {
    console.log("This is odd, see: " + error);
  }
)
```

So your final code may look like this :

```js
//function
function isEven(n) { return (n % 2 == 0) ? 1 : 0; }

//promise object
let promiseMe = new Promise(
function(ifSuccess, ifFailure)
{
  let randomNumber = Math.floor(Math.random() * 100);
  console.log("Number: " + randomNumber);
  if (isEven(randomNumber)===1) ifSuccess(randomNumber);
  else ifFailure(randomNumber);
});

//promise method
promiseMe.then(
  function(value)
  {
    console.log("This is even, see: " + value);
  },
  function(error)
  {
    console.log("This is odd, see: " + error);
  }
)
```

> A `Promise` object can also have only the `ifSuccess` part or the `ifFailure` part.

### `Promise` object's properties

This object has two properties : `state` and `result`. Both can only be accessed through the object's methods.

> The process by which object properties are accessible only through their methods is called **encapsulation**.

## Promise states

**`pending`**

- `Promise` object has been created
- Async function is still ongoing
- Obtains this state when the async function returns the object as value to `fetch()` to make a request.

**`fulfilled`**

- Async function has succeeded.
- `then()` is called.

**`rejected`**

- Async function has failed.
- `catch()` is called.

> A function that performs a task that requires it to 'handle' something - like handling transitions, handling the process of automating tests - is called a **handler**.

**Settle** is a term used to indicate that something's performed with the `Promise` object to change its state from `pending` to either `fulfilled` or `rejected`.

So, a promise is **resolved** if we settle it, if we finish it somehow. It is also resolved when it switches to follow the state of another promise [a promise chain].

### Methods used with `Promise`

> Check out `async-await` from [here](2024-12-11-js-async-await.md)

``Promise.resolve()`` lets you create a `Promise` object that's already been resolved.

```js
function funct()
{
  return Promise.resolve("Hello");
}

funct().then(
  function(value)
  {
    otherFunct(value);
  }
)
```

``Promise.reject()`` lets you create a `rejected` `Promise` object. You've to provide the reason why it was rejected as argument.

```js
function funct()
{
  return Promise.reject("Oh no");
}

funct().then(
  function(value)
  {
    otherFunct(value); //this won't be returned
  }
  function(error)
  {
    console.log("Error"); //this will be returned
  }
)
```
