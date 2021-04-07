
# the function below generates the path from source vertex to destination vertex.
# def DFS(graph, src, vertex, path, dist):
#
#     path.append(vertex)
#     if vertex != src:
#         for neighbour in graph.getInboundNeighbours(vertex):
#             if dist[neighbour] == dist[vertex] - graph.getCostOfEdge((neighbour, vertex)):
#                 return DFS(graph, src, neighbour, path[:], dist)
#
#     else:
#         return path

def generatePath(prev, src, destination):
    path = [destination]
    vertex = destination
    while vertex != src:
        path.append(prev[vertex])
        vertex = prev[vertex]

    path.reverse()

    return path

def BellmanFordAlgortihm(graph, v1, v2):
    """
    This function will compute the minimum cost path from vertex v1 to vertex v2 if it exists
        - If in the graph there is a negative cost cycle, we throw an error.
    :param v2: the destination vertex
    :param v1: the source vertex
    :param graph: the graph object which contain all the vertices and all the edges.
    :return: the minimum cost of the walk from v1 to v2, or None if there is no walk from v1 to v2.
    """

    # We make all the distances equal to infinity
    dist = [float("inf")] * graph.NrOfVertices
    # Except for the source vertex
    dist[v1] = 0
    prev = [0] * graph.NrOfVertices
    changed = True
    while changed:
        changed = False
        for edge in graph.getAllEdges():
            vertex1 = edge[0]
            vertex2 = edge[1]
            cost = graph.getCostOfEdge(edge)
            if dist[vertex1] != float("inf") and dist[vertex2] > dist[vertex1] + cost:
                dist[vertex2] = dist[vertex1] + cost
                prev[vertex2] = vertex1
                changed = True

    for edge in graph.getAllEdges():
        vertex1 = edge[0]
        vertex2 = edge[1]
        cost = graph.getCostOfEdge(edge)
        if dist[vertex1] != float("inf") and dist[vertex2] > dist[vertex1] + cost:
            raise Exception("Negative cost cycle detected!\n")

    if dist[v2] != float("inf"):

        path = generatePath(prev, v1, v2)
        return dist[v2], path

    return None