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

    # 생성자 : 클래스에서 무조건 인스턴스를 찍어내는 시점에 가장 먼저 실행이 된다.
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self): # 여기서 self는 a.setDat를 가리킨다. 이유는 처음 클래스를 사용할 객체를 만들 때 self를 a라고 지정했기 때문.
        result = self.first + self.second
        return result


# a = FourCal() TypeError: FourCal.__init__() missing 2 required positional arguments: 'first' and 'second'
# 위 오류는 생성자에는 2개의 인자를 받고 시작하는데 위 코드는 인수를 지정해주지 않아서 오류가 발생하였다.
a = FourCal(4, 2) # 자바로 치면 FourCal a = new FourCal(); 이다.
print(a.add())

# 클래스의 상속 : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
class MultFourCal(FourCal):
    def pow(self):
        re = self.first ** self.second
        return  re

b = MultFourCal(4,2)
print(b.pow())
print("=" * 50)
class Family:
    lastName = '김'

a = Family()
b = Family()

print(a.lastName)
print(b.lastName)