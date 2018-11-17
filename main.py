from graph import Graph


def main():
    # graph test 1
    graph = {
        'A': {'B': 1, 'D': 3},
        'B': {'C': 3, 'A': 1},
        'C': {'B': 3, 'D': 5, 'E': 2},
        'D': {'A': 3, 'C': 5, 'F': 4},
        'E': {'F': 1, 'C': 2},
        'F': {'D': 4, 'E': 1}
    }

    # graph test 2
    graph = {
        'A': {'B': 1, 'D': 3, 'C': 3},
        'B': {'C': 2, 'A': 1, 'D': 4},
        'C': {'B': 2, 'A': 3, 'E': 5},
        'D': {'A': 3, 'B': 4, 'E': 2},
        'E': {'C': 5, 'D': 2},
    }

    graph = Graph(graph)

    # graph.show_graph()

    graph.prim()

    graph = {
        'GARCA': {'MARILIA': 1, 'GALIA': 4, 'BAURU': 3},
        'MARILIA': {'POMPEIA': 9, 'GARCA': 1},
        'BAURU': {'GARCA': 3, 'CAMPINAS': 3},
        'JAU': {'CAMPINAS': 1, 'GALIA': 5},
        'POMPEIA': {'CAMPINAS': 1, 'MARILIA': 9},
        'GALIA': {'JAU': 5, 'GARCA': 4},
        'CAMPINAS': {'JAU': 1, 'BAURU': 3, 'POMPEIA': 1},
    }

    graph = Graph(graph)

    # graph.show_graph()

    graph.dijkstra()


main()

