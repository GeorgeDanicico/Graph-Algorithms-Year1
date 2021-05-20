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
    vertex = random.choice(graph.getVertices())
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
            edges.append((source, prev[source], graph.getCostOfEdge((source, prev[source]))))
            vertices.append(source)
            for dest in graph.getOutboundNeighbours(source):
                if dist[dest] == float("inf") or graph.getCostOfEdge((source, dest)) < dist[dest]:
                    dist[dest] = graph.getCostOfEdge((source, dest))
                    prio_queue.push(Pair(dest, dist[dest]))
                    prev[dest] = source

    return edges, vertices[0]
