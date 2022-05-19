import math
import numpy as np


def binarysearch(arr, i, r, x):
    if r >= i:
        mid = i + math.floor((r - i) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, i, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, r, x)
    else:
        return -1


arr = np.array([23, 25, 28, 32, 39, 42, 48, 49, 56, 59])
arr.sort()
q = 56
print(binarysearch(arr, 0, len(arr) - 1, q))
