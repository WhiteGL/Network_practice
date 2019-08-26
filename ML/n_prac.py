import numpy as np
import numpy.matlib


a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])

print(np.dot(a, b))

print(np.vdot(a, b))

print(np.inner(np.array([1, 1, 1]), np.array([3, 4, 5])))
print(np.inner(a, b))