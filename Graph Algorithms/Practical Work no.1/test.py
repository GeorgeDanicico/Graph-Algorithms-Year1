from graph import DirectedGraph
from unittest import TestCase


class Testing(TestCase):
    def test_graph(self):
        graph = DirectedGraph()
        graph.loadGraph1("graph2.txt")
        graph.deleteVertex(0)
        graph.writeGraph1("graph1.txt")