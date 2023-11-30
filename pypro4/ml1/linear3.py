# 단순 선형 회귀 분석 모델 작성 : ols() 함수 사용 - OLS Regression Results 내용 알기
# 결정론적 선형회귀분석 방법 - 확률적 모형에 비해 불확실성이 덜하다.
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
plt.rc('font', family='malgun gothic')

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3), df.shape)
print(df.corr(method='pearson'))  # 적절성 / 만족도 : 0.766853
#          친밀도     적절성     만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000

# 독립변수(x, feature) : 적절성
# 종속변수(y, label) : 적절성
# 목적 : 주어진 feature 와 결정적 기반에서 학습을 통해 최적의 w와 x값을 구한다. (회귀 계수(slope, bias)를 찾아내는 것)
model = smf.ols(formula='만족도 ~ 적절성', data=df).fit()
# print(model.summary())
print(model.params)
print(model.pvalues)

# 예측값
print(df.적절성[:5].values)
new_df = pd.DataFrame({'적절성': [4, 3, 4, 2, 2]})
new_pred = model.predict(new_df)
print('만족도 실제 값 : ', df['만족도'][:5].values)
print('만족도 실제 값 : ', new_pred)

# 만족도 실제 값 :  [3 2 4 2 2]
# 만족도 실제 값 :  0    3.735963
# 1    2.996687
# 2    3.735963
# 3    2.257411
# 4    2.257411

# 이 표는 회귀 모델의 통계적 유의성과 성능을 평가하는 데 사용.
# Prob (F-statistic): 2.24e-52 => pvalue 52는 2.24 앞에 0이 52개 있다는 뜻이다.
# R-squared는 모델이 종속 변수의 변동을 얼마나 잘 설명하는지를 나타내며, 0.588로 나타냈다.
# Adj. R-squared는 독립 변수의 수를 고려하여 조정된 결정 계수. 모델이 데이터에 얼마나 잘 적합되었는지를 평가하는데 사용됩
# F-statistic는 회귀 모델 전체의 통계적 유의성을 검정하는데 사용되며, 해당 값이 매우 크면 모델이 유의미하다는 것을 의미
# ==============================================================================
# Dep. Variable:                    만족도   R-squared:                       0.588
# Model:                            OLS   Adj. R-squared:                  0.586
# Method:                 Least Squares   F-statistic:                     374.0
# Date:                Fri, 10 Nov 2023   Prob (F-statistic):           2.24e-52
# Time:                        16:45:36   Log-Likelihood:                -207.44
# No. Observations:                 264   AIC:                             418.9
# Df Residuals:                     262   BIC:                             426.0
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#               coef    std err(표준오차)   t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
# 적절성           0.7393      0.038     19.340      0.000       0.664       0.815
# ==============================================================================
# Omnibus:                       11.674   Durbin-Watson:                   2.185
# Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
# Skew:                          -0.328   Prob(JB):                     0.000335
# Kurtosis:                       4.012   Cond. No.                         13.4
# ==============================================================================
