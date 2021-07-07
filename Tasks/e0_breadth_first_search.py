from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """

    # queue for processing nodes; put the 1st element
    queue = [start_node]

    # queue for visited nodes; put the 1st element
    visited = [start_node]

    # check the queue, until not empty
    while queue:
        # take 1st elem from queue and remove it
        procd_elem = queue.pop(0)
        # check neighbours
        for neighbour in g[procd_elem]:
            # visited?
            if neighbour not in visited:
                # no
                # add it into visited
                visited.append(neighbour)
                # add it into queue for next processing
                queue.append(neighbour)

    return visited

