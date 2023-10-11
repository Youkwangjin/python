# 숫자형 (정수형)
from pyasn1 import type
a = 3
print(a)
print("=" * 50)

# 숫자형 (실수형)
b = 3.15
print(b)
print("=" * 50)

# 문자열 자료형
a = "유광진은"
b = "26살이다."
print(a + " " + b)
print("=" * 50)

a = "파이썬"
print(a * 3)
print("=" * 50)

a = "Life is too short"
print(len(a)) # 공백도 하나의 문자로 취급하기 때문에 17이 출력된다.
print("=" * 50)

# index
a = "Life is too short"
print(a[3])
print(a[12])  
print(a[-1]) # 음수는 역순이다.
# print(a[-100]) # 인덱스의 범위에서 벗어나기 때문에 오류 발생
print("=" * 50)

# 문자열 슬라이싱
a = "Life is too short"
# a[ : : ] 이상 : 미만 : 간격
b = a[0:4] # 0이상 4미만이므로 0부터 3까지의 문자열이 출력 
print(b)
print("=" * 50)

# 문자열 포매팅
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 하동을 %d번째 가봤다.'%5)
print("=" * 50)

# 문자열 갯수 알아보기
a = "hobby"
print(a.count('b'))
print("=" * 50)
# 문자열 위치 알아보기
a = "hobby"
print(a.find('b')) # index 개념에 따라 2번째에 있기 때문에 2가 출력된다.
print("=" * 50)

# 문자열 공백지우기
a = " hi "
print(a.lstrip()) # 왼쪽 공백 지우기
print("=" * 50)

# 리스트 자료형
a = []  #값이 없는 리스트
print(a)

b = [1,2,3]  #숫자가 입력된 리스트
print(b)

c = ["You", "Kwang", "Jin"]  #문자가 입력된 리스트
print(c)

d = ["You", "Kwang", "Jin", 10, 20]  #문자+숫자 같이 입력된 리스트
print(d)

# 패킹
*v1, v2 = 1,2,3,4,5
print(v1, v2)
v1, *v2 = 1,2,3,4,5
print(v1, v2)
v1, *v2, v3 = 1,2,3,4,5
print(v1, v2, v3)














