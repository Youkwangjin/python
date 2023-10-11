# 클로저 : scope의 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다.
# 함수 내에서 선언한 지역변수를 함수 밖에서 사용하기 위한 방법
def funcTimes(a, b):
    c = a * b
    print(c)
    return c

funcTimes(2, 3)
# print(c)      NameError: name 'c' is not defined

imsi = funcTimes(2, 3)
print(imsi)
print("=" * 50)

# 클로저 테스트 : 클로저를 사용하지 않은 경우
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())
out()
# print(out + 1) TypeError: unsupported operand type(s) for +: 'function' and 'int'
print("=" * 50)

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # <= 요게 바로 클로저 : 내부의 함수의 주소를 반환

var1 = outer()
print(var1) # <function outer.<locals>.inner at 0x000001BB8172DC60>
print(var1())
print(var1())
print(var1())
print("=" * 50)

var2 = outer()
print(var2())
print(var2())
print(id(var1), ' ', id(var2)) # 2376835914848   2376835914688
print("=" * 50)

# 수량, 단가, 세금(분기별로 동적으로 바뀌게)을 출력하는 함수 작성
def outer2(tax): # tax는 outer2에서만 유효하는 지역변수
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2

# 1분기에는 tax : 0.1
q1 = outer2(0.1)
print(q1) # <function outer2.<locals>.inner2 at 0x000001763232E160>
result1 = q1(5, 50000)
print('result1 :', result1)   
result2 = q1(1, 10000)
print('result2 :', result2)
print()
q2 = outer2(0.05)
result3 = q2(5, 50000)
print('result3 :', result3)
result4 = q2(2, 10000)
print('result3 :', result4)

    
    
    
    