def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    table = [[0 for _ in range(shape[1])] for _ in range(shape[1])]
    table[0][0] = 1

    def get_paths(x, y):
        paths = 0
        if (x+2 > shape[1]-1 and (y-1 < 0 or y+1 > shape[1]-1)) \
                or (y+2 > shape[1]-1 and (x-1 < 0 or x+1 > shape[1]-1)):
            pass

    print(shape, point)
    return 0
