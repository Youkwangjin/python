# 다중선형회귀
# network 구성 함수로 작성, 조기 종료


from sklearn.datasets import fetch_california_housing
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Concatenate
from keras import optimizers
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split

datasets = pd.read_csv('../testdata/auto-mpg.csv', na_values='?')
print(datasets.head(2))
print(datasets.columns)

del datasets['car name']
print(datasets.corr())

datasets.drop(['cylinders', 'acceleration', 'model year', 'origin'], axis='columns', inplace=True)
print(datasets.head(2))
print(datasets.isna().sum())
datasets = datasets.dropna()
print(datasets.corr())

import seaborn as sns
# sns.pairplot(datasets[['mpg', 'displacement', 'horsepower', 'weight']], diag_kind='kde')
# plt.show()

# train / test split
train_dataset = datasets.sample(frac=0.7, random_state=123)
test_dataset = datasets.drop(train_dataset.index)
print(train_dataset.shape, test_dataset.shape)  # (274, 4) (118, 4)

# 표준화 : (관찰값 - 평균 ) / 표준편차
train_stat = train_dataset.describe()
print(train_stat)
train_stat.pop('mpg')
print(train_stat[:3])
train_stat = train_stat.transpose()
print(train_stat[:3])

def std_func(x):
    return (x - train_stat['mean']) / train_stat['std']

print(std_func(train_dataset[:3]))

st_train_data = std_func(train_dataset)
st_train_data = st_train_data.drop(['mpg'], axis='columns')

st_test_data = std_func(train_dataset)
st_test_data = st_test_data.drop(['mpg'], axis='columns')

print(st_test_data[:2])
print(st_train_data[:2])

train_label = train_dataset.pop('mpg')
print(train_label[:2])
test_label = test_dataset.pop('mpg')
print(test_label[:2])

print()

def buildModelFunc():
    network = Sequential([
        Dense(units=32, activation='relu', input_shape=[3]),
        Dense(units=32, activation='relu'),
        Dense(units=1, activation='linear'),
    ])
    opti = optimizers.Adam(0.01)
    network = compile(optimize=opti, loss = 'mean_squared_error',
            metrics = ['mean_absolute_error', 'mean_squared_error'])
    return network

model = buildModelFunc()
print(model.summary())

from keras.callbacks import EarlyStopping
epochs = 10000
early_stop = EarlyStopping(monitor='loss', patience=3)
history = model.fit(st_train_data, train_label, batch_size=32,
                    epochs=epochs, validation_split=0.2,
                    verbose=2, callbacks=[early_stop])

df = pd.DataFrame(history.history)
print(df.head(3))
print(df.columns)

loss, mae, mse = model.evaluate(st_test_data, test_label, batch_size=32, verbose=0)
