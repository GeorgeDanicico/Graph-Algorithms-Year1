import random
from graph import DirectedGraph

class UI:
    @staticmethod
    def print_menu():
        print("1. Load the graph")
        print("2. Add Vertex.")
        print("3. Add Edge.")
        print("4. Get the number of edges.")
        print("5. Get the number of vertices.")
        print("6. Get the indegree of a vertex.")
        print("7. Get the outdegree of a vertex.")
        print("8. Get the cost of an edge.")
        print("9. Get all vertices.")
        print("10. Check if a vertex exists.")
        print("11. Check if an edge exists.")
        print("12. Delete a vertex.")
        print("13. Delete an edge.")
        print("14. Modify the cost of an edge.")
        print("15. Get the inbound neighbours of a vertex.")
        print("16. Get the outbound neighbours of a vertex.")
        print("17. Copy the graph.")
        print("18. Write the new graph to the file.")
        print("19. Create a random graph.")
        print("0. Exit.\n")

    def __init__(self, graph):
        self._graph = graph
        self._initialisedGraph = False

    def loadGraphUI(self):
        file_name = input("Enter the file name: ")
        reading_type = int(input("Enter the type of reading(1/2): "))
        if reading_type not in [1, 2]:
            raise ValueError("Invalid input...\n")
        if reading_type == 1:
            self._graph.loadGraph1(file_name)
        else:
            self._graph.loadGraph2(file_name)
        self._initialisedGraph = True
        print("Graph loaded succesfully")

    def addVertexUI(self):
        vertex = input("Enter the vertex:")
        try:
            vertex = int(vertex)
        except ValueError:
            raise ValueError("Invalid vertex.\n")

        self._graph.addVertex(vertex, False)
        print("Vertex added.\n")

    def addEdgeUI(self):
        startPoint = input("Enter the start vertex: ")
        endPoint = input("Enter the end vertex: ")
        cost = input("Enter the cost: ")

        try:
            startPoint = int(startPoint)
            endPoint = int(endPoint)
        except ValueError:
            raise ValueError("Invalid edges.\n")

        self._graph.addEdge(startPoint, endPoint, cost, False)
        print("Edge added.\n")

    def retNrOfEdgesUI(self):
        print(f"The number of edges is: {self._graph.NrOfEdges}\n")

    def retNrOfVerticesUI(self):
        print(f"The number of vertices is: {self._graph.NrOfVertices}\n")

    def getIndegreeVertexUI(self):
        vertex = int(input("Enter the vertex: "))
        print(f"The indegree of the vertex {vertex} is: {self._graph.getIndegreeVertex(vertex)}")

    def getOutdegreeVertexUI(self):
        vertex = int(input("Enter the vertex: "))
        print(f"The outdegree of the vertex {vertex} is: {self._graph.getOutdegreeVertex(vertex)}")

    def getEdgeCost(self):
        startPoint = int(input("Enter the start vertex: "))
        endPoint = int(input("Enter the end vertex: "))
        edge = (startPoint, endPoint)
        print(f"Cost of edge {edge}: {self._graph.getCostOfEdge(edge)}\n")

    def getVerticesUI(self):
        print("The vertices are:\n")
        for i in self._graph.getAllVertices():
            print(i)
        print('\n')

    def findVertexUI(self):
        vertex = int(input("Enter the vertex: "))
        print(f"Existence of edge {vertex}: {self._graph.vertexExistence(vertex)}\n")

    def findEdgeUI(self):
        startPoint = int(input("Enter the start vertex: "))
        endPoint = int(input("Enter the end vertex: "))
        edge = (startPoint, endPoint)
        print(f"Existence of edge {edge}: {self._graph.edgeExistence(edge)}\n")

    def deleteVertexUI(self):
        vertex = int(input("Enter the vertex: "))
        self._graph.deleteVertex(vertex)
        print("Deleted succesfully.\n")

    def deleteEdgeUI(self):
        startPoint = int(input("Enter the start vertex: "))
        endPoint = int(input("Enter the end vertex: "))
        edge = (startPoint, endPoint)
        self._graph.deleteEdge(edge)
        print("Deleted succesfully.\n")

    def changeEdgeCostUI(self):
        startPoint = int(input("Enter the start vertex: "))
        endPoint = int(input("Enter the end vertex: "))
        newCost = int(input("Enter the new cost: "))
        edge = (startPoint, endPoint)
        self._graph.setCostEdge(edge, newCost)
        print("Changed succesfully.\n")

    def getInboundUI(self):
        vertex = int(input("Enter the vertex: "))
        print(f"The inbound neighbours of the vertex {vertex} are: {self._graph.getInboundNeighbours(vertex)}\n")

    def getOutboundUI(self):
        vertex = int(input("Enter the vertex: "))
        print(f"The outbound neighbours of the vertex {vertex} are: {self._graph.getOutboundNeighbours(vertex)}\n")

    def copyGraphUI(self):
        copy_graph = self._graph.getGraphCopy()
        print("Graph copied succesfully.\n")

    def writeToFileUI(self):
        file_name = input("Enter the file name:")
        write_type = int(input("Enter the write type: "))
        if write_type not in [1, 2]:
            raise ValueError("Invalid writing type...\n")
        if write_type == 1:
            self._graph.writeGraph1(file_name)
        else:
            self._graph.writeGraph2(file_name)
        print("Saved succesfully.\n")

    def createRandomGraph(self):
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of vertices: "))
        if edges > vertices * (vertices - 1):
            edges = vertices * (vertices - 1)

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

        print("Graph generated succesfully")
        file_name = input("Enter the file where you want to print the graph: ")
        write_type = int(input("Enter the write type(1/2): "))
        if write_type not in [1, 2]:
            raise ValueError("Invalid writing type...\n")
        if write_type == 1:
            randomGraph.writeGraph1(file_name)
        else:
            randomGraph.writeGraph2(file_name)
        print("Saved succesfully.\n")




    def start(self):

        done = False
        command_dict = {
            "1": self.loadGraphUI,  # implemented
            "2": self.addVertexUI,  # implemented
            "3": self.addEdgeUI,    # implemented
            "4": self.retNrOfEdgesUI,   # implemented
            "5": self.retNrOfVerticesUI,    # implemented
            "6": self.getIndegreeVertexUI,  # implemented
            "7": self.getOutdegreeVertexUI, # implemented
            "8": self.getEdgeCost,  # implemented
            "9": self.getVerticesUI,    # implemented
            "10": self.findVertexUI,    # implemented
            "11": self.findEdgeUI,  # implemented
            "12": self.deleteVertexUI,  # implemented
            "13": self.deleteEdgeUI,    # implemented
            "14": self.changeEdgeCostUI,    # implemented
            "15": self.getInboundUI,    # implemented
            "16": self.getOutboundUI,   # implemented
            "17": self.copyGraphUI,     # implemented
            "18": self.writeToFileUI,   # implemented
            "19": self.createRandomGraph
        }
        while not done:
            UI.print_menu()
            command = input("Command>>")
            try:
                if command in command_dict:
                    if command != '1' and self._initialisedGraph is False and command != '19':
                        raise ValueError("You didnt load any graph!")
                    command_dict[command]()
                elif command == '0':
                    print("Exiting...")
                    break
                else:
                    print("Unknown command.\n")
            except ValueError as ve:
                print(str(ve) + "\n")
            except Exception as ve:
                print(str(ve) + "\n")

