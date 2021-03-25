from graph import DirectedGraph


class UndirectedGraph(DirectedGraph):
    def __init__(self):
        super().__init__()

        # This will keep the time needed to discover a component.
        self.Time = 0

        # This is a list which will store the Biconnected components of the graph
        self.BiConComp = []

    def BFS(self):
        # connectedComp will keep a list for each connected component
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

    def BCCFind(self, current_vertex, parent, discovery, fastestDiscovery, stack):
        # We set the finding times for the current vertex
        discovery[current_vertex] = self.Time
        fastestDiscovery[current_vertex] = self.Time
        self.Time += 1
        children = 0 # this will keep the number of children

        # we parse through the set of all the neighbours of the current vertex

        # The below list can be replaced by a simple of neighbours, but I adapted the previous
        # Laboratory work for this problem.
        neighbours = self.getOutboundNeighbours(current_vertex)
        for neighbour in neighbours:
            # if the vertex wasn't discovered already, it means it is accessible
            if discovery[neighbour] == -1:
                # the parent of the neighbour will be the current vertex
                parent[neighbour] = current_vertex
                children += 1
                stack.append((current_vertex, neighbour))
                self.BCCFind(neighbour, parent, discovery, fastestDiscovery, stack)

                # If the current NEIGHBOUR has a connection with any ancestor of the current rooted vertex
                # there might be a chance that the current neighbour can be discovered faster => we have to change
                # the faster discovery time for the current vertex

                fastestDiscovery[current_vertex] = min(fastestDiscovery[current_vertex], fastestDiscovery[neighbour])

                # We know need to make sure that the current vertex is not an ARTICULATION POINT.

                # The first case: when the parent is -1, is when we get back to the initial root of the traversal and there are more than 1 children
                # The second case is when the fastest discovery time of the neighbour is bigger than the discovery time of the current vertex
                if (parent[current_vertex] == -1 and children > 1) or (parent[current_vertex] != -1 and fastestDiscovery[neighbour] > discovery[current_vertex]):
                    edge = 0
                    newBCC = []
                    # we know have a new BCC and pop from the stack, all the edges until the one that is between
                    # the current_vertex and the neighbour
                    while edge != (current_vertex, neighbour):
                        edge = stack.pop()
                        if edge[0] not in newBCC:
                            newBCC.append(edge[0])
                        if edge[1] not in newBCC:
                            newBCC.append(edge[1])
                    self.BiConComp.append(newBCC)

            # if the neighbour isn't accessible, there might be a chance that it could have a faster discovery time
            elif parent[current_vertex] != neighbour and fastestDiscovery[current_vertex] > discovery[neighbour]:
                fastestDiscovery[current_vertex] = discovery[neighbour]
                # we also append this edge to the stack because it changes discovery times and
                # also is in the same BCC
                stack.append((current_vertex, neighbour))

    def BiConnectedComp(self):
        # on the stack we are going to add the edges
        stack = []
        discovery = [-1] * self.NrOfVertices
        fastestDiscovery = [-1] * self.NrOfVertices
        parent = [-1] * self.NrOfVertices
        self.Time = 0

        for vertex in range(self.NrOfVertices):
            # If the vertex hasn't been discovered, we do a dfs on him.
            if discovery[vertex] == -1:
                self.BCCFind(vertex, parent, discovery, fastestDiscovery, stack)
            # If the stack is not empty, it means that there is still one BBC
            # that includes the initial root vertex for the DFS
            if stack:
                # we now create a new component
                newBCC = []
                while stack:
                    edge = stack.pop()
                    if edge[0] not in newBCC:
                        newBCC.append(edge[0])
                    if edge[1] not in newBCC:
                        newBCC.append(edge[1])
                self.BiConComp.append(newBCC)

        return self.BiConComp

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