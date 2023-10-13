# 파이썬의 추상 클래스 : 추상 메서드를 한 개라도 가지고 있다면 추상 클래스가 된다.
from abc import abstractmethod, ABCMeta

class AbstractClass(metaclass=ABCMeta): # 추상 클래스(객체 생성 불가)
    
    @abstractmethod
    def abcMethod(self): # 추상 메서드
        pass 
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메서드')
        
# parent = AbstractClass() TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod


# c1 = Child1() TypeError: Can't instantiate abstract class Child1 with abstract method abcMethod

class Child1(AbstractClass):

    def abcMethod(self):
        name = '난 Child1'
        print('Child1에서 추상메서드를 오버라이딩을 한다 순전히 강요 때문에')
        
c1 = Child1() 
# print(c1.name)
c1.abcMethod()
c1.normalMethod()
print("=" * 50)

class Child2(AbstractClass):

    def abcMethod(self):    # 오버라이드 강요
        print('Child2에서 추상메서드를 제정의')
        print('추상의 마법에서 벗어남')
        
    def normalMethod(self): # 오버라이드 선택
        print('추상 클래스의 알반 메서드를 재정의 한다.')

c2 = Child2()
c2.abcMethod()
c2.normalMethod()
print("=" * 50)

# 추상클래스는 오로지 다형성 때문에 존재한다.

good = c1
good.abcMethod()
good.normalMethod()
print("=" * 50)

good = c2
good.abcMethod()
good.normalMethod()
