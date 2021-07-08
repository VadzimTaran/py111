from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    #print(container)

    # go through the whole list
    for i in range(0, len(container) - 1):
        # improvement: check swapping
        elem_swapped = False
        # range can be shorten by i because max value is shifted to the most right place
        for j in range(len(container) - i - 1):
            if container[j] > container[j + 1]:
                # swap in python's way
                container[j], container[j + 1] = container[j + 1], container[j]
                # set swapped to True
                elem_swapped = True
        # if no elements swapped - container is sorted; no need to go through it any more
        if not elem_swapped:
            break

    #print(container)

    return container
