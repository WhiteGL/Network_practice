import numpy as np
import random as rd

class Network(object):

    def _init_(self, sizes):
        self.layer_numbers = len(sizes)
        self.sizes = sizes

        self.biases = [np.random.randn(y, 1) for y in sizes[:, 1]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

        def feed_forward(self, a):
            for b, w in zip(self.biases, self.weights):
                a = sigmoid(np.dot(w, a) + b)
                return a

        def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
            if test_data: n_test = len(n_test)
            n = len(training_data)
            for j in range(epochs):
                rd.shuffle(training_data)
                mini_batches = [training_data[k:k+mini_batch_size]
                                for k in range(0, n, mini_batch_size)]
                for mini_batch in mini_batches:
                    self.update_mini_batch(mini_batch, eta)
                if test_data:
                    print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
                else:
                    print("Epoch {0}: complete".format(j))
        def update_mini_baich(self, mini_batch, eta):
            