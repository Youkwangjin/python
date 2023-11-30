# Logistic Linear Regression
# 선형회귀 신뢰구간 ,p값 등이 제공되나 회귀계수의 해석하는 방법이 선형회귀분석과 다르다.
# 독립변수 : 연속형, 종속변수 : 범주형, 이항분포를 따르며 출력값을 0 ~ 1 사이의 확률로 제공됨.
# 연속형 결과를 로직(오즈비에 로그를 씌움)변환 후 시그모이드 함수를 통해 결과를 내 보낸다.

import math
# sigmoid function 경험
def sigmoidFunc(x):
    return 1 / (1 + math.exp(-x))

print(sigmoidFunc(3))
print(sigmoidFunc(1))
print(sigmoidFunc(-2))
print(sigmoidFunc(-5))

print('mtcars dataset을 사용')
import statsmodels.api as sm

mtcarData = sm.datasets.get_rdataset('mtcars')
print(mtcarData.keys())
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))
mtcar = mtcars.loc[:, ['mpg', 'hp', 'am']]
print(mtcar.head(2))
print(mtcar['am'].unique())  # [1 0]

# 연비와 마력수는 변속기에 영향을 주는가?
# 모델 작성 방법 1 : logit()
import statsmodels.formula.api as smf
formula = 'am ~ hp+mpg'
model1 = smf.logit(formula=formula, data=mtcar).fit()
print(model1)
print(model1.summary())


import numpy as np
pred = model1.predict(mtcar[:10])
print('예측값 : ', pred.values)
print('예측값 : ', np.around(pred.values))
print('실제값 : ', mtcar['am'][:10].values)

conf_tab = model1.pred_table()
print('confusion matrix : \n', conf_tab)
print('분류 정확도 : ', (16 + 10) / len(mtcar))                          # 분류 정확도 :  0.8125
print('분류 정확도 : ', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))  # 분류 정확도 :  0.8125
from sklearn.metrics import accuracy_score
pred2 = model1.predict(mtcar)
print('분류 정확도 : ', accuracy_score(mtcar['am'], np.around(pred2)))   # 분류 정확도 :  0.8125

# 모델 작성 방법 2 : glm()
model2 = smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit()
print(model2)
print(model2.summary)
glmPred = model2.predict(mtcar[:10])
print('glm 예측값 : ', np.around(glmPred.values))
print('glm 실제값 : ', mtcar['am'][:10].values)
glmPred2 = model2.predict(mtcar)
print('glm 분류 정확도 : ', accuracy_score(mtcar['am'], np.around(glmPred2)))

