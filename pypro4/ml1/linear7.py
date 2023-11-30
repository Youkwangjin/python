# LinearRegression 클래스를 사용해 선형회귀모델 작성

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# 편차가 큰 표본 데이터를 생성
sample_size = 100
# 정규분포를 위한 난수발생
np.random.seed(1)
x = np.random.normal(0, 10, sample_size)
y = np.random.normal(0, 10, sample_size) + x * 30
print(x[:10])
print(y[:10])
print('상관계수 : ', np.corrcoef(x, y))  # 0.99939357

# 객체 생성
scaler = MinMaxScaler()  # 정규화
x_scaled = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled[:10].flatten())


# 시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled, y)
y_pred = model.predict(x_scaled)
print('예측값 : ', y_pred[:10])
print('실제값 : ', y[:10])

# 모델 성능 확인
# print(model.summary()) LinearRegression은 summary을 지원하지 않는다.

def regScoreFunc(y_true, y_pred):
    print('r2_score(결정계수, 설명력):{}'.format(r2_score(y_true, y_pred)))
    print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(MSE, 평균제곱근오차):{}'.format(mean_squared_error(y_true, y_pred)))

regScoreFunc(y, y_pred)
# r2_score(결정계수, 설명력):0.9987875127274646
# explained_variance_score(설명분산점수):0.9987875127274646  # 결정계수와 설명분산점수의 결과의 차이(편함)가 크다면 모델 학습이 잘못
# mean_squared_error(MSE, 평균제곱근오차):86.14795101998743

print("=" * 70)
# 분산이 크게 다른 표본 데이터를 생성
x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 500, sample_size) + x * 30
print(x[:10])
print(y[:10])
print('상관계수 : ', np.corrcoef(x, y))
# 상관계수 :  [[1.         0.00401167]
#  [0.00401167 1.        ]]  => 시각화 해보나 마나

# 객체 생성
scaler = MinMaxScaler()  # 정규화
x_scaled2 = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled2[:10].flatten())

model2 = LinearRegression().fit(x_scaled2, y)
y_pred2 = model2.predict(x_scaled2)
print('예측값 : ', y_pred2[:10])
print('실제값 : ', y[:10])

regScoreFunc(y, y_pred2)
# r2_score(결정계수, 설명력):1.6093526521765433e-05
# explained_variance_score(설명분산점수):1.6093526521765433e-05
# mean_squared_error(MSE, 평균제곱근오차):282457.9703485092
