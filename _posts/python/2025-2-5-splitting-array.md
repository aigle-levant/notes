---
title: "Splitting arrays"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## `array_split()`

It is used to split an array into a given number of sub-arrays.

```py
arr = np.array([[1,2,3],[4,5,6]])
new_arr = np.array_split(arr, 2)
print(new_arr)
# [array([[1, 2, 3]]), array([[4, 5, 6]])]
```

If the number of elements are lesser than the sub-arrays specified, it'll use `null` value to make up the missing elements.

```py
arr = np.array([1,2,3,4])
new_arr = np.array_split(arr, 5)
print(new_arr)
# [array([1]), array([2]), array([3]), array([4]), array([], dtype=int32)]
```

### Accessing using index

We can access array elements after split with their index

```py
arr = np.array([1,2,3,4])
new_arr = np.array_split(arr, 5)
print(new_arr[0]) # [1]
print(new_arr[4]) # []
```

### `axis`

We can specify which axis we want to do split around using `axis` attribute.

```py
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = np.array_split(arr, 3, axis=1)
print(new_arr)
"""
[array([[1],
       [4]]), array([[2],
       [5]]), array([[3],
       [6]])]
"""
```

## Horizontal split : `hsplit`

It splits an array horizontally [along the columns].

```py
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = np.hsplit(arr, 3)
print(new_arr)
"""
[array([[1],
       [4]]), array([[2],
       [5]]), array([[3],
       [6]])]
"""
```

> Use `hsplit` when you need to divide an array column-wise.

## Horizontal Stack : `hstack`

It stacks [combines] arrays horizontally [column-wise].

```py
arr = np.array([[1, 2, 3], [4, 5, 6]])
x = np.array([[10,20,30], [50,60,70]])
new_arr = np.hstack((arr,x))
print(new_arr)
"""
[[ 1  2  3 10 20 30]
 [ 4  5  6 50 60 70]]
"""
```

> Use `hstack` if you wanna combine arrays by adding more columns.

## Vertical Split : `vsplit`

It splits an array vertically [row-wise]

```py
arr = np.array([[1, 2, 3], [4, 5, 6]])
x = np.vsplit(arr,2)
print(x)
# [array([[1, 2, 3]]), array([[4, 5, 6]])]
```

> Use `vsplit` when you want to divide an array row-wise.

## Depth Split : `dsplit`

It splits an array depth-wise and is only used for 3-D or higher dimension arrays.

```py
arr = np.array([[[1, 2, 3],
                 [4, 5, 6]],
                [[7, 8, 9],
                 [10, 11, 12]]])

new_arr = np.dsplit(arr,3)
print(new_arr)
"""
[array([[[ 1],
        [ 4]],

       [[ 7],
        [10]]]), array([[[ 2],
        [ 5]],

       [[ 8],
        [11]]]), array([[[ 3],
        [ 6]],

       [[ 9],
        [12]]])]
"""
```

> Use `dsplit` if you want your higher-dimension array to divided along the depth.
