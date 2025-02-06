---
title: "Creating Arrays"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## Creating arrays using NumPy

We can create arrays using one of the two modules : `numpy` and `array`. I'd prefer using the former.

```py
import numpy as np

array = np.array(["APT", "Hey Brother", "Winter of Our Youth"])
print(array) # ['APT' 'Hey Brother' 'Winter of Our Youth']
```

> Arrays made using `numpy` belong to the class `numpy.ndarray`.

Every element in an array must be of the same datatype. However, they can be modified, add and deleted.

### Dimensions

0-D arrays have a single element. No brackets will be there for this one.

```py
import numpy as np

array = np.array(42)
print(array) # 42
```

1-D arrays are just your regular arrays.

```py
import numpy as np

array = np.array(["APT", "Hey Brother", "Winter of Our Youth"])
print(array) # ['APT' 'Hey Brother' 'Winter of Our Youth']
```

2-D arrays have 1-D arrays as their elements. They're used to show matrices.

```py
import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
```

3-D arrays have 2-D arrays as their elements.

```py
import numpy as np

array = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(array)
"""
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
"""
```

#### `ndim`

`ndim` tells you the dimension of the array.

```py
a = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
b = np.array("String")
c = np.array(["APT", "Dynamite", "Move"])
print(a.ndim) # 3
print(b.ndim) # 0
print(c.ndim) # 1
```

#### `ndmin`

`ndmin` lets you define dimensions for your array.

```py
arr = np.array([1,2,3,4], ndmin=4)
print(arr) # [[[[1 2 3 4]]]]
```

### Accessing arrays

To access 2-D arrays, think of them as table with rows and columns. Use the index numbers accordingly.

```py
arr = np.array([[10,20,30],[5,10,15]])
print(arr[0][1]) # 20
print(arr[1][2]) # 15
print(arr[1]) # [5 10 15]
print(arr[0]) # [10 20 30]
```

Do a similar thing with 3-D arrays.

```py
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[1])
"""
[[ 7  8  9]
 [10 11 12]]
"""
print(arr[1][0]) # [7 8 9]
print(arr[1][0][2]) # 9
```

#### Negative indexing

Use negative indexing to access array from end.

```py
arr = np.array(["Apt", "Dynamite", "Hangin'", "Beetlebum 2012"])
print(arr[-1]) # Beetlebum 2012
```
