# 다중회귀분석 - 다층 신경망
# 캘리포니아 주택가격 데이터

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

housing = fetch_california_housing()
print(housing.keys())   # 데이터셋의 속성들을 확인
print(housing.data[:3], type(housing.data))     # 입력 특성 데이터 (독립 변수)
print(housing.target[:3], type(housing.target))     # 출력 데이터 (종속 변수)
print(housing.feature_names)    # 입력 특성의 이름들
print(housing.target_names)     # 출력 데이터의 이름

print(housing.data.shape)   # 입력 특성 데이터의 형태를 확인 / (20640, 8)

# train_test_split / 데이터를 훈련 세트, 검증 세트, 테스트 세트로 나누는 함수
x_train_all, x_test, y_train_all, y_test = train_test_split(housing.data, housing.target, random_state=12)
print(x_train_all.shape, x_test.shape, y_train_all.shape, y_test.shape) # (15480, 8) (5160, 8) (15480,) (5160,)
# 전체 데이터를 훈련 세트와 테스트 세트로 나눈 결과를 출력

x_train, x_valid, y_train, y_valid = train_test_split(x_train_all, y_train_all, random_state=12, test_size=0.2)
print(x_train.shape, x_valid.shape, y_train.shape, y_valid.shape)   # (12384, 8) (3096, 8) (12384,) (3096,)
# 훈련 세트 중 20%를 검증 세트로 나눈 결과를 출력

# scale 조정 : 표준화
scaler = StandardScaler()   # 평균이 0이고 표준 편차가 1인 표준 정규 분포로 스케일을 조정하는 스케일러를 생성
x_train = scaler.fit_transform(x_train) # 훈련 세트의 특성 데이터를 표준화
x_valid = scaler.fit_transform(x_valid) # 동일
x_test = scaler.fit_transform(x_test)
print(x_train[:2])

print('Sequential api : 단순한 MLP -------------')
model = Sequential()    # Sequential 모델은 각 레이어를 차례대로 쌓아서 구성하는 간단한 신경망 모델
model.add(Dense(units=32, activation='relu', input_shape=x_train.shape[1:]))    # 입력 데이터의 형태를 지정. 첫 번째 레이어에서만 사용, 입력 특성의 개수에 맞게 설정
model.add(Dense(units=1))   # 출력 레이어를 추가. 하나의 유닛을 가지며, 회귀 문제이므로 활성화 함수를 지정하지 않음

model.compile(optimizer='adam', loss='mse', metrics=['mse'])
history = model.fit(x_train, y_train, epochs=50, validation_data=(x_valid, y_valid), verbose=2)
# validation_data=(x_valid, y_valid): 검증 세트를 사용하여 훈련 중에 모델을 평가
print('evaluate : ', model.evaluate(x_test, y_test, verbose=0)) # 테스트 세트를 사용하여 모델을 평가하고 결과를 출력
x_new = x_test[:3]
y_pred = model.predict(x_new)
print('예측값 : ', y_pred.ravel())
print('실제값 : ', y_test[:3])

# 시각화
# plt.plot(history.history['mse'], c='b', label='mse')
# plt.plot(history.history['val_mse'], c='r', label='val_mse')
# plt.xlabel('epochs')
# plt.ylabel('mse')
# plt.legend()
# plt.show()


print('function api : 복잡하고 유연한 MLP ----------')
from keras.layers import Input
from keras.models import Model

input_ = Input(shape=x_train.shape[1:])
net1 = Dense(units=32, activation='relu')(input_)
net2 = Dense(units=32, activation='relu')(net1)
concat = Concatenate()([input_, net2])  # 입력층과 마지막 은닉층을 연결
output = Dense(units=1)(concat)

model2 = Model(inputs=[input_], outputs=[output])

model2.compile(optimizer='adam', loss='mse', metrics=['mse'])
history = model2.fit(x_train, y_train, epochs=50, validation_data=(x_valid, y_valid), verbose=2)
print('evaluate : ', model2.evaluate(x_test, y_test, verbose=0))
x_new = x_test[:3]
y_pred = model2.predict(x_new)
print('예측값 : ', y_pred.ravel())
print('실제값 : ', y_test[:3])

# plt.plot(history.history['mse'], c='b', label='mse')
# plt.plot(history.history['val_mse'], c='r', label='val_mse')
# plt.xlabel('epochs')
# plt.ylabel('mse')
# plt.legend()
# plt.show()


print('function api : 일부 특성은 짧은 경로로 전달하고, 다른 특성들은 깊은 경로로 전달 ----------')
# 5개 특성(0 ~ 4)은 짧은 경로, 6개 특성(2 ~ 7)은 긴 경로로 전달
input_a = Input(shape=[5], name='wide_input')
input_b = Input(shape=[6], name='deep_input')
net1 = Dense(units=32, activation='relu')(input_b)
net2 = Dense(units=32, activation='relu')(net1)
concat = Concatenate()([input_a, net2])
output = Dense(units=1, name='output')(concat)
model3 = Model(inputs=[input_a, input_b], outputs=[output])

model3.compile(optimizer='adam', loss='mse', metrics=['mse'])

# fit()을 실행할 때 하나의 입력행렬 x_train을 전달하는 것이 아니라
# 입력 마다 하나씩 행렬의 튜플(x_train_a, x_train_b)을 전달행야 한다.
x_train_a, x_train_b = x_train[:, :5], x_train[:, 2:]
x_valid_a, x_valid_b = x_valid[:, :5], x_valid[:, 2:]
x_test_a, x_test_b = x_test[:, :5], x_test[:, 2:]  # evaluate용
x_new_a, x_new_b = x_test_a[:3], x_test_b[:3]  # predict용

history = model3.fit((x_train_a, x_train_b), y_train, epochs=50,
                     validation_data=((x_valid_a, x_valid_b), y_valid), verbose=2)
print('evaluate : ', model3.evaluate((x_test_a, x_test_b), y_test, verbose=0))

y_pred = model3.predict((x_new_a, x_new_b))
print('예측값 : ', y_pred.ravel())
print('실제값 : ', y_test[:3])

plt.plot(history.history['mse'], c='b', label='mse')
plt.plot(history.history['val_mse'], c='r', label='val_mse')
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()





