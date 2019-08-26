import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def directive_sigmoid(x):
    return np.multiply(1 - sigmoid(x), sigmoid(x))


def cost_function(y_o, y):
    return 1 / (2 * m) * np.sum(np.square(np.subtract(y_o, y)))


m = 10
l_rate = 0.01
X = np.random.rand(m, 2)
Y = np.random.rand(m, 1)

W1 = np.random.rand(2, 3)
Z = np.dot(X, W1)
H = sigmoid(Z)

W2 = np.random.rand(3, 1)
y_hat = np.dot(H, W2)

cost = cost_function(y_hat, Y)
print("start", cost)

cnt = 0
while not cost < 0.1:
    derivative_c_out3 = np.subtract(y_hat, Y) / m
    dw2 = np.dot(H.T, derivative_c_out3)

    derivative_out2_in2 = directive_sigmoid(H)
    derivative_c_in2 = np.multiply(np.dot(derivative_c_out3, W2.T), derivative_out2_in2)
    dw1 = np.dot(X.T, derivative_c_in2)

    W2 = W2 - l_rate * dw2
    W1 = W1 - l_rate * dw1

    Z = np.dot(X, W1)
    H = sigmoid(Z)
    y_hat = np.dot(Z, W2)

    cost = cost_function(y_hat, Y)
    if cnt % 100 == 0:
        print("cost:", cost)
    cnt += 1

print("end", cost)
print("cnt", cnt)