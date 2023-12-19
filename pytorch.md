# Pytorch Cheetsheet

Here's a PyTorch cheat sheet that covers some common operations and concepts:

### Installation:

```bash
pip install torch
```

### Importing PyTorch:

```python
import torch
```

### Tensor Basics:

```python
# Creating Tensors:
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.Tensor([[4, 5, 6], [7, 8, 9]])

# Operations:
result = tensor_a + tensor_b
```

### Automatic Differentiation:

```python
# Tensors with gradient tracking:
x = torch.tensor([1.0], requires_grad=True)
y = x**2
y.backward()

# Accessing gradients:
print(x.grad)
```

### Neural Networks:

```python
import torch.nn as nn

# Define a neural network:
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.output_layer = nn.Linear(128, 10)

    def forward(self, x):
        x = self.fc(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.output_layer(x)
        return x

# Instantiate the model:
model = MyModel()
```

### Loss Function and Optimizer:

```python
# Loss function:
criterion = nn.CrossEntropyLoss()

# Optimizer:
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

### Training the Model:

```python
# Training loop:
for epoch in range(5):
    for inputs, labels in train_data:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

### Saving and Loading Models:

```python
# Save model:
torch.save(model.state_dict(), 'my_model.pth')

# Load model:
model.load_state_dict(torch.load('my_model.pth'))
```

### PyTorch Datasets and DataLoaders:

```python
from torch.utils.data import Dataset, DataLoader

# Custom dataset class:
class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# Creating DataLoader:
train_dataset = MyDataset(train_data, train_labels)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
```

### GPU Acceleration:

```python
# Move model to GPU:
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Move tensors to GPU:
inputs, labels = inputs.to(device), labels.to(device)
```

### TensorBoardX (Visualization):

```python
# Install TensorBoardX:
# pip install tensorboardX

# Import and use:
from tensorboardX import SummaryWriter
writer = SummaryWriter()
writer.add_scalar('loss', loss.item(), global_step=iteration)
```

This cheat sheet provides a quick reference for working with PyTorch. Like TensorFlow, PyTorch is a powerful deep learning library with many features, and this cheat sheet covers only some fundamental aspects. For more detailed information, refer to the official PyTorch documentation: [PyTorch Documentation](https://pytorch.org/docs/stable/index.html).
