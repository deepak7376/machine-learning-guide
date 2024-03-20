## Tree Traversal Algorithms

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
