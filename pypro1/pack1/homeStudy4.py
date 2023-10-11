# 자바에서는 메서드라고 불리는게 파이썬에는 함수라 부른다.
# 매게변수(parameter) 함수에서 정의되어 사용되는 변수(인자라고도 부른다.)
# 인수(argument) 함수를 호출할 때 건네주는 변수 

def add(a, b): # a, b는 매개변수(parameter)
    return a + b
print(add(3, 4)) # 3, 4는 인수(argument)
print("=" * 50)

# 예제
a = 1 # 여기서 a는 전역변수
def vartest(a): # 여기서 a는 지역변수
    a = a + 1
    
vartest(a)
print(a)
print("=" * 50)

# 예제 
def add2(a, b):
    result = a + b
    return result;
print(add2(10, 15))
print("=" * 50)

# 클래스는 설계도 그 설계도에 의헤 만들어지는게 객체, 클래스는 명은 맨 앞글자를 대문자로 설정하는것이 관례이다.
# 객체는 값(변수)과 행동(함수, 자바에서는 메세드)이 있다. 
class FourCal:
    pass 

a = FourCal() # 자바로 치면 FourCal a = new FourCal(); 이다.
print(a)