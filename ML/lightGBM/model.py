import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

iris = load_iris()
data = iris.data
target = iris.target
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

lgb_train = lgb.Dataset(x_train, y_train)
lgb_eval = lgb.Dataset(x_test, y_test, reference=lgb_train)

params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': {'l2', 'auc'},
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 1
}

print('start training')

gbm = lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval,early_stopping_rounds=5)

print('save model')

gbm.save_model('model.txt')

print('start predicting')

y_pred = gbm.predict(x_test, num_iteration=gbm.best_iteration)

print('rmse is:', mean_squared_error(y_test, y_pred) ** 0.5)