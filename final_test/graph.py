# Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
# Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
# Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
#
# В графе на картинке – три подграфа, т.е. число компонент связности = 3.

import networkx as nx


# try to find routes from nodes using breadth algorithm
def getGraphNumber(gr: nx.Graph) -> int:
    if not len(gr):
        return 0
    # nodes in graph
    nodes = [n for n in gr.nodes().keys()]
    # number of graphs
    graph_num = 0
    # check path from each
    while len(nodes) > 0:
        node_ = nodes[0]
        queue = [node_]
        # queue for visited nodes; put the 1st element
        visited = [node_]
        # check the queue, until not empty
        while queue:
            # take 1st elem from queue and remove it
            procd_elem = queue.pop(0)
            # check neighbours
            for neighbour in graph[procd_elem]:
                # visited?
                if neighbour not in visited:
                    # no
                    # add it into visited
                    visited.append(neighbour)
                    # add it into queue for next processing
                    queue.append(neighbour)
        print(visited)
        graph_num += 1
        # remove visited nodes (1 graph)
        for node in visited:
            nodes.remove(node)
    return graph_num


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('F', 'G'),
    ])

    num = getGraphNumber(graph)
    print(num)
