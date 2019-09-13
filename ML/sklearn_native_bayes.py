from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score


# 引入iris数据集
iris = datasets.load_iris()
# 训练集划分函数train_test_split在高版本sklearn中被放入model_selection库中
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=1)
# 使用朴素贝叶斯模型
model = GaussianNB()
model.fit(x_train, y_train)
y_model = model.predict(x_test)
print(accuracy_score(y_model, y_test))