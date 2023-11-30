# SVM : 데이터 분류 및 예측을 위한 가장 큰 폭의 경계선을 찾는 알고리즘 사용
# 커널트릭 이라는 기술을 통해 선형은 물론 비선형, 이미지 분류 까지도 처리 가능

# SVM으로 XOr 처리를 실습

x_data = [
    [0, 0, 0],   # OR 연산
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],

]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

df = pd.DataFrame(x_data)
print(df)

feature = np.array(df.iloc[:, 0:2])  # 0열 1열
label = np.array(df.iloc[:, 2])
print(feature)  # 2차원
print(label)    # 1차원

model1 = LogisticRegression().fit(feature, label)
pred = model1.predict(feature)
print('Logistic 예측값 : ', pred)
print('Logistic acc : ', metrics.accuracy_score(label, pred))  # 실제값, 예측값 순서 바뀌면 안된다.

print()

model2 = svm.SVC(C=1.0).fit(feature, label)  # 과적합(Overfitting) 방지
# model2 = svm.LinearSVC().fit(feature, label)
pred2 = model2.predict(feature)
print('svm 예측값 : ', pred2)
print('svm acc : ', metrics.accuracy_score(label, pred))  # 실제값, 예측값 순서 바뀌면 안된다.

