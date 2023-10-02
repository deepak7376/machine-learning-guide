**Logistic Regression Implementation**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate a simple classification training dataset
np.random.seed(42)
threshold = 0.62
W = np.random.randn(4,1)
b = np.random.randn(1,)

X = np.random.randn(1000, 4)
y = 1/(1+np.exp(-np.dot(X, W) + b)) > threshold

# Implement Logistic Regression

def sigmoid(x):
  return 1/ (1+np.exp(-x))


def binary_cross_entropy_loss(y_pred, y_true):
  return -1/N * np.sum(y_true * np.log(y_pred) + (1-y_true)*np.log(1-y_pred))


epochs = 1000
lr = 0.001
N = X.shape[0]

# initialize the weight
np.random.seed(43)
W = np.random.randn(4,1)
b = np.random.randn(1,)
losses = []

for epoch in range(1, epochs+1):
  temp = np.dot(X, W) + b
  y_pred = sigmoid(temp)
  loss = binary_cross_entropy_loss(y_pred, y)
  losses.append(loss)

  # backpropagation
  # (-y/p + (1-y)/(1-p))

  dW = np.dot(X.T, (-1*y/y_pred + (1-y)/(1-y_pred))*y_pred*(1-y_pred))
  db = np.sum((-1*y/y_pred + (1-y)/(1-y_pred))*y_pred*(1-y_pred), axis=0, keepdims=True)

  W = W - lr*dW
  b = b - lr*db

  print(f"Epoch: {epoch}, loss: {loss:.3f}")

# visua;ization
plt.figure(figsize=(8, 6))
plt.scatter(range(epochs), losses, label='Original Data')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('Loss curve')
plt.legend()
plt.grid(True)
plt.show()


