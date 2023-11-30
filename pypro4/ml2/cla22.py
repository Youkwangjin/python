# [GaussanNB 문제]
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from xgboost import plot_importance
import matplotlib.pyplot as plt
import xgboost as xgb

df = pd.read_csv('../testdata/mushrooms.csv')
print(df.head(3), df.shape)  # (8124, 23)
print(df.info())

le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])
print(df.head(3))

x = df.drop(columns=['class'])
y = df['class']

print(x[:3])
print(y[:3])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (6499, 22) (1625, 22) (6499,) (1625,)



