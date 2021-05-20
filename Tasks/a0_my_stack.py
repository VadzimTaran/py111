"""
My little Stack
"""
from typing import Any

# stack variable
my_stack = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing

    O(1)
    """
    print(elem)

    my_stack.append(elem)

    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element

     O(1)
    """

    popped_elem = None if not my_stack else my_stack[len(my_stack)-1]
    my_stack.pop()

    return popped_elem


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place

     O()
    """
    print(ind)
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None

     O()
    """
    return None


if __name__ == '__main__':
    for i in range(10):
        push(i)
    print(my_stack)

    for _ in range(10):
        pop()
    print(my_stack)