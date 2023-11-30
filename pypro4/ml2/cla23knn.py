# 주변의 가장 가까운 K개의 데이터를 보고 데이터가 속할 그룹을 판단하는 알고리즘이 K-NN 알고리즘이다.
# feature의 수가 많거나, 이상치가 있으면 성능이 떨어짐
# 서로 다른 값들의 비율(단위)이 일정하지 않으면 성능이 떨어지므로 스케일링(표준화, 정규화)을 권장

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

train = [
    [5, 3, 2],
    [6, 4, 2],
    [3, 2, 1],
    [2, 4, 6],
    [1, 3, 7]
]

label = [0, 0, 0, 1, 1]
# plt.xlim([-1, 7])
# plt.xlim([0, 10])
# plt.plot(train, 'o')
# plt.show()

kmodel = KNeighborsClassifier(n_neighbors=1)  # n_neighbors은 k값
kmodel.fit(train, label)
pred = kmodel.predict(train)
print('pred : ', pred)
print('test acc : {:.2f}'.format(kmodel.score(train, label)))

newData = [[1, 2, 15], [78, 22, -5]]
newpred = kmodel.predict(newData)
print('newpred : ', newpred)



