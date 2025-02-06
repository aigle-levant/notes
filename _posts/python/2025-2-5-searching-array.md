---
title: "Searching in arrays"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## `where()`

It's used to search the array for a certain value.

```py
arr = np.array(["APT", "Dynamite", "Crysalis Suspirii", "Glory"])
x = np.where(arr=="APT")
print(x) # (array([0], dtype=int64),)
```

We can set conditions for generating elements.

```py
arr = np.array([1,3,57,43,6,2223,2])
x = np.where(arr%2==0)
print(x) # (array([4, 6], dtype=int64),)
```

## `searchsorted()`

It performs a binary search on sorted arrays and returns the index of the element.

```py
arr = np.array([1,3,57,43,6,2223,2])
x = np.searchsorted(arr,3)
print(x) # 1
```

By default, it returns the left-most index. To make it do the right-most index, we use `side='right'`.

```py
arr = np.array([1,3,57,43,6,2223,2])
x = np.searchsorted(arr,3, side='right')
print(x) # 2
```

To search for multiple values, enclose them in brackets.

```py
arr = np.array([1,3,57,43,6,2223,2])
x = np.searchsorted(arr, [3,6])
print(x) [1 2]
```
