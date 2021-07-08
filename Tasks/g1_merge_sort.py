from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) <= 1:
        return container

    # divide
    # middle
    mid = len(container) // 2
    # left part
    left_part = container[:mid]
    # right part
    right_part = container[mid:]
    # sort left part
    sort(left_part)
    # sort right part
    sort(right_part)

    # merge
    # iterators for parts
    i = 0
    j = 0
    # main iterator
    k = 0
    # copy from parts to main cont:
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            container[k] = left_part[i]
            # next in left
            i += 1
        else:
            container[k] = right_part[j]
            # next in right
            j += 1
        # next in main
        k += 1

    # check leftovers
    while i < len(left_part):
        container[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        container[k] = right_part[j]
        j += 1
        k += 1

    return container
