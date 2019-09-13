import numpy as np


def load_data(path, delimeter):
    data = np.loadtxt(path, delimiter=delimeter)
    print("dimensions:", data.shape)
    print(data[1:6, :])
    return data