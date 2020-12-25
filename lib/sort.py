

class Sort:
    def __init__(self, arr):
        print(arr)

    def quick_sort(self, arr, l, r):
        if l>=r: 
            return
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
        self.quick_sort(arr, low, l-1)
        self.quick_sort(arr, l+1, high)

    def select_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

