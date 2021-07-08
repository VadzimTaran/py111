from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) <= 1:
        return container

    pivot_idx = len(container) // 2
    pivot = container[pivot_idx]

    less_part = [less_val for less_val in container if less_val < pivot]
    equal_part = [equal_val for equal_val in container if equal_val == pivot]
    more_part = [more_val for more_val in container if more_val > pivot]

    return sort(less_part) + equal_part + sort(more_part)
