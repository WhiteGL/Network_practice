from sklearn import datasets
from sklearn.decomposition import PCA
import seaborn as sns

# 引入iris数据集
iris = datasets.load_iris()
model = PCA(n_components=2)
model.fit(iris.data)
x_2d = model.transform(iris.data)

iris['PCA1'] = x_2d[:, 0]
iris['PCA2'] = x_2d[:, 1]
sns.lmplot("PCA1", "PCA2", data=iris, hue='target', fit_reg=False)