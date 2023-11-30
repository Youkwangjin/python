# 단순선형회귀 분석 : iris dataset, 함수는 ols() 사용
# 상관관계가 약한 경우와 강한 경우를 나눠 분석 모델을 작성 후 비교


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf


iris = sns.load_dataset('iris')
print(iris.head(3), iris.shape)  # (150, 5)
print(iris.iloc[:, 0:4].corr())
#               sepal_length  sepal_width  petal_length  petal_width
# sepal_length      1.000000    -0.117570      0.871754     0.817941
# sepal_width      -0.117570     1.000000     -0.428440    -0.366126
# petal_length      0.871754    -0.428440      1.000000     0.962865
# petal_width       0.817941    -0.366126      0.962865     1.000000

# 상관관계가 약한 경우 : sepal_length  sepal_width : -0.117570
result1 = smf.ols(formula='sepal_length ~ sepal_width', data=iris).fit()
print('result1 모델 정보 : ', result1.summary())
print('result1 R_squared : ', result1.rsquared)  # 0.013822654141080748
print('result1 p-value : ', result1.pvalues[1])  # 0.1518 > 0.05 이므로 모델은 유의하지 않다. (의미 없는 모델)

plt.scatter(iris.sepal_width, iris.sepal_length)
# plt.plot(iris.sepal_width, result1.predict(), color='r')
# plt.show()

# 상관관계가 강한 경우 : sepal_length  sepal_width : -0.117570
result2 = smf.ols(formula='sepal_length ~ petal_length', data=iris).fit()
print('result2 모델 정보 : ', result2.summary())
print('result2 R_squared : ', result2.rsquared)  # 0.7599546457725153
print('result2 p-value : ', result2.pvalues[1])  # 1.0386 > 0.05 이므로 모델은 유의하지 않다. (의미 없는 모델)

plt.scatter(iris.petal_length, iris.sepal_length)  # 0.7599546457725153
# plt.plot(iris.petal_length, result2.predict(), color='r')
# plt.show()

print('실제값 : ', iris.sepal_length[:10].values)
print('예측값 : ', result2.predict()[:10])


# 새로운 petal_length로 sepal_length로 예측 가능
new_data = pd.DataFrame({'petal_length' : [1.1, 0.5, 5.0]})
y_pred = result2.predict(new_data)
print('예측 결과 : ', y_pred.values)

print('다중선형회귀 : 독립변수가 복수')
# result3 = smf.ols(formula='sepal_length ~ petal_length + petal_width + sepal_width', data=iris).fit()
column_select = "+".join(iris.columns.difference(['sepal_length', 'species']))
print(column_select)
result3 = smf.ols(formula='sepal_length ~ ' + column_select, data=iris).fit()
print('result3 모델 정보 : ', result3.summary())

