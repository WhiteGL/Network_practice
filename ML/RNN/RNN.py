import tensorflow as tf
import numpy as np

cell = tf.nn.rnn_cell.BasicRNNCell(num_units=128)
print(cell.state_size)

inputs = tf.placeholder(np.float, shape=(32, 100))
h0 = cell.zero_state(32, np.float)
output, h1 = cell.__call__(inputs, h0)
print(h1.shape)

