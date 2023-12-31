# tf.constant() : tensor를 직접 기억
# tf.Variable() : tensor가 저장된 주소를 참조
import tensorflow as tf
import numpy as np

node1 = tf.constant(3, dtype=tf.float32)
node2 = tf.constant(4.0)
print(node1)
print(node2)

imsi = tf.add(node1, node2)
print(imsi)

print()
node3 = tf.Variable(3, dtype=tf.float32)
node4 = tf.Variable(4.0)
print(node3)
print(node4)
node4.assign_add(node3)
print(node4)

print()
a = tf.constant(5)
b = tf.constant(10)
c = tf.multiply(a, b)
result = tf.cond(a < b, lambda : tf.add(10, c), lambda : tf.square(a))
print('result : ', result.numpy())

print('---')
v = tf.Variable(1)

@tf.function  # Graph 환경에서 처리가 된다.
def find_next_func():
    v.assign(v + 1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)

find_next_func()
print(v.numpy())
print(type(find_next_func))  # <class 'function'>

print('func1 --------------------------------')
def func1():
    imsi = tf.constant(0)
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)

    return imsi

kbs = func1()
print(kbs.numpy(), ' ', np.array(kbs))  # 3   3


print('func2 --------------------------------')
@tf.function
def func2():
    # imsi = tf.constant(0)
    global imsi
    su = 1
    for _ in range(3):
        # imsi = tf.add(imsi, su)
        # imsi = imsi + su
        imsi += su
    return imsi

kbs = func2()
print(kbs.numpy(), ' ', np.array(kbs))


print('func3 --------------------------------')
imsi = tf.Variable(0)
@tf.function
def func3():
    # imsi = tf.Variable(0)  # autograp에서는 Variable()은 함수 밖에서 선언
    su = 1
    for _ in range(3):
        imsi.assign_add(su)
    return imsi

kbs = func3()
print(kbs.numpy(), ' ', np.array(kbs))  # 3   3

print('구구단 출력 --------------------------------')
@tf.function
def gugu1(dan):
    su = 0
    for _ in range(9):
        su = tf.add(su, 1)
        # print(su) Good
        # print(su.numpy()) No Good
        print('{} * {} = {}'.format(dan, su, dan * su))
gugu1(3)

print('---------------------------')
# 내장함수 : 일반적으로 numpy 지원함수를 그대로 사용.  + 알파
# ... 중 reduce ~ 함수
ar = [[1., 2.], [3., 4.]]
print(tf.reduce_sum(ar).numpy())  # 10
print(tf.reduce_mean(ar, axis=0).numpy())
print(tf.reduce_mean(ar, axis=1).numpy())

# one_hot
print(tf.one_hot([0, 1]))
