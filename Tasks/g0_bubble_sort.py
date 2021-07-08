from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    #print(container)

    # go through the whole list
    for _ in range(0, len(container) - 1):
        for j in range(len(container) - 1):
            if container[j] > container[j + 1]:
                temp = container[j]
                container[j] = container[j + 1]
                container[j + 1] = temp

    #print(container)

    return container
