---
title: "Classes"
subtitle: "The main reason of Java"
header_type: splash
header_img: "https://images.unsplash.com/photo-1533709752211-118fcaf03312?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODZ8fGphdmElMjBwcm9ncmFtbWluZ3xlbnwwfHwwfHx8MA%3D%3D"
categories: [lang-notes, java]
tags: [high-level language, java, classes, oop, constructors]
---

In Java, classes are a public entity. They are usually declared in a separate file from the main program.

```java
public class coffee
{
    private String name;
    private double price;
}
```

Every class we create [even the ready-made ones] inherits the class ``Object``. This is why we can pass an instance of a class as a parameter to a method and why ``toString`` and ``equals`` methods exist.

### Public, static and void

A **public entity** is visible to the outside world. We can access and modify it.

Whereas a **private entity** is hidden and forces the users of the class to access it through specified means only. Usually we hide the instance variables of a class.

> This is possible thanks to the concept of encapsulation.

**Static** is a modifier that indicates that the method doesn't belong to an object [we don't need an object to access it] and can't be used to access variables that belong to objects.

We use this modifier if the method is receiving the variables as parameters [case in point - main method].

### Constructor

In Java, the constructor has the **same name as the class**. Its parameters are the **instance variables** we declared before [if we want, we can change the name in the parameters].

After that, we pass the parameters to our instance variables, which are referred by ``this.var``.

> A constructor is automatically created if it's not defined for a class [however, it will be an empty constructor that does nothing].

```java
public class coffee
{
    private String name;
    private double price;
 
    public coffee(String name, double price)
    {
        this.name = name;
        this.price = 0;
    }
}
```

We then create objects in our main program using the command `new`. The arguments passed here will be assigned to the instance variables of the objects [thus, defining its state].

## Strings and objects

We use the method ``toString()`` to return a string representation of our object.

```java
public class coffee
{
 //program
 public String toString()
 {
  //return statement
 }
}
```

This, we can call in our main function by the print statement. When we do so, Java parses the statement as below, thanks to abstraction.

```java
System.out.println(espresso);

//becomes
System.out.println(espresso.toString());

