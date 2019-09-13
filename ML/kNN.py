import numpy as np
from numpy import *
import operator


def cos_dist(v1, v2):
    return dot(v1, v2)/(linalg.norm(v1) * linalg.norm(v2))


def classify(test_data, train_data, k, label_list):
    print(test_data)
    data_size = train_data.shape[0]
    distances = array(zeros(data_size))
    for index in range(data_size):
        distances[index] = cos_dist(test_data, train_data[index])
    sorted_index = argsort(-distances)
    classCount = {}
    for i in range(k):
        vote_label = label_list[sorted_index[i]]
        classCount[vote_label] = classCount.get(vote_label, 0) + 1
    sorted_class_count = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
label = ['A', 'A', 'B', 'B']
test = [0.2, 0.2]
k = 3
print(classify(test, group, k, label))
