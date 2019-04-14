import numpy as np
from math import pow
import random
BATCH_SIZE = 1
L_Rate = 0.01

train_data = np.random.randn(100, 2)
test_data = train_data


class LP(object):
    def __init__(self):
        self.weights = np.random.rand(1)
        self.biases = np.random.rand(1)

    def predict(self, x):
        w = self.weights
        b = self.biases
        return w*x + b

    def loss(self, data):
        n = len(data)
        loss_ = 0
        w = self.weights
        b = self.biases
        for sample in data:
            loss_ += pow(sample[0] * w + b - sample[1], 2)
        return loss_ / n

    def SGD(self, train_data, eta, epochs, batch_size):
        n = len(train_data)
        for j in range(epochs):
            random.shuffle(train_data)
            batches = [train_data[k:k+batch_size] for k in range(0, n, batch_size)]
            for mini_batch in batches:
                self.update_variables(mini_batch, eta)
            print(self.weights, self.biases)

    def update_variables(self, mini_batch, eta):
        nabla_w = np.zeros(1)
        nabla_b = np.zeros(1)
        w = self.weights
        b = self.biases
        for x, y in mini_batch:
            nabla_w += 2 * (w*x+b-y) * w
            nabla_b += 2 * (w*x+b-y)
        self.weights = w - eta*nabla_w
        self.biases = b - eta*nabla_b


lp = LP()
lp.SGD(train_data, L_Rate, 3, BATCH_SIZE)