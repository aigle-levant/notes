---
title: "Iterating array elements"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## Using `for` loops

We can loop through an array using a simple `for` loop.

```py
arr = np.array(["Shame", "Hangin'", "Glory"])
for i in arr:
    print(i)
"""
Shame
Hangin'
Glory
"""
```

It returns arrays [which are the elements] in case of multi-dimensional arrays.

```py
arr = np.array([["Shame", "Hangin'", "Glory"],["The Nights", "Warmth", "Of The Night"]])
for i in arr:
    print(i)
"""
['Shame' "Hangin'" 'Glory']
['The Nights' 'Warmth' 'Of The Night']
"""
```

## `nditer()`

If looping through multi-dimensional arrays, I'd suggest using `nditer()`

```py
arr = np.array([["Shame", "Hangin'", "Glory"],["The Nights", "Warmth", "Of The Night"]])
for i in np.nditer(arr):
    print(i)
"""
Shame
Hangin'
...
Of The Night
"""
```

### Slicing operation

Slicing can be done to loop through certain parts of the array.

```py
arr = np.array([["Shame", "Hangin'", "Glory", "My Blood"],["Riptide","The Nights", "Warmth", "Of The Night"]])
for i in np.nditer(arr[:, ::2]):
# select the entire array and go for 1st and 3rd elements
    print(i)
"""
Shame
Glory
Riptide
Warmth
"""
```

## `ndenumerate()`

It loops through the array and returns position and value of all elements.

```py
arr = np.array([["Shame", "Hangin'", "Glory", "My Blood"],["Riptide","The Nights", "Warmth", "Of The Night"]])
for i in np.ndenumerate(arr):
    print(i)
"""
((0, 0), 'Shame')
((0, 1), "Hangin'")
...
((1, 3), 'Of The Night')
"""
```

`index` and `value` are its two properties.

```py
for index, value in np.ndenumerate(arr):
    print(f"{value} is at position {index}")
"""
Shame is at position (0, 0)
Hangin' is at position (0, 1)
...
Of The Night is at position (1, 3)
"""
```
