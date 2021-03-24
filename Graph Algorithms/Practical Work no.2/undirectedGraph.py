from graph import DirectedGraph


class UndirectedGraph(DirectedGraph):
    def __init__(self):
        super().__init__()

    def BFS(self):

        visited = [False] * self.NrOfVertices
        connectedComp = []

        while False in visited:
            vertex = None
            index = 0
            # we find a vertex that has not been visited.
            while vertex is None and index < self.NrOfVertices:
                if visited[index] is False:
                    vertex = index
                index += 1

            # now in order to find the connected component that includes this vertex
            # we are going to perform a BFS.
            queue = []
            new_connectecComp = [vertex]
            visited[vertex] = True
            queue.append(vertex)
            while queue:
                current = queue.pop(0)
                # we know search through the current vertex neighbours in order to find unvisited vertices
                neighbours = self.getOutboundNeighbours(current)
                for vertex in neighbours:
                    if visited[vertex] is False:
                        visited[vertex] = True
                        queue.append(vertex)
                        new_connectecComp.append(vertex)
            # after the BFS was performed, we append the new component
            connectedComp.append(new_connectecComp)

        return connectedComp

    def readUndirectedGraph(self, file_name):
        """
       We read the undirected graph from a file.
       """

        file = open(file_name, "r")
        lines = file.readline()
        line = lines.split()
        vertices = int(line[0])
        edges = int(line[1])

        lines = file.readlines()
        for line in lines:
            try:
                line = line.split()
                firstPoint = int(line[0])
                secondPoint = int(line[1])
                self.addVertex(firstPoint, True)
                self.addVertex(secondPoint, True)
                self.addEdge(firstPoint, secondPoint, 0, True)
                self.addEdge(secondPoint, firstPoint, 0, True)
            except Exception:
                pass

        index = 0
        self.NrOfEdges //= 2
        while self.NrOfVertices < vertices:
            self.addVertex(index, True)
            index += 1

        file.close()

    def writeUndirectedGraph(self, file_name):
        with open(file_name, "w") as file:
            file.write("%d %d \n" % (self.NrOfVertices, self.NrOfEdges))
            for vertex in self.getAllVertices():
                vertex_list = self.getOutboundNeighbours(vertex)
                for destination in vertex_list:
                    file.write("%d %d \n" % (vertex, destination))

            file.close()

