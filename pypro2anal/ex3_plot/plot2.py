# matplotlib 스타일 인터페이스, 차트종류 몇 가지 경험하기

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(10)
'''
# matplotlib 스타일 인터페이스 
plt.figure()
plt.subplot(2, 1, 1)  # 힝식 ; (row. column, panel, number
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()

# matplotlib 스타일 인터페이스 - 객체지향 인터페이스
fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(x, np.sin(x))
ax[1].scatter(x, np.cos(x))
plt.show()
'''

data = [50, 80, 100, 70, 80]
# 막대 그래프
plt.bar(range(len(data)), data)  # x축
plt.show()

'''
# 새로 막대 그래프
err = np.random.rand(len(data))
plt.barh(range(len(data)), data, xerr=err)  # error bar (오차 막대) : 편차, 오차, 신뢰구간 등 표현에 효과적
plt.show()
'''

'''
#  원 그래프
plt.pie(data, explode=(0, 0, 0.2, 0, 0), colors=['yellow', 'blue', 'red'])
plt.show()
'''

# 히스토그램
plt.hist(data, bins=5, alpha=0.1)
plt.show()

# 박스 그래프
plt.boxplot(data, notch=True)
plt.show()

# 시계열 데이터 출력
import pandas as pd
fdata = pd.DataFrame(np.random.rand(1000, 4), index=pd.date_range('1/1/2000', periods=1000))
columns = list('abcd')
print(fdata.head(3))
print((fdata.tail(3)))
plt.plot(fdata)
plt.show()

# pandas의 plot 기능
fdata.plot(kind='box')
plt.show()

# mapplottlib의 기능 보충용 lib로 seaborn

import seaborn as sns

# seaborn 데이터셋 목록
# print(sns.get_dataset_names())

'''
titanic = sns.load_dataset('titanic')
# print(titanic.info())
print(titanic.head(3))
plt.plot(titanic['age'])
plt.show()

sns.displot(titanic['age'])
plt.show()

sns.boxplot(y='age', data=titanic)
plt.show()
'''


# iris dataset
iris_data = sns.load_dataset('iris')
print(iris_data.head(3))

import pandas as pd
iris_data = pd.read_csv('../testdata/iris.csv')
print(iris_data.head(3))

# 산점도
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.show()


# Species별 색상 부여
# print(iris_data['Species'].unique())
# print(set(iris_data['Sepal.Length']))  # ['setosa' 'versicolor' 'virginica']

cols = []
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa': choice = 1
    elif s == 'versicolor': choice = 2
    elif s == 'virginica': choice = 3
    cols.append(choice)

plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=cols)
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Length')
plt.show()

# Sepal.Length, Sepal.width, Petal.Length를 사용해 scatter matrix 그래프 출력
iris_col = iris_data.loc[:, 'Sepal.Length': 'Petal.Width']
print(iris_col)

pd.plotting.scatter_matrix(iris_col, diagonal='kde')
plt.show()

# seaborn으로 scatter_matrix 그래프 출력
sns.pairplot(iris_data, hue='Species', height=2)
plt.title('seaborn으로 scatter_matrix 그래프 출력')
plt.show()

# 그래프(차트)를 이미지로 저장
fig = plt.gcf()
plt.show()
fig.savefig('plot2.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('plot2.png')
plt.imshow(img)
plt.show()
