from collections import deque

class UndirectedGraph:
    def init(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def remove_vertex(self, v):
        if v in self.graph:
            # Remove vertex v from all adjacency lists
            for vertex in self.graph[v]:
                self.graph[vertex].remove(v)
            del self.graph[v]

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)
            if u in self.graph[v]:
                self.graph[v].remove(u)

    def is_adjacent(self, u, v):
        return v in self.graph.get(u, [])

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage
ug = UndirectedGraph()
ug.add_vertex('A')
ug.add_vertex('B')
ug.add_vertex('C')
ug.add_edge('A', 'B')
ug.add_edge('A', 'C')
ug.add_edge('B', 'C')

ug.display()
print("\nUndirected Graph:")
ug.remove_vertex('A')
ug.display()