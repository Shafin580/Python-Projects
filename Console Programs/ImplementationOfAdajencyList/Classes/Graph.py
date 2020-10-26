
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adajency_list = {}

        for node in self.nodes:
            self.adajency_list[node] = []

    def add_edges(self, u, v):
        self.adajency_list[u].append(v)


    def print_graph(self):
        for node in self.nodes:
            print(node, ">-", self.adajency_list[node])
            print(bool(self.adajency_list[node]))

    def degree(self, node):
        return len(self.adajency_list[node])

    def dfs_traversal(self, a, b, explored, path):
        explored[self.nodes.index(a)] = True
        path.append(a)
        if a == b:
            print(path)
        else:
            for node in self.adajency_list[a]:
                if not explored[self.nodes.index(node)]:
                    self.dfs_traversal(node, b, explored, path)
        path.pop()
        explored[self.nodes.index(a)] = False



    def dfs(self, a, b):

        i = 0
        for node in self.nodes:
            i += 1
        explored = [False]*i
        path = []
        self.dfs_traversal(self.nodes[a], self.nodes[b], explored, path)
