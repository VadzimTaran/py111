from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)

    if not len(arr):
        return None

    mid = len(arr) // 2
    mid_val = arr[mid]

    if len(arr) == 1 and mid_val != elem:
        return None

    if mid_val == elem:
        while mid-1 >= 0 and arr[mid-1] == elem:
            mid -= 1
        return mid

    if mid_val > elem:
        res = binary_search(elem, arr[:mid-1])
        if res is None:
            return None
    else:
        res = binary_search(elem, arr[mid + 1:])
        if res is None:
            return None
        else:
            res += (mid + 1)
    return res
