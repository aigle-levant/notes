---
title: "Shape of an array"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## Shape of an array

It is the number of elements in each dimension. To be more specific, it is no. of elements along each axis.

```py
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape) # (2,3)
# 2 rows and 3 columns
```

```py
x = np.array([1,2,3])
print(x.shape) # (3,)
# 3 rows and 0 columns
```

## `reshape()`

It lets you change the shape of the array.

```py
arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(3,2)
print(new_arr)
"""
[[1 2]
 [3 4]
 [5 6]]
"""
# 3 rows and 2 columns
```

```py
arr = np.array([1,2,3])
new_arr = arr.reshape(3,1)
print(new_arr)
"""
[[1]
 [2]
 [3]]
"""
# 3 rows and 1 column
```

### `-1`

It is used as placeholder for unknown dimension. NumPy will automatically infer the correct size if its used.

```py
arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(3,-1)
print(new_arr)
"""
[[1 2]
 [3 4]
 [5 6]]
"""
# 3 rows and [2] columns
```

> `-1` can only be used for 1 dimension

## `flatten()`

It lets you convert multi-dimensional array into 1-D array.

```py
arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.flatten()
print(new_arr) # [1 2 3 4 5 6]
```

An alternative to this is `reshape(-1)`.

```py
arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(-1)
print(new_arr) # [1 2 3 4 5 6]
```
