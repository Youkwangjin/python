# fashion_mnist : mnist와 구조는 같음
import keras.datasets.mnist
import tensorflow as tf
import sys
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
# print(x_train[0])   # 0번째 feature
# print(y_train[0])   # 0번째 label

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankel boot']
print(set(y_train))
plt.imgshow(x_train[0], cmap='gray')
plt.show()
'''
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.xticks(class_names[y_train])
    plt.imshow(x_train[i])
plt.show()
'''

x_train = x_train / 255.0
x_test = x_test / 255.0

# print(x_train[0])

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # 차원축소 : 784로 변환
    keras.layers.Dense(units=128, activation=tf.nn.relu),
    keras.layers.Dense(units=10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
model.fit(x_train, y_train, batch_size=128, epochs=5, verbose=1)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('test loss : ', test_loss)
print('test_acc : ', test_acc)

pred = model.predict(x_test, verbose=0)
print(pred[0])
print('예측값 : ', np.argmax(pred[0]))
print('실제값 : ', y_test[0])

# 실제 레이블과 예측 이미지 비교
def plot_image():
    pass

i = 0
plt.subplot(1, 2, 1)
plot_image()





