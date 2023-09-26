```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Generate the training dataset
X = np.random.random(size=(1000, 4)) # Four features
W = np.random.random(size=(4, 1))
b = np.random.random(size=(1, ))
y = np.dot(X, W) + b

# Parameters
epochs = 10000
lr = 0.001
N = y.shape[0]
lambda_reg = 0.1

# init weight
np.random.seed(49)
W = 0.001* np.random.random(size=(4, 1))
b = 0.001* np.random.random(size=(1, ))
losses = []

def mse(y_pred, y_true):
  loss = 0.5/N*np.sum((y_pred - y_true)**2)
  return loss

# start the training
for epoch in range(1, epochs+1):
  y_pred = np.dot(X, W) + b

  # calculate the loss
  loss = mse(y_pred, y) + 0.5 * lambda_reg * np.sum(W**2)
  print(f"Epoch: {epoch}, loss: {loss}")

  losses.append(loss)
  # Backpropagation
  dW =  1/N*np.dot(X.T, (y_pred-y)) + lambda_reg * W
  db = 1/N * np.sum((y_pred - y), axis=0)

  # weight update
  W = W - lr*dW
  b = b - lr*db


# visualization
plt.figure(figsize=(8, 6))
plt.scatter(range(epochs), losses, label='Original Data')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('Loss curve')
plt.legend()
plt.grid(True)
plt.show()
```
