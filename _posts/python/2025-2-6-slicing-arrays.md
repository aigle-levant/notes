---
title: "Slicing arrays"
subtitle: "NumPy Arrays : Python"
categories: [lang-notes, python]
tags: [numpy, arrays]
---

## Slicing arrays using a range

We can slice index using a `[start:end:step]` range.

- If `start` is excluded, it is 0
- If `end` is excluded, it is the length of the array
- If `step` is excluded, it is 1

Result includes `start` and excludes `end`.

```py
arr = np.array(["Apt", "Dynamite", "Hangin'", "Beetlebum 2012", "Song 2"])
print(arr[1:4])
# ['Dynamite' "Hangin'" 'Beetlebum 2012']
print(arr[:4])
# ['Apt' 'Dynamite' "Hangin'" 'Beetlebum 2012']
print(arr[1:])
# ['Dynamite' "Hangin'" 'Beetlebum 2012' 'Song 2']
print(arr[0:len(arr):2])
# ['Apt' "Hangin'" 'Song 2']
```

In case of 2-D array, specify which part and then slice.

```py
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0,2:4]) # [3 4]
print(arr[1,::2]) # [ 6 8 10]
```
