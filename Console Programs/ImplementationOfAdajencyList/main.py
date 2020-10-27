from Classes.Graph import Graph

nodes = ["A", "B", "C", "D", "E", "F"]

graph = Graph(nodes)

graph.add_edges("A", "B")
graph.add_edges("A", "C")
graph.add_edges("B", "C")
graph.add_edges("B", "D")
graph.add_edges("C", "E")
graph.add_edges("D", "F")
graph.add_edges("E", "D")

print("Adajency List:")
graph.print_graph()
#graph.degree()
source_node = input("Enter source node: ")
goal_node = input("Enter goal node: ")
print("The path from", source_node.upper(), "to", goal_node.upper(), "is: ")
graph.dfs(nodes.index(source_node.upper()), nodes.index(goal_node.upper()))






