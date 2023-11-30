# sklearn의 분류모델은 연속형 결과 output이 연속형인 예측 모델도 제공
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

adver = pd.read_csv("../testdata/Advertising.csv")
print(adver.head(3))
print(adver.corr(method='pearson'))

x = np.array(adver.loc[:, 'tv': 'newspaper'])
y = np.array(adver.sales)
print(x[:3])
print(y[:3])

print('LinearRegression')
rmodel = LogisticRegression().fit(x, y)
rpred = rmodel.predict(x)
print('LinearRegression pred : ', rpred[:5])
print('LinearRegression real : ', y[:5])
print('결정계수 : ', r2_score(y, rpred))

print('XGBRegressor --')
xmodel = SVR(criterion='squared_error').fit(x, y)
xpred = xmodel.predict(x)
print('XGBRegressor pred : ', xpred[:5])
print('XGBRegressor real : ', y[:5])
print('결정계수 : ', r2_score(y, xpred))
