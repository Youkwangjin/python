# 함수 : 반복소스의 단순화를 목표로, 여러 개의 수행문을 하나의 이름으로 묶은 실행단위
# 내장함수
from pack1.test3 import mydic
print(sum([3,4,5])) # List
print(bin(8))
print(int(1.5), float(3), str(5) + '오')
print(round(1.3), round(1.6))
print("=" * 50)
# ceil, floor 는 import 해야한다.
import math
print(math.ceil(1.3), math.ceil(1.6))
print(math.floor(1.3), math.floor(1.6))
print("=" * 50)

x = [10,20,30]
y = ['a', 'b']
for i in zip(x, y):
    print(i) # (10, 'a') (20, 'b')
print("=" * 50)

# 사용자 정의 함수
# 양식 : def 함수명 (parameter,...):
#         return 반환값을 주거나 안주거나~

def func1():
    print('func1 수행') 

func1()
print("=" * 50)
func1() # 함수는 명시적으로 적어주지 않으면 None을 반환한다.
imsi = func1()
print(imsi)
print(func1) # <function func1 at 0x00000249E355DC60> 객체를 참조하고 있다.
print("=" * 50)

def func2(para1, para2):
    result = para1 + para2
    aa = func3(result)
    return aa


def func3 (result):
    if result % 2 == 1:
        return 
    else:
        return result
    
print(func2(3, 4)) # 인수
print(func2(3, 5))
print(func2, id(func2)) # 0x00000295D6BD5A80 2842576116352

print("=" * 50)
def swap(a, b):
    return b, a # return (b, a) 파이썬도 반환값이 하나이다.

a = 10; b = 20
print(swap(a, b))
print("=" * 50)

def func4():
    print('func4 처리')
    def func5(): # 함수안에서 또 다른 함수를 정의할 수 있다.
        print('내부 함수 처리')
    func5()
    
func4()
print("=" * 50)
# if 조건식 안에 함수 사용
def isodd(para):
    return para % 2 == 1

mydict = {x:x*x for x in range(11) if isodd(x)} # 딕셔너리 자료형
print(mydict)


