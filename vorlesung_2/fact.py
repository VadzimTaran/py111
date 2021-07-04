# n! = 1*2*3*4*...*(n-1)*n
#  fact(n) = 1, n = 0; (n-1)!*n, n>=1

def factorial(n):
    if n == 0:
        return 1  # базовый случай (обязательно)
    return factorial(n - 1) * n  # рекурсивный вызов


if __name__ == '__main__':
    print(factorial(998))
