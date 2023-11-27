import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False


# x = ['서울', '수원', '연천'] list
# x = {'서울', '수원', '연천'} 순서가 없기 때문에 사용 불가 (인덱싱 불가)

'''
x = ('서울', '수원', '연천')
y = [5, 3, 7]
plt.xlim([-1, 3])
plt.ylim([-5, 10])
plt.plot(x, y)
plt.yticks(list(range(-3, 11, 3)))
plt.xlabel('지역명')
plt.ylabel('친구명')
plt.title('선그래프')
plt.show()
'''

'''
# sin 곡선
x = np.arange(10)
y = np.sin(x)
print(x, y)
# plt.plot(x, y, 'bo')
plt.plot(x, y, 'go--', linewidth=3, markersize=10)
plt.show()
'''

# hold : '복수의 차트'  그리기 명령을 하나의 figure에 표현할 수 있다.
x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, c='r')
plt.scatter(x, y_cos, c='b')
plt.legend(['sin', 'cosine'], loc=1)  # loc는 시계 반대방향으로 움직인다.
plt.show()

# subplot : 여러 개의 영역으로 나눠 차트를 그린다.
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('sine')

plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('cosine')

plt.show()