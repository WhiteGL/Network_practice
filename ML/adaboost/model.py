#coding=utf-8
import matplotlib as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

digits = datasets.load_digits()
