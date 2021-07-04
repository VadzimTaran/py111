"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    # empty arr
    if not len(arr):
        return -1

    # set min - first elem
    min_value = arr[0]
    min_idx = 0

    # go through the whole arr to check each elem - compare it with min
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_idx = i

    print(arr)

    return min_idx
