
## Joining arrays

We can join arrays using `concatenate()` to their axes.

```py
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])

x = np.concatenate((a,b), axis=0)
print(x)
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""
```

```py
x = np.concatenate((a,b), axis=1)
print(x)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""
```

`stack()` joins them to a new axis.

```py
x = np.stack((a,b), axis=0)
print(x)
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""
```

```py
x = np.stack((a,b), axis=1)
print(x)
"""
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
"""
```
