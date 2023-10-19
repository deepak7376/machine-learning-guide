implementations of Breadth-First Search (BFS) for graph traversal:

### Breadth-First Search (BFS):

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # Process the current node

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

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
print("BFS traversal:")
bfs(graph, start_node)
```

In the BFS code, we use a queue to process nodes in a breadth-first order. We start with the `start_node`, enqueue it, mark it as visited, and then dequeue and process nodes while enqueuing their unvisited neighbors.

Both DFS and BFS are useful algorithms for traversing graphs, and you can adapt these implementations for your specific graph structures and tasks.
