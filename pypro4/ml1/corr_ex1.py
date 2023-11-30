# 공분산 / 상관계수
import numpy as np

print(np.cov(np.arange(1,6),np.arange(2,7))) # 2.5
print(np.cov(np.arange(1,6),(3,3,3,3,3))) # 0
print(np.cov(np.arange(1,6),np.arange(6,1,-1))) # -2.5

print()
x=[8,3,6,6,9,4,3,9,4,3]
print('평균: ',np.mean(x),' , 분산: ', np.var(x))

y=[6,2,4,6,9,5,1,8,4,5]
print('평균: ',np.mean(y),' , 분산: ', np.var(y))

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()

print('x,y의 공분산 : ',np.cov(x,y))
print('x,y의 공분산 : ',np.cov(x,y)[0,1])


# print('x,y의 상관계수 : ',np.corrcoef(x,y))
print('x,y의 상관계수 : ', np.corrcoef(x, y)[0, 1])

print('----곡선의 경우에는 상관계수는 의미가 없다.----')
print()
m = [-3, -2, -1, 0, 1, 2, 3]
n = [9, 4, 1, 0, 1, 4, 9]
plt.plot(m, n)
plt.show()
print('m,n의 공분산 : ', np.cov(m, n)[0, 1])
print('m,n의 상관계수 : ', np.corrcoef(m, n)[0, 1])
# 곡선으로 표시되는 것은 공분산과 상관계수가 제대로 표시가 안된다 따라서 사용이 불가능함
