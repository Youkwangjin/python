# 광고비에 따른 판매량(액) 데이터로 선형회귀분석모델 작성
# *** 선형회귀분석의 기존 가정 충족 조건 ***
# . 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
# . 정규성 : 잔차항(오차항)이 정규분포를 따라야 한다.
# . 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
# . 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
# . 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.

import pandas as pd
import matplotlib.pyplot as plt
from django.conf.locale import pl
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np

advdf = pd.read_csv("../testdata/Advertising.csv", usecols=[1,2,3,4])
print(advdf.head(3), advdf.shape)       # (200, 4)
print(advdf.info())

print('r: \n', advdf.loc[:,['sales', 'tv']].corr())     # 0.782224
# 인과관계가 있다는 가정하에 회귀분석 모델 작성

lm = smf.ols(formula='sales ~ tv', data=advdf).fit()
# lm.fit()
print(lm.summary())
print(lm.params)
print(lm.pvalues[1])
print(lm.rsquared)

# 시각화
# plt.scatter(advdf.tv, advdf.sales)
# plt.xlabel('tv')
# plt.ylabel('sales')
# y_pred = lm.predict(advdf.tv)
# plt.plot(advdf.tv, y_pred, c='r')
# plt.show()

# 모델 검정
pred = lm.predict(advdf[:10])
print('실제값 : ', advdf.sales[:10].values)
print('예측값: ', pred[:10].values)
# 예측1 : 새로운 tv 값으로 sales을 추정
x_new = pd.DataFrame({'tv':[200.0, 40.5, 100.0]})
new_pred = lm.predict(x_new)
print('sales 추정값 : ', new_pred.values)      # [16.53992164  8.95782749 11.78625759]


print('~~~~~~~~~~~~~~~' * 50)
# 다중선형회귀모델
print('r : \n', advdf.corr())
lm_mul = smf.ols(formula='sales ~ tv+radio', data=advdf).fit()
print(lm_mul.summary())     # Prob (F-statistic): 4.83e-98 < 0.05, Adj.     R-squared:0.897

# 예측2 : 새로운 tv, radio 값으로 sales을 추정
x_new2 = pd.DataFrame({'tv':[200.0, 40.5, 100.0], 'radio':[37.8, 45.3, 55.0]})
new_pred2 = lm_mul.predict(x_new2)
print('sales 추정값 : ', new_pred2.values)      # [19.1782447  13.29030839 17.83626389]


print('잔차항 구하기')
fitted = lm_mul.predict(advdf.iloc[:, 0:2])
# print(fitted)
residual = advdf['sales'] - fitted  # 잔차
# print('residual : ', residual, sum(residual))       # 2.312816604899126e-12

# . 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다. 예측값과 잔차가 비슷하게 유지
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})    # lowess=True : 비모수적 최적모델 추정(로컬 가중 선형회귀)
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color='blue')
# .show()  # 예측값과 잔차가 곡선을 그림 - 선형성을 만족하지 못함. 다항회귀(PolynomialFeatures)분석모델을 추천

# . 정규성 : 잔차항(오차항)이 정규분포를 따라야 한다. Q_Q plot을 사용
import scipy.stats
ssz = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(ssz)
sns.scatterplot(x=x, y=y)
plt.plot([-3,3],[-3,3], '--', color='blue')
# plt.show()  # 커브를 그리면서 추세선 밖으로 나가고 있는 형태이므로 정규성 만족 못함
print('정규성 : ', scipy.stats.shapiro(residual))  # pvalue=4.190036317908152e-09 < 0.05

# log를 취하는 방법등을 사용하여 좀 더 데이터 가공이 필요하다.

# 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다. 잔차가 자기상관(인접 관측자와 독립이어야 함)이 있는지 확인 필요
# 자기상관은 Durbin-Watson 지수 d 를 이용하여 검정한다.
# d 값은 0 ~ 4 사이에 나오며 2에 가까울수록 자기 상관이 없이 독립이며, 독립일 경우 회귀분석을 사용할 수 있다.
# DW 값이 0 또는 4에 근사하면 잔차들이 자기상관에 있고, 계수(t, f, r제곱) 값을 증가시켜 유의하지 않은 결과를 유의한 결과로 왜곡시킬 수 있다.

# Durbin-Watson: 2.081
print('Durbin-Watson : ', 2.081)

# 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
# 분산은 모든 잔차에 대해 동일해야 한다. 잔차(y축) 및 예상 값(x축)의 산점도를 사용하여 이 가정을 테스트할 수 있다.
# 결과 산점도는 플롯에서 임의로 플롯된 점의 수평 밴드로 나타나야 한다.
sns.regplot(x=fitted, y=np.sqrt(np.abs(ssz)), lowess=True, line_kws={'color': 'red'})
# plt.show()  # 적색 실선이 수평선을 그리지 않으므로 등분산성 만족 못함. 이상값, 비선형 여부 확인. 가중회귀분석을 고려!


# 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.
# VIF(Variance Inflation Factor, 분산 팽창 지수)
# VIF는 예측변수들이 상관성이 있을 때 추정 회계 계수의 산포 크기를 측정하는 것이며,
# 산포가 커질수록 회귀 모형은 신뢰할 수 없게 됩니다.
# VIF 값이 1 근방에 있으면 다중공선성이 없어 모형을 신뢰할 수 있으며
# 만약 VIF 값이 10 이상이 되면 매우 높은 다중공선성이 있다.

from statsmodels.stats.outliers_influence import variance_inflation_factor
# lm_mul = smf.ols(formula='sales ~ tv+radio', data=advdf).fit()
print(variance_inflation_factor(advdf.values, 1))
print(variance_inflation_factor(advdf.values, 2))
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(advdf.values, i)for i in range(1, 3)]
print(vifdf)
#    vif_value
# 0  12.570312    tv : 다중공선성이 있다. 독립변수에서 제거해야 하는 영향력이 큰 변수라면 고민이 필요
# 1   3.153498    radio :

# 컬럼이 독립변수가 더 많은 경우, 예를 들어 남편의 수입과 아내의 수입이 서로 상관성이 높다면 두 개의 변수를 
# 더해서 가족 수입이라는 새로운 변수룰 작성하거나 또는 주성분분석을 이용하여 하나의 변수로 만들어 작업할 수 있다.

print("참고 : Cook's distance - 극단값을 나타내는 지표 이해 --")
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm_mul).cooks_distance  # 극단값을 나타내는 지표를 반환
print(cd.sort_values(ascending=False).head())

statsmodels.api.graphics.influence_plot(lm_mul, criterion='cooks')
plt.show()  # 원의 크기가 특별히 큰 데이터는 이상값 (outlinear) 이라 볼 수 있다.

