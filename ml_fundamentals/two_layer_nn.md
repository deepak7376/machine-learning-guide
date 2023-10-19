**Implementation of Two Layer neural network from scratch**

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

def softmax_loss(y_true, y_pred):
    num_samples = len(y_true)
    y_clip = np.clip(y_pred, 0.0001, 1)
    loss = -np.sum(y_true*np.log(y_clip)) / num_samples
    return loss

def calculate_accuracy(y_true, y_pred):
    predictions = np.argmax(y_pred, axis=1)
    accuracy = np.mean(predictions == y_true)
    return accuracy

class TwoLayerNN:
    def __init__(self, D=6, h_dim=64, num_classes=10):
        self.h_dim = h_dim
        self.num_classes = num_classes
        np.random.seed(45)
        self.W1 = np.random.randn(D, h_dim)
        self.b1 = np.random.randn(h_dim,)

        self.W2 = np.random.randn(h_dim, num_classes)
        self.b2 = np.random.randn(num_classes,)
        self.losses = []
        self.train_acc = []
        self.val_acc = []
        self.train_losses = []
        self.val_losses = []

    def train(self, X_train, y_train, X_val, y_val, epochs, lr=0.0001):

        for epoch in range(1, epochs+1):
            train_loss = 0
            o1 = np.dot(X_train, self.W1) + self.b1
            h1 = relu(o1)
            o2 = np.dot(h1, self.W2) + self.b2
            h2 = relu(o2)

            # calculate softmax
            y_pred = softmax(h2)

            # calculate cross-entropy loss (softmax loss)
            train_loss = softmax_loss(y_train, y_pred)
            self.train_losses.append(train_loss)

            train_accuracy = calculate_accuracy(y_train, y_pred)
            self.train_acc.append(train_accuracy)

            o1_val = np.dot(X_val, self.W1) + self.b1
            h1_val = relu(o1_val)
            o2_val = np.dot(h1_val, self.W2) + self.b2
            h2_val = relu(o2_val)

            y_pred_val = softmax(h2_val)

            val_loss = softmax_loss(y_val, y_pred_val)
            self.val_losses.append(val_loss)

            val_accuracy = calculate_accuracy(y_val, y_pred_val)
            self.val_acc.append(val_accuracy)

            print(f"Epoch: {epoch}, Train Loss: {train_loss:.3f}, Train Accuracy: {train_accuracy:.3f}, Validation Loss: {val_loss:.3f}, Validation Accuracy: {val_accuracy:.3f}")

            # Backpropagation
            dh2 = y_pred - y_train
            # dh2[range(len(y_train)), y_train] -= 1

            do2 = dh2
            db2 = np.sum(do2, axis=0)
            dW2 = np.dot(h1.T, do2)

            dh1 = np.dot(do2, self.W2.T)
            do1 = dh1 * (o1 > 0)  # ReLU derivative
            db1 = np.sum(do1, axis=0)
            dW1 = np.dot(X_train.T, do1)

            # update the weights
            self.W1 = self.W1 - lr * dW1
            self.b1 = self.b1 - lr * db1

            self.W2 = self.W2 - lr * dW2
            self.b2 = self.b2 - lr * db2

        return self.train_losses, self.val_losses, self.train_acc, self.val_acc

```
