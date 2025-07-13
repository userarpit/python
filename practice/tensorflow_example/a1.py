import tensorflow as tf

# print(tf.__version__)

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(2.0, tf.float32)

print(type(node1))
node3 = node1 * node2
print(node3)

x = tf.constant([-2, -1, 0, 1, 2, 3], dtype=tf.float32)

print(tf.nn.relu(x))
print(tf.nn.tanh(x))
print(tf.nn.sigmoid(x))
