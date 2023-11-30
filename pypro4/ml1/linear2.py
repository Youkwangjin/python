print('방법4 : linear 사용. 모델 생성 됨')

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IQ에 따른 시험 점수 값 예측
score_iq = pd.read_csv("../testdata/score_iq.csv")
print(score_iq.head(3), score_iq.shape)
x = score_iq.iq
y = score_iq.score

# 상관계수 확인
print(np.corrcoef(x, y)[0, 1])   # 0.882220
# plt.scatter(x, y)
# plt.show()

# 인과관계가 있다는 가정하에 선형회귀분석 모델 생성
model = stats.linregress(x, y)
print(model)
print('x 기울기 : ', model.slope)
print('y 절편 : ', model.intercept)
print('상관 계수 : ', model.rvalue)
print('p값 : ', model.pvalue)

# plt.scatter(x, y)
# plt.plot(x, model.slope * x + model.intercept, c='r')
# plt.show()

# 회귀 모델 수식 : y = model.slope * x + model.intercept
print('점수 예측 : ', model.slope * 80 + model.intercept)
print('점수 예측 : ', model.slope * 120 + model.intercept)
print('점수 예측 : ', model.slope * 140 + model.intercept)
# predict() 차원 x : numpy의 ployval([기울기, 절편], x)을 사용

print('점수 실제값 : ', score_iq['score'][:5].values)   # [90 75 77 83 65]
# [88.34388626 78.57242197 75.31526721 85.0867315  65.54380291]
print('점수 예측값 : ', np.polyval([model.slope, model.intercept], np.array(score_iq['iq'][:5])))

new_df = pd.DataFrame({'iq': [83, 90, 100, 127, 141]})
print('새로운 점수 예측값 : ', np.polyval([model.slope, model.intercept], new_df))

# [[51.21232195]
#  [55.77233862]
#  [62.28664815]
#  [79.87528387]
#  [88.99531721]]

# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량에 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 운동 10시간 초과는 이상치로 한다.

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


data = StringIO('''
구분,지상파,종편,운동
1,0.9,0.7,4.2
2,1.2,1.0,3.8
3,1.2,1.3,3.5
4,1.9,2.0,4.0
5,3.3,3.9,2.5
6,4.1,3.9,2.0
7,5.8,4.1,1.3
8,2.8,2.1,2.4
9,3.8,3.1,1.3
10,4.8,3.1,35.0
11,NaN,3.5,4.0
12,0.9,0.7,4.2
13,3.0,2.0,1.8
14,2.2,1.5,3.5
15,2.0,2.0,3.5''')

df = pd.read_csv(data)  # ,로 구분되어 있으니 csv로 읽는다.
print(df.head(2), type(df))  # <_io.StringIO object at 0x00000255B6FFBC70>
#    구분  지상파   종편   운동
# 0   1  0.9  0.7  4.2
# 1   2  1.2  1.0  3.8

avg = df['지상파'].mean()
df = df.fillna(avg)
# print(df)

# 이상치가 있는 행은 제거
for d in df.운동:
    if d > 10:
        df = df[df.운동 != d]

for d in df.지상파:
    if d > 10:
        df = df[df.지상파 != d]

for d in df.종편:
    if d > 10:
        df = df[df.종편 != d]

print(df, df.head(3), df.shape)  # (14, 4)

# - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
x = df.지상파
y = df.운동

model = stats.linregress(x, y)
print('기울기 : ', model.slope)              # -0.6684550167105406
print('절편 : ', model.intercept)           # 4.709676019780582
print('상관계수 : ', model.rvalue)           # -0.8655346605559783
print('p값 : ', model.pvalue)              # 6.347578533142469e-05

# plt.scatter(x, y)
# plt.plot(x, model.slope * x + model.intercept, c='r')
# plt.show()

new_df = pd.DataFrame({'지상파':[0.1, 1.0, 2.5, 3.5, 5.5]})
print('새로운 운동 시간 예측값 : ', np.polyval([model.slope, model.intercept], new_df))



