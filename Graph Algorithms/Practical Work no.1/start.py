from UI import UI

from graph import DirectedGraph


def main():
    graph = DirectedGraph()
    ui = UI(graph)
    ui.start()


if __name__ == "__main__":
    main()