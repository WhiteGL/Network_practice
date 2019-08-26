import numpy as np
import random
from load_data import load_data
from math import exp, pow

data = load_data("./resources/data_for_regression.txt", ",")

data_x = data[:, 0:2]
data_y = data[:, 2]
BATCH_SIZE = 5


class LogisticRegression(object):

    def __init__(self, size):
        self.size = size
        self.weights = [np.random.randn(size, 1)]
        self.biases = [np.random.randn(1, 1)]