---
title: "Copy vs View"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## Array Copy

`copy` creates a duplicate of the original array with all its elements intact. Any changes made to it doesn't affect the original array.

```py
arr = np.array(["Shame", "Hangin'", "Glory", "My Blood"])
new_arr = arr.copy()
new_arr[1] = "Hit It"
print(arr) # ['Shame' "Hangin'" 'Glory' 'My Blood']
print(new_arr) # ['Shame' 'Hit It' 'Glory' 'My Blood']
```

> Use `copy` if you don't want the original array to be affected.

## Array view

`view` lets you create a view of the original array. Changes made to the `view` will affect the original array and vice versa.

```py
arr = np.array(["Shame", "Hangin'", "Glory", "My Blood"])
new_arr = arr.copy()
new_arr[1] = "Hit It"
print(arr) # ['Shame' "Hangin'" 'Glory' 'My Blood']
print(new_arr) # ['Shame' 'Hit It' 'Glory' 'My Blood']
```

> Use `view` if you wish to save memory.

## `base`

It returns `None` if the array is a copy. If not, it refers the original array.

```py
arr = np.array([1,2,3])
x = arr.copy()
y = arr.view()

print(x.base) # None
print(y.base) # [1 2 3]

z = x.copy()
print(z.base) # None

w = y.view()
w[0] = 100
print(w.base) # [100   2   3]
```
