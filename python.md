# Python Cheetsheet

### Lists (Arrays):

```python
# Initialization:
arr = [1, 2, 3, 4, 5]

# Length of list:
length = len(arr)

# Iterate through list:
for i in range(length):
    # Process arr[i]

# Alternative iteration:
for val in arr:
    # Process val

# Sorting list:
arr.sort()
```

### Lists (Dynamic Arrays):

```python
# Initialization:
vec = [1, 2, 3, 4, 5]

# Length of list:
length = len(vec)

# Iterate through list:
for i in range(length):
    # Process vec[i]

# Alternative iteration:
for val in vec:
    # Process val

# Sorting list:
vec.sort()
```

### Linked List:

```python
# Node class:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Insertion at the end:
def insert(head, value):
    new_node = ListNode(value)
    if not head:
        head = new_node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node

# Traversal:
temp = head
while temp:
    # Process temp.val
    temp = temp.next
```

### Stacks:

```python
# Using lists as stacks:
stack = []

# Push and pop elements:
stack.append(1)
stack.pop()

# Checking if stack is empty:
is_empty = not stack

# Accessing the top element:
if stack:
    top_element = stack[-1]
```

### Queues:

```python
# Using collections.deque as a queue:
from collections import deque

# Initialization:
queue = deque()

# Enqueue and dequeue:
queue.append(1)
queue.popleft()

# Checking if queue is empty:
is_empty = not queue

# Accessing the front element:
if queue:
    front_element = queue[0]
```

### Dictionaries (Hash Maps):

```python
# Initialization:
my_dict = {1: "One", 2: "Two"}

# Accessing values safely:
value = my_dict.get(1, None)

# Iterating through the dictionary:
for key, value in my_dict.items():
    # Process key and value
```

### Trees:

```python
# Node class:
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Tree traversal (Inorder, Preorder, Postorder):
def inorder(root):
    if root:
        inorder(root.left)
        # Process root.val
        inorder(root.right)

# Searching in a binary search tree:
def search(root, key):
    while root:
        if root.val == key:
            return True
        elif key < root.val:
            root = root.left
        else:
            root = root.right
    return False
```
