# 회귀분석 문제 3)
# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음)
# Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.  (단순선형회귀는 아니다.)
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf

df = pd.read_csv('../testdata/Carseats.csv')
print(df.head(2))
print(df.info())
df = df.drop([df.columns[6], df.columns[9], df.columns[10]], axis=1)  # 6, 9, 10 열은 제외. (objcet 이기 때문에)
print(df.head(2))
print(df.corr())  # 상관관계 확인
lm = smf.ols(formula='Sales ~ Income + Advertising + Price + Age', data=df).fit()
print('요약 결과: \n', lm.summary())  # p-value : 1.33e-38 < 0.05 이므로 유의한 데이터이다.

df_lm = df.iloc[:, [0, 2, 3, 5, 6]]
print(df_lm)


print('회귀분석모형의 적절성 확인 작업')
# 잔차 구하기
fitted = lm.predict(df_lm)  # 예측값
residual = df_lm['Sales'] - fitted  # 실제값 - 예측값
print(residual[:3])
print('잔차의 평균 :', np.mean(residual))  # -3.028688411177427e-15

print('선형성')
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color': 'red'})
plt.axhline(y=0, linestyle='--', color='blue')  # 가로선 추가
plt.show()

print('정규성')
import scipy.stats as stats
sr = stats.zscore(residual)
(x, y), _ = stats.probplot(sr)
sns.scatterplot(x=x, y=y)
plt.plot([-3, 3], [-3, 3], '--', c='b')
plt.show()  # 잔차항이 정규분포를 따름

print('shapiro test :', stats.shapiro(residual))  # p-value : 0.2127407342195511 > 0.05 이므로 정규성 만족

print('독립성')
# Durbin-Watson : 1.931   2에 근사하므로 독립성 만족

print('등분산성 ')
sr = stats.zscore(residual)
sns.regplot(x=fitted, y=np.sqrt(abs(sr)), lowess=True, line_kws={'color': 'red'})
plt.show()  # 평균선을 기준으로 일정한 패턴을 보이지 않아 등분산성 만족.

print('다중공선성')
from statsmodels.stats.outliers_influence import variance_inflation_factor
df2 = df[['Income', 'Advertising', 'Price', 'Age']]
print(df2.head(2))
print(df2.shape)  # (400, 4)
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(df2.values, i) for i in range(df2.shape[1])]
print(vifdf)  # 모든 변수가 10을 넘기지 않음. 다중공선성 우려 없음.


# 모델 검증이 끝난 경우 모델을 저장
# 방법 1
import pickle
with open('linear6-1.model', 'wb') as obj:
    pickle.dump('linear6-1.model', obj)


# 방법 2 모델 저장 (메모리 절약)
import joblib
joblib.dump(lm, 'yhs.model')  # yhs.model 이름으로 저장

mymodel = joblib.load('yhs.model')
