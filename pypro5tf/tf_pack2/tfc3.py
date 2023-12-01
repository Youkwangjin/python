# red & white dataset으로 이항분류 모델

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

wdf = pd.read_csv("../testdata/wine.csv", header=None)
print(wdf.head(2))
print(wdf.info())
print(wdf.iloc[:, 12].unique())  # [1 0]
print(len(wdf[wdf.iloc[:, 12] == 0]))  # 4898 red
print(len(wdf[wdf.iloc[:, 12] == 1]))  # 1599 white

datasets = wdf.values
x = datasets[:, 0:12]
y = datasets[:, -1]
print(x[0])
print(y[0])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = Sequential()
model.add(Dense(32, input_dim=12, activation='relu'))  # input_shape=(12,)
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 32)                416
#
#  dense_1 (Dense)             (None, 16)                528
#
#  dense_2 (Dense)             (None, 8)                 136
#
#  dense_3 (Dense)             (None, 1)                 9
#
# =================================================================

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
loss, acc = model.evaluate(x=x_train, y=y_train, verbose=2)
print('훈련안한 모델 정확도:{:5.2f}%'.format(acc * 100))

import os
MODEL_DIR = 'model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

fname = 'tf3.hdf5'
chkpoint = ModelCheckpoint(MODEL_DIR + fname, monitor='val_loss', verbose=0, save_best_only=True)
early_stop = EarlyStopping(monitor='loss', mode='auto')
history = model.fit(x=x_train, y=y_train, epochs=1000, batch_size=64,
                    validation_split=0.3, callbacks=[early_stop, chkpoint])

loss, acc = model.evaluate(x=x_test, y=y_test, verbose=2)
print('훈련한 모델 정확도:{:5.2f}%'.format(acc * 100))

# 시각화
epoch_len = np.arange(len(history.epoch))

plt.plot(epoch_len, history.history['accuracy'], c='red', label='accuracy')
plt.plot(epoch_len, history.history['val_accuracy'], c='blue', label='val_accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()

print('-----------------------------------------------')
# 가장 우수한 모델로 저장된 파일을 읽어 분류 예측
from keras.models import load_model
mymodel = load_model(MODEL_DIR + fname)
new_data = x_test[:5, :]
pred = mymodel.predict(new_data)
print('pred : ', np.where(pred > 0.5, 1, 0).flatten())


# softmax 
