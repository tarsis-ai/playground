class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[node]
