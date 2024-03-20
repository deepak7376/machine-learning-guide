# Tree Traversal Algorithms

## Traversal Algo

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is None:
        return []
    result = []
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def preorder_traversal(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

def postorder_traversal(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return result[::-1]  # Reverse the result to get postorder traversal
```

## Search Algo

```python

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root, target):
    if root is None:
        return False
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val == target:
            return True
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return False

def bfs(root, target):
    if root is None:
        return False
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

```

Recursive

```python

def dfs_recursive(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return dfs(root.left, target) or dfs(root.right, target)

def bfs_recursive(queue, target):
    if not queue:
        return False

    current = queue.pop(0)
    if current.val == target:
        return True

    if current.left:
        queue.append(current.left)
    if current.right:
        queue.append(current.right)

    return bfs_recursive(queue, target)

def bfs(root, target):
    if root is None:
        return False
    return bfs_recursive([root], target)

```


