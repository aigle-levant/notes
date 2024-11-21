---
title: "Compilation process"
subtitle: "Computer Systems : A Programmer's Perspective"
header_type: hero
header_img: "https://images.unsplash.com/photo-1516101922849-2bf0be616449?q=80&w=2128&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
categories: [book-notes, computer-systems]
tags: [programs, information, compiler, programming]
---

## Compilation process

All information inside a system is represented as a bunch of bits [bunch may be underestimating its power].

The very process by which a compiler compiles the code and displays output for languages like C, Java, etc. deals with converting to and from bytes.

### Compiler

Now, a **compiler** is a tool to translate our source code to a sequence of low-level instructions, written in binary. We pass instructions to our computer by translating our program using this tool.

> Languages like C, Java, C++, etc. use a compiler. Languages like Python and JavaScript, on the other hand, use an interpreter.

Its finished product is called an executable object program [or simply, file] and is stored as a binary disk file.

To translate a program and execute it, a compiler undergoes the following phases [we use C as an example here] :

#### Preprocessing phase

In this phase, the program is modified according to the directives issues by a **pre-processor**, a program that produces output from certain input to be used as input for another program.

Directives are statements that tell the pre-processor to perform an action.

For example, `#include <stdio.h>` is a directive in C telling the pre-processor to use functions from the header file [a library] called Standard Input / Output.

A library [or in this case, a header file] is a file containing pre-defined functions.

#### Compilation phase

Now the compiler translates the source file into a text file that contains its Assembly translation. This phase is where most compile-time errors occur.

#### Assembly phase

After the translation's done, the assembler [a program that converts Assembly language into binary] translates the text file into an actual binary file and packs it neatly into a relocatable object program [an object file that contains code which can be linked with other files to create an executable object file].

This program is stored as an object file. It contains the binary output, but isn't executable yet.

#### Linking phase

Now, the final phase of compilation involves another program called linker merging the necessary files [such as code for library functions used in the program] with the object file.

This creates an executable object file [just executable, please], which is loaded into memory and executed by your system.

This phase is also famous for linker errors that happen when it's unable to combine the files properly.

## Why do we need to understand this?

*"Why can't I just...code? I'll understand this better!"*

If you understand how different statements are dealt by the compiler, and how binary works, you can make your program efficient to handle.

Instead of grouping 4-5 `if-else` ladders, you'd use a single `switch` statement.

Instead of using a ``while(true)`` loop, you'd switch to a `do-while` loop.

Overhead [extra time or memory used to achieve a goal] wouldn't be too much.
