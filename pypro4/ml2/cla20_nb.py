# Naive Bayes Classifier : weather dataset 사용 - 비가 오는지 여부 분류

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# 자료 읽기
df = pd.read_csv("../testdata/weather.csv")
print(df.head(3), df.shape)  # (366, 12)
print(df.columns)


feature = df[['MinTemp', 'MaxTemp', 'Rainfall']]
# label = df['RainTomorrow'].apply(lambda x:1 if x == 'Yes' else 0)
# print(label[:10])
label = df['RainTomorrow'].map({'Yes': 1, 'No': 0})
print(label[:10].values)

# train/test

train_x, test_x, train_y, test_y = train_test_split(feature, label, random_state=0, test_size=0.3)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)  # (256, 3) (110, 3) (256,) (110,)

# model
gmodel = GaussianNB()
print(gmodel)
gmodel.fit(train_x, train_y)

pred = gmodel.predict(test_x)
print('예측값 : ', pred[:10])
print('실제값 : ', test_y[:10].values)

acc = sum(test_y == pred) / len(pred)
print('정확도 : ', acc)
print('정확도 : ', accuracy_score(test_y, pred))
print('분류 보고서 : \n', classification_report(test_y, pred))
# 분류 보고서 :
#                precision    recall  f1-score   support
#
#            0       0.81      0.92      0.86        90
#            1       0.12      0.05      0.07        20
#
#     accuracy                           0.76       110
#    macro avg       0.47      0.49      0.47       110
# weighted avg       0.69      0.76      0.72       110

print('새 값으로 예측')
import numpy as np
myWeather = np.array([[2, 12, 0], [22, 34, 50], [1, 2, 3]])
print('예측 결과 : ', gmodel.predict(myWeather))  # 예측 결과 :  [0 1 0]

# GaussianNB : 연속형 데이터
# BernouNB : 연속형 데이터
# MultinomialNB : 텍스트 분류(카운트 데이터)


