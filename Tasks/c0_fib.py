from itertools import count

def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)

    if n < 0:
        raise ValueError

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_recursive(n-2) + fib_recursive(n-1)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)

    if n < 0:
        raise ValueError

    if n == 0:
        return 0

    if n == 1:
        return 1

    res = [0 for _ in range(n+1)]

    res[1] = 1

    for i in range(2, n+1):
        res[i] = res[i-1] + res[i-2]

    return res[n]
