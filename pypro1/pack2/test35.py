# singleton pattern (객체가 매번 안만들어진다.)

class SingletonClass:
    inst = None

    def __new__(cls):  # 객체의 생성을 담당한다. init 메서드에 의해 초기화된다.
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst

    def aa(self):
        print('난 메서드야!')


# 싱글톤 클래스를 상속받는다.
class SubClass(SingletonClass):
    pass

s1 = SubClass()
s2 = SubClass()

print(id(s1), id(s2))  # 1736072760144 1736072760144

s1.aa()
s2.aa()

print("=" * 50)
# 클래스의 멤버 변수를 고정
class Ani:
    __slots__ = ['irum', 'nai']

    def printData(self):
        print(self.irum, self.nai)

a = Ani()
a.irum = '호랑이'
a.nai = 3
# a.eat = '치킨'  AttributeError: 'Ani' object has no attribute 'eat' 클래스의 멤버 변수를 고정으로 인해 변수 추가가 되지 않는다.
a.printData()
