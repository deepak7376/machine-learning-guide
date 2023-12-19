# C/C++ Cheetsheet

### Arrays:

```cpp
// Initialization:
int arr[] = {1, 2, 3, 4, 5};

// Size of array:
int size = sizeof(arr) / sizeof(arr[0]);

// Iterate through array:
for (int i = 0; i < size; ++i) {
    // Process arr[i]
}

// Range-based loop:
for (int val : arr) {
    // Process val
}

// Sorting array:
#include <algorithm>
std::sort(arr, arr + size);
```

### Vectors (Dynamic Arrays):

```cpp
// Initialization:
std::vector<int> vec = {1, 2, 3, 4, 5};

// Size of vector:
int size = vec.size();

// Iterate through vector:
for (int i = 0; i < size; ++i) {
    // Process vec[i]
}

// Range-based loop:
for (int val : vec) {
    // Process val
}

// Sorting vector:
#include <algorithm>
std::sort(vec.begin(), vec.end());
```

### Linked List:

```cpp
// Insertion at the end:
void insert(ListNode*& head, int value) {
    ListNode* newNode = new ListNode(value);
    if (!head) {
        head = newNode;
    } else {
        ListNode* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Deletion of a node:
void deleteNode(ListNode*& head, int value) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* prev = dummy;
    ListNode* curr = head;
    while (curr) {
        if (curr->val == value) {
            prev->next = curr->next;
            delete curr;
            break;
        }
        prev = curr;
        curr = curr->next;
    }
    head = dummy->next;
    delete dummy;
}
```

### Stacks:

```cpp
// Checking if stack is empty:
bool isEmpty = st.empty();

// Accessing the top element:
if (!isEmpty) {
    int topElement = st.top();
}

// Iterating through the stack:
while (!st.empty()) {
    // Process st.top()
    st.pop();
}
```

### Queues:

```cpp
// Checking if queue is empty:
bool isEmpty = q.empty();

// Accessing the front element:
if (!isEmpty) {
    int frontElement = q.front();
}

// Iterating through the queue:
while (!q.empty()) {
    // Process q.front()
    q.pop();
}
```

### Hash Maps:

```cpp
// Accessing values safely:
if (myMap.find(1) != myMap.end()) {
    std::string value = myMap[1];
}

// Iterating through the map:
for (const auto& entry : myMap) {
    int key = entry.first;
    std::string value = entry.second;
}
```

### Trees:

```cpp
// Tree traversal (Inorder, Preorder, Postorder):
void inorder(TreeNode* root) {
    if (root) {
        inorder(root->left);
        // Process root->val
        inorder(root->right);
    }
}

// Searching in a binary search tree:
bool search(TreeNode* root, int key) {
    while (root) {
        if (root->val == key) return true;
        else if (key < root->val) root = root->left;
        else root = root->right;
    }
    return false;
}
```
