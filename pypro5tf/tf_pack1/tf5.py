# 모델을 만드는 건 분류가 편하다.
# keras 모듈(라이브러리)을 사용하여 네트워크 구성
# 논리회로 분류 모델
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from keras.optimizers import SGD, RMSprop, Adam

# 1. 데이터 수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

# 2. 모델 구성(설정)
# model=Sequential([
#     Dense(input_dim=2,units=1),
#     Activation('sigmoid')
# ])

# 2. 모델구성 방법 2
model = Sequential()
# model.add(Activation('sigmoid'))
# model.add(Dense(units=1, input_dim=2, activation='sigmoid'))  # 위 두줄 합친 것
model.add(units=5, input_dim=2)
model.Add(Activation('relu'))
# model.add(units=1)
# model.Add(Activation('sigmoid'))  # 분류로 빠져나가기 때문에 sigmoid 사용
model.add(Dense(units=5, input_dim=2, activation='relu'))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x, y, epochs=100, batch_size=1, verbose=1)
loss_metrics = model.evaluate(x, y)
print(loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
print('예측 결과 :', pred.flatten())

print(model.summary())

print()
print(model.input)
print(model.output)
print(model.weights)

print()
print(history.history('loss'))
print(history.history('accuracy'))

# 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='train accuracy')
plt.xlabel('epochs')
plt.legend()
plt.show()


pd.DataFrame(history.history)['loss'].plot(figsize=(8, 5))
plt.show()


