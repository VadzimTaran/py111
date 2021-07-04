"""
Taylor series
"""
from typing import Union
from math import factorial

DELTA = 0.0001

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)
    return 0


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    print(x)

    def _get_item(n):
        # only more than 1
        if not n >= 1:
            raise ValueError

        # only int
        if not isinstance(n, int):
            raise TypeError

        return ((-1) ** (n + 1)) * (x ** (2 * n - 1)) / factorial(2 * n - 1)

    res = 0
    n = 1 # Todo itertools: count
    while True:
        current_elem = _get_item(n)
        if abs(current_elem) < DELTA:
            break
        res += current_elem
        n += 1

    return res
