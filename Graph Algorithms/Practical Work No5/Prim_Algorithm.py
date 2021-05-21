import random
from prio_queue import Priority_Queue, Pair


def Prim_Alg(graph):
    """
    Using Prim's Algorithm, we will return the minimal spanning tree of a given undirected graph.
    :param graph: an undirected graph.
    :return: the minimal spanning tree
    """

    # Initializing
    prio_queue = Priority_Queue()
    prev = [-1] * graph.NrOfVertices
    dist = [float("inf")] * graph.NrOfVertices
    edges = []
    vertex = 0
    vertices = [vertex]

    # initializing the distances
    for dest in graph.getOutboundNeighbours(vertex):
        dist[dest] = graph.getCostOfEdge((vertex, dest))
        prev[dest] = vertex
        pair = Pair(dest, dist[dest])
        # store all the neighbours of the randomly chosen vertex.
        prio_queue.push(pair)

    while not prio_queue.is_empty() and len(edges) < graph.NrOfVertices-1:
        # always get the element with the minimal priority and if it was not visited, store the vertex, edge, and parse all its neighbours.
        pair = prio_queue.pop()
        source = pair.first
        if source not in vertices:
            edges.append((prev[source], source, graph.getCostOfEdge((source, prev[source]))))
            vertices.append(source)
            for dest in graph.getOutboundNeighbours(source):
                if dist[dest] == float("inf") or graph.getCostOfEdge((source, dest)) < dist[dest]:
                    dist[dest] = graph.getCostOfEdge((source, dest))
                    prio_queue.push(Pair(dest, dist[dest]))
                    prev[dest] = source

    return edges, vertices[0]

def hamiltonCycle(graph):
    # get the MST
    edges, root = Prim_Alg(graph)
    # Initiliase a list for visiting the edges and an array for the previous
    visited = [0] * (len(edges) + 1)
    next = {}
    for i in range(graph.NrOfVertices):
        next[i] = []
    # simulate a stack.
    stack = [root]

    # setting the previous for every vertex in the MST
    for edge in edges:
        next[edge[0]].append(edge[1])

    vertex_walk = [root]
    size = 1
    total_cost = 0
    while len(stack) > 0:
        # get the element from the top of the stack
        current_node = stack.pop(len(stack) - 1)
        # parse the list to in preorder to get the nodes
        neighbours = next[current_node]
        for i in range(len(neighbours)-1, -1, -1):
            if neighbours[i] not in vertex_walk:
                stack.append(neighbours[i])
        # if the vertex is not the root, we add it to the walk.
        if current_node != root:
            vertex_walk.append(current_node)
            total_cost += graph.getCostOfEdge((vertex_walk[size - 1], current_node))
            size += 1

    # we append the root to end a cycle
    total_cost += graph.getCostOfEdge((vertex_walk[size - 1], root))
    vertex_walk.append(root)

    return total_cost, vertex_walk

