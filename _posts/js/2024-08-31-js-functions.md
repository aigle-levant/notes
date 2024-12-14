---
title: "Functions"
subtitle: "Wait, they're objects?!"
categories: [lang-notes, javascript]
tags: [high-level language, javascript, functions]
---

*Wait what?!*

Yes. The title is right. **Functions are, indeed, objects**.

Long short short, functions belong to a category of data types called reference-type. This category includes :

* Objects
* Arrays

Since any value that isn't a primitive is considered an object [because, duh, everything resembles an object if you look at its template], functions are also objects.

They're specifically called **callable objects** for this reason.

Let's say we've this function :

```js
function caller(name, phone)
{
    this.name = name;
    this.phone = phone;

    this.dial = function(){
        console.log(this.phone + "\nCalling " + this.name + "...");
    }
}
```

Now let's head over to the console window and try out some commands using this function :

```js
caller.name //"caller"
caller.length //2
caller.call({}, "Mozart", undefined);
caller.apply({}, ["This", "That", "Everyone"], [2, 2, undefined]);
```

Notice the dot [.] operator being used here? This is because functions are objects.
{: #myid .alert .alert-info .p-3 .mx-2 mb-3}

Alright, now let me explain what each does :

`functionName.name` simply returns the name of the function.

`functionName.length` returns the number of arguments passed in a function.

`functionName.call()` is used to create objects. Be warned, this object may not have a name!

`functionName.apply()` is used to do the same thing as above, except with arrays.

## First, how do they work?

A function in JS has the same syntax like any other language :

```js
function weightOfLiving()
{
    return "under the weight of living";
}

console.log("or " + weightOfLiving());
console.log("you're " + weightOfLiving());
console.log(weightOfLiving());
console.log("you are " + weightOfLiving());

/*
or under the weight of living
you're under the weight of living
under the weight of living
you are under the weight of living
*/
```

If we remove the ``console.log()`` and call the function as it is...

```js
function weightOfLiving()
{
    return "under the weight of living";
}

weightOfLiving(); //no output
```

Nothing happens. This is because the `return` statement 'returns' something and doesn't actually print the value; we have to use ``console.log()`` to print that value.

```js
function weightOfLiving()
{
    console.log("under the weight of living");
}

weightOfLiving(); //under the weight of living
```

A function with an empty or non-existent `return` statement will return `undefined`.
{: #myid .alert .alert-info .p-3 .mx-2 mb-3}

### Arguments and parameters

We can make functions have a certain parameter by default and then enable us to pass parameters to it :

```js
function hey(rel="Brother")
{
    console.log("Hey " + rel);
}

const prompt = require("prompt-sync")({sigint:true});
const opt = prompt("brother or sister?");

if (opt=="sister")
{
    hey("Sister");
}
else
{
    hey();
}
```

This function, by default, has the value 'Brother', and so if we merely call it, it'll use that value.

Use this ``const prompt = require("prompt-sync")({sigint:true});`` in case `prompt()` doesn't work for you in VSCode.
{: #myid .alert .alert-info .p-3 .mx-2 mb-3}

### Anonymous functions

We call a nameless function an anonymous function :

```js
(
    function()
    {
        console.log("Is anyone there??");
    }
);
```

They can also be defined like this :

```js
let variable = (() =>
{
    console.log("Is anyone there??");
});
```

The above form is widely used in JS DOM.

### Function scope

A function's scope is the area in code reachable by it. It's confined by the mighty curly braces `{}`.

In that, we observe 2 variables : local and global.

Local variables are confined inside a function and can be used only within it.

Global variables, on the other hand, are outside functions and can be accessible from anywhere in the program.

```js
let song = "Hey Brother";

function setSong(song)
{
    console.log(song);
}

setSong(song); //Hey Brother
```

The function uses the already existing global variable as argument and returns the value.

Now let's add in a local variable :

```js
function setSong(song)
{
    let artist = "Avicii";
    console.log(song);
}

console.log(artist); //ReferenceError
```

We get a `ReferenceError` since the variable's out of scope.

### Function expression

It is another way to directly create a function :

```js
let line = function()
{
    console.log("Ge-");
};
let word = "Genius";
console.log(line + word);

/*
function()
{
    console.log("Ge-");
};
*/
```

We don't need the *damn* code! I'll have to modify this one just a bit...

```js
function genius()
{
    return "Ge-"
}

let line = genius;
let word = "Genius";
console.log((line().repeat(6)) + word);

//Ge-Ge-Ge-Ge-Ge-Ge-Genius
```

### Arrow functions

Now that we've seen function expressions, we wish to make them easier to write. For this, we go for arrow functions.

Consider the following code :

```js
let line = function(song, artist)
{
    return ("Playing : " + song + " by " + artist);
};

const prompt = require("prompt-sync")({sigint:true});

let song = prompt("Song name: ");
let artist = prompt("Artist: ");
console.log(line(song, artist));
```

Looks like we can shrink down a bit of our code using this arrow functions :

```js
let line = (song, artist) => ("Playing : " + song + " by " + artist);
```

`=>` is the arrow equivalent of `return`. We merely pass parameters and the function returns something.

Let's try this out with less than 2 parameters :

```js
let line = song => ("Playing : " + song);

const prompt = require("prompt-sync")({sigint:true});
let song = prompt("Song name: ");
console.log(line(song));
```

We can also have default values for our function :

```js
let line = (song="Bad Blood", artist="Bastille") => ("Playing : " + song + " by " + artist);

console.log(line());

//Playing : Bad Blood by Bastille
```
