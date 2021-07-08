from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) <= 1:
        return container

    def partition(list_, start_, end_):
        pivot_idx = len(container) // 2
        pivot = list_[pivot_idx]
        left = start_ + 1 if pivot_idx == start_ else start_
        right = end_
        done = False
        while not done:
            while left <= right and list_[left] <= pivot:
                left = left + 1
            while list_[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                list_[left], list_[right] = list_[right], list_[left]
        list_[start_], list_[right] = list_[right], list_[start_]
        return right

    def quickSort(list_, start_, end_):
        if start_ < end_:
            pivot = partition(list_, start_, end_)
            quickSort(list_, start_, pivot - 1)
            quickSort(list_, pivot + 1, end_)
        return list_

    return quickSort(container, 0, len(container)-1)
