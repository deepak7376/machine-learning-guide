# Tensorflow Cheetsheet

Here's a TensorFlow cheat sheet that covers some common operations and concepts:

### Installation:

```bash
pip install tensorflow
```

### Importing TensorFlow:

```python
import tensorflow as tf
```

### Tensor Basics:

```python
# Creating Tensors:
tensor_a = tf.constant([1, 2, 3])
tensor_b = tf.Variable([4, 5, 6])

# Operations:
result = tensor_a + tensor_b
```

### Sessions:

```python
# Creating a Session:
with tf.Session() as sess:
    result_value = sess.run(result)
    print(result_value)
```

### TensorFlow 2.x:

```python
# Eager Execution (default in TF 2.x):
tf.config.run_functions_eagerly(True)

# No need for sessions:
result_value = result.numpy()
print(result_value)
```

### Placeholders (For TensorFlow 1.x):

```python
# Placeholder (for feeding data in sessions):
x = tf.placeholder(tf.float32, shape=(None, 784))
```

### Neural Networks:

```python
# Sequential model:
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model:
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training the model:
model.fit(train_data, train_labels, epochs=5)
```

### Saving and Loading Models:

```python
# Save model:
model.save('my_model.h5')

# Load model:
loaded_model = tf.keras.models.load_model('my_model.h5')
```

### TensorFlow Datasets:

```python
# Loading a dataset:
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocessing data:
train_images = train_images / 255.0
test_images = test_images / 255.0
```

### Custom Layers:

```python
# Creating a custom layer:
class MyLayer(tf.keras.layers.Layer):
    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(MyLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                      shape=(input_shape[1], self.output_dim),
                                      initializer='uniform',
                                      trainable=True)
        super(MyLayer, self).build(input_shape)

    def call(self, x):
        return tf.matmul(x, self.kernel)

# Using the custom layer:
model.add(MyLayer(64))
```

### TensorBoard:

```python
# Using TensorBoard:
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
model.fit(train_data, train_labels, epochs=5, callbacks=[tensorboard_callback])
```

This cheat sheet provides a quick reference for working with TensorFlow. Remember that TensorFlow's capabilities are extensive, and this cheat sheet covers only some fundamental aspects. For more detailed information, refer to the official TensorFlow documentation: [TensorFlow Documentation](https://www.tensorflow.org/api_docs/python).
