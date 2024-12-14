---
title: "Defining Objects"
subtitle: "in JavaScript"
categories: [lang-notes, javascript, js-oop]
tags: [high-level language, javascript, objects]
---

There are 3 ways to define an object in JS :

## Using object literals

If you've dabbled in python before, you must be familiar with dictionaries. What we're going to do now resembles them.

If not, watch and learn.

```js
const player = {
    //content goes here
};
```

We defined a variable [which is object's name] and are assigning values to it :

```js
const player = {
    name: "Jean Antonique",
    job: "Ranger",
    traitsStengths: ["Outdoorsman", "Axe Man", ""],
    traitsWeakness: ["Thin-skinned", "Fear of Blood", ""],
    //...
    mainWeapon: "Axe"
};
```

Since object's a collection of key-value pairs, the way this looks seems to make sense :

```js
const objectName = {
    keyName: value,
    anotherKeyName: anotherValue
};
```

However, there's a problem. Let's say we've to duplicate our object...

```js
const player = {
    name: "Jean Antonique",
    job: "Ranger",
    traitStrength: ["Outdoorsman", "Axe Man", ""],
    traitWeakness: ["Thin-skinned", "Fear of Blood", ""],
    jacket: "Wedding Suit",
    shirt: "Dress Shirt",
    pant: "Dress Pants",
    //...
    mainWeapon: "Axe"
};

const playerTwo = {
    name: "Yves Montagne",
    job: "Burger Flipper",
    traitStrength: ["Resilient", "Amateur Mechanic", ""],
    traitWeakness: ["Sunday Driver", "Conspicuous", ""],
    jacket: "Flannel",
    shirt: "Vest",
    pant: "Jeans",
    //...
    mainWeapon: "None"
};
```

This looks tedious. Imagine doing it for *gasp* 10 different entries.

By remembering this handy principle, let's go to an easier way of creating objects.

> **DRY - Don't Repeat Yourself**

## Using factory functions

This function churns out objects like a factory using a template we define it using.

```js
function player(playerName="Anonymous", playerJob="Unemployed", playerStrength, playerWeakness, playerJacket="None", playerShirt="Dress Shirt", playerPant="Jeans", playerWeapon="None")
{
    //further statements!
}
```

We've assigned values to keys [playerName, playerJob, etc.] so that they display if user doesn't enter input for them. In short, they're the default values.

```js
function player(arguments)
{
    return {
        name: playerName,
        job: playerJob,
        traitStrength: playerStrength,
        traitWeakness: playerWeakness,
        jacket: playerJacket,
        shirt: playerShirt,
        pant: playerPant,
        //...
        mainWeapon: playerWeapon,
        playerInfo : function()
        {
            //statements
        }
    }
}
```

Inside this function, we assign the user-input to the keys in our return statement. We can also have functions in this format - ``functName : function()`.

Now if we create an object...

```js
const playerOne = Player("Jean Antonique", "Ranger", "Outdoorsman", "Fear of Blood", "Wedding Suit", "Dress Shirt", "Dress Pants", "Axe");

playerOne.playerInfo(); //although this returns nothing
```

It's as easy as that!

## Using constructors

If you're familiar with Java or Python, you may know what a constructor is.

It creates instances of a class from its instance variables.

So we do the same thing we did, except differently.

```js
function player(playerName="Anonymous", playerJob="Unemployed", playerStrength, playerWeakness, playerJacket="None", playerShirt="Dress Shirt", playerPant="Jeans", playerWeapon="None")
{
    this.playerName = playerName;
    this.job = job;
    //...
    this.mainWeapon = this.mainWeapon;

    this.playerInfo = function()
    {
        //statements
    }
}
```

`this` refers to the object involved here. We use it to point to the object instead of point at the program as a whole, allowing us to hide away the complexities of a program.

```js
const playerOne = new player("Jean Antonique", "Ranger", "Outdoorsman", "Fear of Blood", "Wedding Suit", "Dress Shirt", "Dress Pants", "Axe");
```

Notice the `new` keyword? It's a thing from Java. An object's type is usually a class.

## Getting information out of an object

Say, we need the info. stored in our object urgently? For example, I need to know what my player does for a living [before the apocalypse began].

Then I'd have 2 ways to ask JS for this info.

```js
playerOne.playerJob;

playerOne["playerJob"];
```

Bracket notation is used when property name is a string with spaces in it.
{: #myid .alert .alert-info .p-3 .mx-2 mb-3}

## Organising objects

One way to write better code is to organise one's objects. Take a look here :

```js
//method one
const pOne = "Jean Antonique";
const pTwo = "Yves Montagne";
const pOneLoc = "Rosewood";
const pTwoLoc = "Arizona";
```

```js
//method two
const pOne
{
    name: "Jean Antonique",
    loc: "Rosewood"
}
const pTwo
{
    name: "Yves Montagne",
    loc: "Arizona"
}
```

While method one looks easy to declare and go, you'll have to remember the correct variable name and manually print it.

Why not use a function for that, instead?

```js
function printInfo(player)
{
    console.log(`Name: ${player.name}\nLocation: ${player.loc}`);
}
printInfo(pTwo)
/*
Name: Yves Montagne
Location: Arizona
*/
```

Another better way is to simply create object constructors.
