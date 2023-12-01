# 로직스틱 회귀 분석 소스) 2.x
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam

x_data = [[1, 2], [2, 3], [3, 4], [4, 3], [3, 2], [2, 1]]
y_data = [[0], [0], [0], [1], [1], [1]]

# Sequential Api
model = Sequential()
model.add(Dense(units=1, input_dim=2, activation='sigmoid'))
model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics='accuracy')
print(model.summary())

model.fit(x_data, y_data, epochs=500, batch_size=1, verbose=0)
m_eval = model.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('m_eval : ', m_eval)

# pred
new_data = [[1, 5], [10, 3]]
pred = model.predict(new_data)
print('예측 결과 : ', pred)
print('예측 결과 : ', np.squeeze(np.where(pred > 0.5), 1, 0))
# Model: "sequential"
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 1)                 3
#
# =================================================================
# Total params: 3 (12.00 Byte)
# Trainable params: 3 (12.00 Byte)
# Non-trainable params: 0 (0.00 Byte)
# _________________________________________________________________

print('functional API')
from keras.layers import Input
from keras.models import Model

inputs = Input(shape=(2, ), batch_size=1)
outputs = Dense(units=1, activation='sigmoid')(inputs)
model2 = Model(inputs, outputs)

model2.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics='accuracy')
print(model2.summary())

model2.fit(x_data, y_data, epochs=500, batch_size=1, verbose=0)
m_eval = model2.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('m_eval : ', m_eval)

# pred
new_data = [[1, 5], [10, 3]]
pred = model2.predict(new_data)
print('예측 결과 : ', pred)
print('예측 결과 : ', np.squeeze(np.where(pred > 0.5), 1, 0))
