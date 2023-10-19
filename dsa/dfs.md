### Depth-First Search (DFS):

```python
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')  # Process the current node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
visited = set()  # Create an empty set to keep track of visited nodes
print("DFS traversal:")
dfs(graph, start_node, visited)
```

In this code, the `dfs` function recursively explores the graph using depth-first search. It starts at the `start_node`, marks it as visited, processes it, and then recursively explores its unvisited neighbors.
