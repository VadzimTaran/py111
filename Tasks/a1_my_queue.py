"""
My little Queue
"""
from typing import Any

# basic container
my_queue = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing

    O(1)
    """
    print(elem)

    my_queue.append(elem)

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element

    O(N)
    """

    return my_queue.pop(0) if my_queue else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element

    O(1)
    """
    print(ind)

    if ind in range(len(my_queue)-1):
        return my_queue[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    my_queue.clear()

    return None
