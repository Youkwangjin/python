# 체질량지수는 자신의 몸무게(kg)를 키의 제곱(m)으로 나눈 값입니다.
# 예) 키 : 175, 몸무게 : 68        68 / ((170/ 100))
print(68 / ((170 / 100) * (170 / 100)))  # 23.529411764705884

'''
# 다량의 데이터를 생산하기
import random
random.seed(12)

def calcBMI_Func(h, w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5:return 'thin'
    if bmi < 25.0:return 'normal'
    return 'fat'

print(calcBMI_Func(172, 68))

ff = open('bmi.csv', 'w')
ff.write('height,weight,label\n')  # csv파일 만들기
cnt = {'thin':0,'normal':1, 'fat':2}

for i in range(50000):
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calcBMI_Func(h, w)
    cnt[label] += 1
    ff.write('{0},{1},{2}\n'.format(h, w, label))

ff.close()
'''

# SVM으로 분류모델

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('bmi.csv')
print(df.head(3), df.shape)  # (500000, 3)
print(df.info())

label = df['label']
print(label[:3])

w = df['weight'] / 100  # 정규화 작업
print(w[:3].values)
h = df['height'] / 200  # 정규화 작업
print(h[:3].values)


wh = pd.concat([w, h], axis=1)
print(wh.head(3), wh.shape)


# 데이터 50만개 짜르는 작업
x_train, x_test, y_train, y_test = train_test_split(wh, label, test_size=0.3, random_state=1)  # test_size=0.3 은 7:3으로 짜르기
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (350000, 2) (150000, 2) (350000,) (150000,)
model = svm.SVC(C=0.01).fit(x_train, y_train)
print(model)

pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10].values)

ac_score = metrics.accuracy_score(y_test, pred)
print('분류 정확도 : ', ac_score)

from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, wh, label, cv=3)
print('각각의 검증 정확도 : ', cross_vali)
print('평균 검증 정확도 : ', cross_vali.mean())

print()

# 시각화
df2 = pd.read_csv('bmi.csv', index_col=2)
print(df2.head(3))

def scatterFunc(lbl, color):
    b = df2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label=lbl)

scatterFunc('fat', 'red')
scatterFunc('normal', 'yellow')
scatterFunc('thin', 'blue')
plt.legend()
plt.show()

# 새로운 값으로 분류 예측
newdata = pd.DataFrame({'weight': [69, 59, 99], 'height': [170, 180, 160]})
print(newdata)
newdata['weight'] = newdata['weight'] / 100
newdata['weight'] = newdata['height'] / 200
print(newdata)  # 학습할 때 정규화를 했기 때문에 정규화 작업 반드시 해야된다.

newPred = model.predict(newdata)
print('새로운 예측 결과 : ', newPred)

