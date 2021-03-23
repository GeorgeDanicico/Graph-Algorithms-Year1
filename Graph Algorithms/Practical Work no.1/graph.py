import random
from copy import deepcopy


class DirectedGraph:
    def __init__(self):
        """
        The initialisation of the graph
        """
        self.__numberOfVertices = 0
        self.__numberOfEdges = 0
        self.__dictIn = {}
        self.__dictOut = {}
        self.__dictCost = {}

    @property
    def NrOfEdges(self):
        return self.__numberOfEdges

    @property
    def NrOfVertices(self):
        return self.__numberOfVertices

    @NrOfEdges.setter
    def NrOfEdges(self, value):
        self.__numberOfEdges = value

    @NrOfVertices.setter
    def NrOfVertices(self, value):
        self.__numberOfVertices = value

    @staticmethod
    def generateRandomGraph(vertices, edges):
        randomGraph = DirectedGraph()
        randomGraph.NrOfEdges = 0
        randomGraph.NrOfVertices = 0
        for i in range(vertices):
            randomGraph.addVertex(i, True)

        copy_edges = edges
        while copy_edges:
            try:
                startPoint = random.randint(0, vertices - 1)
                endPoint = random.randint(0, vertices - 1)
                cost = random.randint(0, 200)
                randomGraph.addEdge(startPoint, endPoint, cost, False)
                copy_edges -= 1
            except ValueError:
                pass

        return randomGraph

    def __initGraph(self):
        """
        This function initialize the dictionaries.
            It sets for every vertex an empty list.
        """
        for i in range(self.__numberOfVertices):
            self.__dictIn[i] = []
            self.__dictOut[i] = []

    def getAllVertices(self):
        for i in self.__dictOut.keys():
            yield i

    def getGraphCopy(self):
        return deepcopy(self)

    def getInboundNeighbours(self, vertex):
        """
        This function returns the inbound neighbours of a vertex, if it exists.
        :param vertex: integer number representing the vertex
        :return:
        """
        if self.vertexExistence(vertex):
            return self.__dictIn[vertex]
        raise ValueError("The vertex does not exists...\n")

    def getOutboundNeighbours(self, vertex):
        """
        This function returns the inbound neighbours of a vertex, if it exists.
        :param vertex: integer number representing the vertex
        :return:
        """
        if self.vertexExistence(vertex):
            return self.__dictOut[vertex]
        raise ValueError("The vertex does not exists...\n")

    def getCostOfEdge(self, edge):
        """
        This fun1ction returns the cost of an edge if it exists/ otherwise it raises an error.
        :param edge: a tuple of 2 integer numbers, representing the starting and ending poiny of the edge.
        :return: the cost of an edge if it exists/otherwise an error.
        """
        if self.edgeExistence(edge):
            return self.__dictCost[edge]
        raise ValueError("The edge does not exist...\n")

    def getIndegreeVertex(self, vertex):
        """
        This function returns the indegree of a specific vertex, if it exists.
        :param vertex: integer number representing the vertex
        :return: the indegree if the vertex exists/ otherwise an error.
        """
        if self.vertexExistence(vertex):
            return len(self.__dictIn[vertex])
        raise ValueError("The vertex does not exists...\n")

    def getOutdegreeVertex(self, vertex):
        """
        This function returns the indegree of a specific vertex, if it exists.
        :param vertex: integer number representing the vertex
        :return: the indegree if the vertex exists/ otherwise an error.
        """
        if self.vertexExistence(vertex):
            return len(self.__dictOut[vertex])
        raise ValueError("The vertex does not exists...\n")

    def setCostEdge(self, edge, cost):
        if self.edgeExistence(edge):
            self.__dictCost[edge] = cost
        else:
            raise ValueError("Invalid input. The edge does not exist.\n")

    def vertexExistence(self, vertex):
        """
        This function checks if a specific vertex exists in the graph.
        :param vertex: integer number, the vertex
        """
        return vertex in self.__dictOut.keys()

    def edgeExistence(self, edge):
        """
        This function checks if a specific edge exists in the graph.
        :param edge: a tuple of 2 integer numbers, representing the starting and ending poiny of the edge.
        """
        return edge in self.__dictCost.keys()

    def deleteVertex(self, vertex):
        """
        This function deletes a vertex from a graph.
            - From each inbound/outbound neighbour we delete the corresponding edges.
            - After that we delete the 'vertex' key from both dictIn and dictOut
        :param vertex: an integer number representing the vertex.
        """
        if self.vertexExistence(vertex):
            copy_dictIn = self.__dictIn[vertex][:]
            for neighbour in copy_dictIn:
                self.deleteEdge((neighbour, vertex))
            copy_dictOut = self.__dictOut[vertex][:]
            for neighbour in copy_dictOut:
                self.deleteEdge((vertex, neighbour))

            del self.__dictIn[vertex]
            del self.__dictOut[vertex]
            self.__numberOfVertices -= 1
        else:
            raise ValueError("The vertex does not exist")

    def deleteEdge(self, edge):
        """
        This function deletes an edge from the graph.
        :param edge: a tuple of integers, representing the ending points of an edge
        """
        if self.edgeExistence(edge):
            self.__dictIn[edge[1]].remove(edge[0])
            self.__dictOut[edge[0]].remove(edge[1])
            edge1 = edge
            del self.__dictCost[edge]
            self.__numberOfEdges -= 1
        else:
            raise ValueError("The edge does not exist.\n")

    def addEdge(self, startPoint, endPoint, cost, load_time):
        """
        Adds a new edge.
        :param load_time:
        :param cost: the cost of the edge.
        :param startPoint: integer number, the starting point of the edge.
        :param endPoint: integer number, the ending point of the edge.
        """
        if self.edgeExistence((startPoint, endPoint)) is False:
            self.__numberOfEdges += 1
            self.__dictIn[endPoint].append(startPoint)
            self.__dictOut[startPoint].append(endPoint)
            self.__dictCost[(startPoint, endPoint)] = cost

        else:
            if load_time is False:
                raise ValueError("The edge already exists")

    def addVertex(self, vertex, load_time):
        """
        We add a new vertx and also increment the total number of vertices
        :param load_time:
        :param vertex: integer number, that represents a new vertex
        """

        if self.vertexExistence(vertex) is False:
            self.__numberOfVertices += 1
            self.__dictIn[vertex] = []
            self.__dictOut[vertex] = []
        else:
            if load_time is False:
                raise ValueError("The vertex already exist.")

    def loadGraph1(self, graph_file):
        """
        Load graph data from a given file in the first reading mode.
        :param graph_file: the text file that contains the data
        """
        file_open = open(graph_file, "r")

        first_line = file_open.readline().split()
        if len(first_line) != 2:
            raise Exception("Invalid input file!\n")

        try:
            self.__numberOfVertices = int(first_line[0])
            self.__numberOfEdges = int(first_line[1])
        except ValueError as ve:
            raise ValueError("Invalid values in the file. Please check the file.\n")

        # Because we increment both the total number of vertices and edges, after we checked if they
        # are valid in the file, we set them to 0 before initialising the vertices and edges.
        vertices = self.__numberOfVertices
        self.__numberOfVertices = 0
        self.__numberOfEdges = 0

        for i in range(vertices):
            self.addVertex(i, True)

        lines = file_open.readlines()
        file_open.close()

        for line in lines:
            line = line.split()
            try:
                startPoint = int(line[0])
                endPoint = int(line[1])
                cost = int(line[2])
                self.addEdge(startPoint, endPoint, cost, True)
                # self.setCostEdge((startPoint, endPoint), cost)
            except ValueError as ve:
                raise ValueError("Invalid values in the file. Please check the file.\n")

    def loadGraph2(self, graph_file):
        """
        Load graph data from a given file in the first reading mode.
        :param graph_file: the text file that contains the data
        """
        file_open = open(graph_file, "r")

        first_line = file_open.readline().split()
        if len(first_line) != 2:
            raise Exception("Invalid input file!\n")

        try:
            self.__numberOfVertices = int(first_line[0])
            self.__numberOfEdges = int(first_line[1])
        except ValueError as ve:
            raise ValueError("Invalid values in the file. Please check the file.\n")

        # Because we increment both the total number of vertices and edges, after we checked if they
        # are valid in the file, we set them to 0 before initialising the vertices and edges.
        vertices = self.__numberOfVertices
        self.__numberOfVertices = 0
        self.__numberOfEdges = 0

        for i in range(vertices):
            self.addVertex(i, True)

        lines = file_open.readlines()
        file_open.close()

        for line in lines:
            line = line.split()
            try:
                startPoint = int(line[0])
                if len(line) == 3:
                    endPoint = int(line[1])
                    cost = int(line[2])
                    self.addEdge(startPoint, endPoint, cost, True)
                    # self.setCostEdge((startPoint, endPoint), cost)
            except ValueError as ve:
                raise ValueError("Invalid values in the file. Please check the file.\n")

    def writeGraph1(self, graph_file):

        with open(graph_file, "w") as output:
            output.write("%d %d\n" % (self.__numberOfVertices, self.__numberOfEdges))
            for i in self.getAllVertices():
                pass
                for vertex in self.__dictOut[i]:
                    output.write("%d %d %d\n" % (i, vertex, self.getCostOfEdge((i, vertex))))

            output.close()

    def writeGraph2(self, graph_file):

        with open(graph_file, "w") as output:
            output.write("%d %d\n" % (self.__numberOfVertices, self.__numberOfEdges))
            for i in self.getAllVertices():
                if self.__dictIn[i] == [] and self.__dictOut[i] == []:
                    output.write("%d \n" %i)
                else:
                    for vertex in self.__dictOut[i]:
                       output.write("%d %d %d\n" % (i, vertex, self.getCostOfEdge((i, vertex))))

            output.close()

