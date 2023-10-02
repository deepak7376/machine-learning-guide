# ReLU
The derivative of the Rectified Linear Unit (ReLU) activation function depends on the input value.

The ReLU activation function is defined as:

$$
\text{ReLU}(x) = \begin{cases} 
x & \text{if } x > 0 \\
0 & \text{if } x \leq 0 
\end{cases}
$$
```python
def relu(x):
    return np.where(x > 0, x, 0)
```

The derivative of the ReLU function with respect to its input \(x\) is:

$$
\frac{d}{dx}(\text{ReLU}(x)) = \begin{cases} 
1 & \text{if } x > 0 \\
0 & \text{if } x \leq 0 
\end{cases}
$$

```python
def relu_derivative(x):
    return np.where(x > 0, 1, 0)
```

# Softmax Function

Certainly! Here's the derivative of the softmax function with respect to one of the logits, Z_i, in the same Markdown format:

**Softmax Derivative**

The softmax function for class i is defined as:

$$
P_i = \frac{e^{Z_i}}{\sum_{j} e^{Z_j}} \text{ for all } j
$$

To calculate the derivative $$\(\frac{dP_i}{dZ_i}\)$$, you can start by finding the derivative of \(P_i\) with respect to \(Z_i\) using the quotient rule:

$$\frac{dP_i}{dZ_i} = \frac{e^{Z_i} \sum_{j} e^{Z_j} - e^{Z_i} e^{Z_i}}{\left(\sum_{j} e^{Z_j}\right)^2}$$

Simplifying further:

$$
\frac{dP_i}{dZ_i} = \frac{e^{Z_i}}{\sum_{j} e^{Z_j}} \cdot \left(1 - \frac{e^{Z_i}}{\sum_{j} e^{Z_j}}\right)
$$

$$
\frac{dP_i}{dZ_i} = P_i \cdot \left(1 - P_i\right)
$$

# Cross Entropy Loss (Log loss or Softmax loss)

**For Binary Classification (Two Classes):**

The cross-entropy loss for binary classification is defined as:

$$
\text{Cross-Entropy Loss} = -\left( y \log(p) + (1 - y) \log(1 - p) \right)
$$

- \(y\) is the true binary label (0 or 1) for the sample.
- \(p\) is the predicted probability that the sample belongs to class 1.

**For Multiclass Classification (More Than Two Classes):**

The categorical cross-entropy loss for multi-class classification is defined as:

$$
\text{Categorical Cross-Entropy Loss} = -\sum_{i=1}^{N} \sum_{j=1}^{C} y_{ij} \log(p_{ij})
$$

- \(N\) is the number of samples.
- \(C\) is the number of classes.
- \(y_{ij}\) is the ground truth probability that sample \(i\) belongs to class \(j\) (1 if the true class, 0 otherwise).
- \(p_{ij}\) is the predicted probability that sample \(i\) belongs to class \(j\) according to your model.


**Derivative of Binary Cross-Entropy Loss (Log Loss) with Respect to Predicted Probability \(p\):**

$$
\frac{d}{dp}\left(-y \log(p) - (1 - y) \log(1 - p)\right) = -\frac{y}{p} + \frac{1 - y}{1 - p}
$$

**Derivative of Categorical Cross-Entropy Loss with Respect to Predicted Probability \(p_{ij}\):**

$$
\frac{d}{dp_{ij}}\left(-\sum_{i=1}^{N} \sum_{j=1}^{C} y_{ij} \log(p_{ij})\right) = -\frac{y_{ij}}{p_{ij}}
$$

# Derivate (Softmax + Cross Entropy Loss)

Let Z_i be the logit (unnormalized score) for class i, and P_i be the softmax probability for class i. The softmax function is defined as:

P_i = exp(Z_i) / Σ(exp(Z_j)) for all j

The categorical cross-entropy loss is defined as:

L = -Σ(Y_i * log(P_i))

Where Y_i is the true label (1 if class i is the correct class, 0 otherwise).

To find the derivative of this combined loss with respect to Z_i (the logit for class i), you can calculate:

∂L/∂Z_i = P_i - Y_i
