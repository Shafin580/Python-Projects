from Classes.Graph import Graph

nodes = ["A", "B", "C", "D", "E", "F"]

graph = Graph(nodes)

graph.add_edges("A", "B")
graph.add_edges("B", "C")
graph.add_edges("B", "D")
graph.add_edges("C", "E")
graph.add_edges("D", "F")

graph.print_graph()


graph.dfs(nodes.index("B"), nodes.index("E"))






