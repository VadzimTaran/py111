from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    print(g, start_node)

    # visited nodes
    visited = []

    # special routine
    def dfsRoutine(visited_lst: list, graph: nx.Graph, node: Hashable):
        # Mark the current node as visited
        visited_lst.append(node)
        # For all neighbours
        for neighbour in graph[node]:
            # node is not processed yet
            if neighbour not in visited_lst:
                # process
                dfsRoutine(visited_lst, graph, neighbour)

    dfsRoutine(visited, g, start_node)

    return visited