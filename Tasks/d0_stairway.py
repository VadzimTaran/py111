from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    # reverse way
    stairs_cost = [float('inf')] * len(stairway)
    stairs_cost[0] = stairway[0]
    stairs_cost[1] = stairway[1]

    for curr_stair in range(len(stairway)):
        try:
            stairs_cost[curr_stair + 1] = min(stairs_cost[curr_stair + 1],
                                              stairway[curr_stair] + stairway[curr_stair + 1])
        except IndexError:
            pass

        try:
            stairs_cost[curr_stair + 2] = min(stairs_cost[curr_stair + 2],
                                              stairway[curr_stair] + stairway[curr_stair + 2])
        except IndexError:
            pass

    print(stairway)
    return stairs_cost[-1]


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    # direct way
    stairs_cost = [0] * len(stairway)
    stairs_cost[0] = stairway[0]
    stairs_cost[1] = min(stairway[1], stairway[0] + stairway[1])

    for curr_stair in range(2, len(stairway)):
        stairs_cost[curr_stair] = stairway[curr_stair] + min(stairway[curr_stair - 1], stairway[curr_stair - 2])

    print(stairway)
    return stairs_cost[-1]


def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    # reverse way
    stairs_cost = [float('inf')] * len(stairway)
    stairs_cost[0] = stairway[0]
    stairs_cost[1] = stairway[1]

    for curr_stair in range(len(stairway)):
        try:
            stairs_cost[curr_stair + 1] = min(stairs_cost[curr_stair + 1],
                                              stairway[curr_stair] + stairway[curr_stair + 1])
        except IndexError:
            pass

        try:
            stairs_cost[curr_stair + 2] = min(stairs_cost[curr_stair + 2],
                                              stairway[curr_stair] + stairway[curr_stair + 2])
        except IndexError:
            pass

    print(stairway)
    return stairs_cost[-1]


def lazy_stairway_path(stairway, current_stair):
    if current_stair == 0:
        return stairway[0]

    if current_stair == 1:
        return stairway[1]

    return stairway[current_stair] + min(lazy_stairway_path(stairway, current_stair-1),
                                         lazy_stairway_path(stairway, current_stair-2))
