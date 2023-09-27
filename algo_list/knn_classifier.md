***k-Nearest Neighbors (k-NN) algorithm***

```python
import numpy as np

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        y_pred = [self._predict(x) for x in X_test]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        
        # Sort by distance and return indices of the first k neighbors
        k_indices = np.argsort(distances)[:self.k]
        
        # Extract the labels of the k nearest neighbor training samples
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Return the most common class label among the k neighbors
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common

# Example usage:
if __name__ == "__main__":
    # Generate the training dataset
    np.random.seed(42)
    threshold = 12
    X_train = np.random.randn(2000, 6)
    
    #We uses y=2x+3 relation to generate the dataset 
    y_train = np.sum(2*X_train + 3, axis=1) > threshold
    print(X_train.shape, y_train.shape)
    X_test = np.random.rand(5, 6)
    
    # Create a k-NN classifier with k=3
    knn = KNNClassifier(k=3)
    knn.fit(X_train, y_train)
    
    # Make predictions on the test data
    predictions = knn.predict(X_test)
    
    print("Test Data:")
    print(X_test)
    print("Predicted Labels:")
    print(predictions)
```

**K-NN drawbacks**
- Computation complexity is very high
- Sensitive to the Choice of k
- Distance Metric Selection: wrong distance matrics leads to poor result
- Storage Requirements: storing training data once for large dataset require more memory

**Important Concept**

The Minkowski distance is a generalization of various distance metrics, including the Euclidean distance and the Manhattan distance. It is defined by the following formula:

For two points \(P\) and \(Q\) in an \(n\)-dimensional space, the Minkowski distance \(D\) between them is calculated as:

\[D(P, Q) = \left(\sum_{i=1}^{n} |p_i - q_i|^p\right)^{\frac{1}{p}}\]

Where:
- \(P = (p_1, p_2, ..., p_n)\) and \(Q = (q_1, q_2, ..., q_n)\) are the coordinates of the two points in the \(n\)-dimensional space.
- \(p\) is a parameter that determines the order of the Minkowski distance:
  - When \(p = 1\), it corresponds to the Manhattan distance (L1 norm).
  - When \(p = 2\), it corresponds to the Euclidean distance (L2 norm).
  - When \(p = \infty\), it corresponds to the Chebyshev distance (maximum absolute difference along any dimension).

The Minkowski distance allows you to control the degree of "sensitivity" to differences in individual dimensions. Smaller values of \(p\) give more weight to larger differences in individual dimensions, whereas larger values of \(p\) make the metric more resistant to differences in individual dimensions.

You can compute the Minkowski distance between two points using this formula with the appropriate value of \(p\) depending on your specific use case and the desired distance metric.
