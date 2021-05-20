from UI import UI

from graph import DirectedGraph
from undirectedGraph import UndirectedGraph

def main():
    graph = DirectedGraph()
    ugraph = UndirectedGraph()
    ui = UI(graph, ugraph)
    ui.start()


if __name__ == "__main__":
    main()