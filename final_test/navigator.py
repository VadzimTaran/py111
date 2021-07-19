# Навигатор на сетке.
# Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
# (все стоимости положительные).
# Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.

from random import randint
from tabulate import tabulate

# size
N = 10

# go down or right


# calculate cost of arrival into cells
def calculate_costs(array):
    arr_sz = len(array)
    # temporary array for calculation
    tmp_arr = [[0 for _ in range(arr_sz)] for _ in range(arr_sz)]  # fill with 0-s
    # print(tabulate(tmp_arr, headers=[k for k in range(arr_sz)], showindex="always"))

    # start with low right corner
    tmp_arr[arr_sz - 1][arr_sz - 1] = array[arr_sz - 1][arr_sz - 1]  #

    # fill low row (going left)
    for j in range(arr_sz - 2, -1, -1):
        tmp_arr[arr_sz - 1][j] = tmp_arr[arr_sz - 1][j + 1] + array[arr_sz - 1][j]

    # fill low column (going up)
    for j in range(arr_sz - 2, -1, -1):
        tmp_arr[j][arr_sz - 1] = tmp_arr[j + 1][arr_sz - 1] + array[j][arr_sz - 1]

    # fill all other cells
    for i in range(arr_sz - 2, -1, -1):  # i - row
        for j in range(arr_sz - 2, -1, -1):  # j  - column
            # value
            tmp_arr[i][j] = array[i][j] + min(tmp_arr[i + 1][j], tmp_arr[i][j + 1])

    return tmp_arr


# find and display the path
def find_path(arr):
    sz = len(arr)
    # fill with dots
    str_arr = [["." for _ in range(sz)] for _ in range(sz)]
    str_arr[0][0] = "*"  # start

    i = 0  # i - row
    j = 0  # j  - column
    while True:
        next_steps = [[i, j + 1], [i + 1, j]]  # next steps: low or right
        next_vals = [arr[i][j + 1], arr[i + 1][j]]  # values of correspondent cells to move to
        i, j = next_steps[next_vals.index(min(next_vals))]  # next - min val
        str_arr[i][j] = "*"
        if i == sz - 1:  # reached the lowest row
            while j <= sz - 1:  # go to the very right column
                str_arr[i][j] = "*"  # go right
                j += 1
            break
        if j == sz - 1:  # reached the right row
            while i <= sz - 1:  # go down
                str_arr[i][j] = "*"
                i += 1
            break
    return str_arr


if __name__ == '__main__':
    grid = [[randint(0, 50) for _ in range(N)] for _ in range(N)]

    print(tabulate(grid, headers=[i for i in range(N)], showindex="always"))

    np_t = calculate_costs(grid)  # calculate cost of paths
    # print(tabulate(np_t, headers=[i for i in range(N)], showindex="always"))

    print('Min cost path:')
    print(tabulate(find_path(np_t)))  # print path
