import numpy as np
import random
from lib.sort import Sort


if __name__ == "__main__":
    arr = np.random.randint(10,size=30)
    sort = Sort(arr)

    sorted_arr = sort.select_sort(arr)
    print('select_sort:', sorted_arr)

    sort.quick_sort(arr, 0, len(arr)-1)
    print('quick_sort :', arr)