import numpy as np
import random


def quick_sort(arr, l, r):
    '''
    Quick_sort
    '''
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

def select_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i, len(arr)-1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]




if __name__ == "__main__":
    arr = np.random.randint(10,size=20)
    print(arr)
    # quick_sort(arr, 0, len(arr)-1)
    select_sort(arr)
    print(arr)
