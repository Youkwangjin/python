# 3 way
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers

import numpy as np

# 공부시간에 따른 성적 결과 예측
# x_data = [[1], [2], [3], [4], [5]]
x_data = np.array([1, 2, 3, 4, 5], dtype=np.float32)
y_data = np.array([11, 39, 55, 66, 70], dtype=np.float32)
print(np.corrcoef(x_data, y_data))  # 0.95469145

print('1) Sequential API 사용 : 가장 단순한 방법. 레이어를 순서대로 쌓아 올린 완전 연결층 모델 생성')
model = Sequential()
model.add(Dense(units=2, input_dim=1, activation='relu'))
model.add(Dense(units=1, activation='linear'))
print(model.summary())

opti = optimizers.Adam(learning_rate=0.1)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=2)
loss_metrics = model.evaluate(x=x_data, y=y_data, batch_size=1, verbose=0)
print('loss_metrics : ', loss_metrics)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data)))
print('실제값 : ', y_data)
print('예측값 : ', model.predict(x_data).ravel())

new_data = [1.5, 2.3, 6.8, 8.0]
print('새 예측값 : ', model.predict(new_data).flatten())

import matplotlib.pyplot as plt
plt.plot(x_data.flatten(), model.predict(x_data), 'b', x_data.flatten(), y_data, 'ko')
plt.show()
# mse 의 변화량
plt.plot(history.history['mse'], label='mean squard error')
plt.xlabel('epoch')
plt.show()

print('2) function API 사용 : 유연한 구조로 설계 가능.')
from keras.layers import Input
from keras.models import Model

inputs = Input(shape=(1, ))
# outputs = Dense(units=1, activation='linear')(inputs)  이전 층을 다음 층 함수의 입력으로 사용하도록 함
output1 = Dense(units=2, activation='relu')(inputs)
output2 = Dense(units=1, activation='linear')(output1)

model2 = Model(inputs, output2)
print('새 예측값 : ', model.predict(x_data).ravel())

new_data = [1.5, 2.3, 6.8, 8.0]
print('새 예측값 : ', model2.predict(new_data).flatten())

print('3) sub classing 사용 : 동적인 구조로 설계 가능. 난이도 높은 네트워크 처리 가능')
x_data = np.array([[1.], [2.], [3.], [4.], [5.]], dtype=np.float32)
y_data = np.array([11, 39, 55, 66, 70],dtype=np.float32)

class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(2, activation='linear')
        self.d2 = Dense(1, activation='linear')

    def call(self, x):      # process 담당
        inputs = self.d1(x)
        return self.d2(inputs)

model3 = MyModel()

opti = optimizers.Adam(learning_rate=0.1)
model3.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model3.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=2)
loss_metrics = model3.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('loss_metrics : ', loss_metrics)

print('설명력 : ', r2_score(y_data, model3.predict(x_data)))
print('실제값 : ', y_data)
print('예측값 : ', model3.predict(x_data).ravel())  # ravel or flatten


print('-------------------')
print('3) sub classing 사용2')
from keras.layers import Layer
class Linear(Layer):
    def __init__(self, units=1):
        super(Linear, self).__init__()
        self.units = units

    def build(self, input_shape):
        # 모델의 가중치 관련 작업 기술
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                 initializer='random_normal', trainable=True)   # trainable=True 역전파 수행 여부
        self.b = self.add_weight(shape=(self.units), initializer='zeros', trainable=True)

    def call(self, inputs):
        # 정의된 값들을 이용해 해당층의 로직을 수행
        return tf.matmul(inputs, self.w) + self.b   # wx + b

class MlpModel(Model):
    def __init__(self):
        super(MlpModel, self).__init__()
        self.linear1 = Linear(2)
        self.linear2 = Linear(1)

    def call(self, inputs):
        # Layer의 build를 call
        x = self.linear1(inputs)
        return self.linear2(x)

model4 = MlpModel()

opti = optimizers.Adam(learning_rate=0.1)
model4.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model4.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=2)
loss_metrics = model4.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('loss_metrics : ', loss_metrics)

print('설명력 : ', r2_score(y_data, model4.predict(x_data)))
print('실제값 : ', y_data)
print('예측값 : ', model4.predict(x_data).ravel())
print(model4.summary())
