import numpy as np
import random

### Quick_sort

def quick_sort(arr, l, r):
    if l>=r: return
    low = l
    high = r
    key = arr[l]
    while l<r:
        while l<r and arr[r] > key:
            r -= 1
        arr[l] = arr[r]

        while l<r and arr[l] <= key:
            l += 1
        arr[r] = arr[l]
    
    arr[r] = key
    quick_sort(arr, low, l-1)
    quick_sort(arr, l+1, high)


if __name__ == "__main__":
    arr = np.random.randint(10,size=10)
    print(arr)
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
