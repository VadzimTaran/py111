from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)

    start = 0
    end = len(arr) - 1
    mid = 0

    while start <= end:
        mid = start // 2 + end // 2

        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            end = mid - 1
        else:
            start = mid + 1

    return None

