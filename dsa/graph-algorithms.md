## Top Graph Algorithms

1. **Adjacency List Implementation:**

```python
class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def __str__(self):
        result = ""
        for node in self.graph:
            result += f"{node}: {', '.join(map(str, self.graph[node]))}\n"
        return result


# Usage:
graph_adj_list = GraphAdjList()
graph_adj_list.add_edge(0, 1)
graph_adj_list.add_edge(0, 2)
graph_adj_list.add_edge(1, 2)
graph_adj_list.add_edge(2, 0)
graph_adj_list.add_edge(2, 3)

print("Adjacency List:")
print(graph_adj_list)
```

2. **Adjacency Matrix Implementation:**

```python
class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  # For undirected graph

    def __str__(self):
        result = ""
        for row in self.graph:
            result += " ".join(map(str, row)) + "\n"
        return result


# Usage:
num_vertices = 4
graph_adj_matrix = GraphAdjMatrix(num_vertices)
graph_adj_matrix.add_edge(0, 1)
graph_adj_matrix.add_edge(0, 2)
graph_adj_matrix.add_edge(1, 2)
graph_adj_matrix.add_edge(2, 3)

print("Adjacency Matrix:")
print(graph_adj_matrix)
```

In the above code, the `GraphAdjList` class represents a graph using an adjacency list, and the `GraphAdjMatrix` class represents a graph using an adjacency matrix. You can add edges to these graph representations and print them to visualize the graph structure. Adjust the number of vertices and edges as needed for your specific graph.
