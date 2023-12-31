
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np

model = Sequential()  # 계층구조(Linear layer stack)를 이루는 모델을 정의
model.add(Dense(1, input_dim=1, activation='linear'))

x_data = [1., 2., 3., 4., 5.]
y_data = [1.2, 2.0, 3.0, 3.5, 5.5]


# activation function의 종류 : https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras/activations
sgd = optimizers.SGD(lr=0.01)  # 학습률(learning rate, lr)은 0.01
model.add(Dense(units=1,input_dim=1, activation='linear'))
model.compile(optimizer=sgd, loss='mse', metrics=['mse'])
model.fit(x_data, y_data, batch_size=1, epochs=100, verbose=1)
print(model.evaluate(x_data))

pred = model.predict(x_data)
print('pred : ', pred.flatten())

import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'ro')
plt.plot(x_data, pred, 'b')
plt.show()

# 결정계수
from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, pred))

# 새로운 값으로 예측
new_x = [1.5, 2.5, 3.3]
print('새로운 값 예측 결과 : ', model.predict(new_x).flatten())


# 옵티마이저는 경사하강법의 일종인 확률적 경사 하강법 sgd를 사용.
# 손실 함수(Loss function)은 평균제곱오차 mse를 사용.
# 주어진 X와 y데이터에 대해서 오차를 최소화하는 작업을 100번 시도.

model.fit(x_data, y_data, batch_size=1, epochs=100, shuffle=False, verbose=2)
from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data)))
print('예상 수 : ', model.predict([5]))  # [[4.801656]]
print('예상 수 : ', model.predict([2.5]))  # [[2.490468]]
print('예상 수 : ', model.predict([1.5, 3.3]))  # [[1.565993][3.230048]]
