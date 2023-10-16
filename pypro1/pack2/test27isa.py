# 상속 연습
print('클래스는 모듈의 멤버이다')  # 자바랑 다른점

class Person:
    say = '난 사람'    # 공유 자원 / public
    nai = '20'
    __my = 'private 멤버'     # private / __를 붙히면 현재 클래스내에서만 쓸 수 있는 멤버 변수가 됨

    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai      # 각각의 인스턴스마다 만들어짐 / Person의 공유자원으로도 있고 각 각의 인스턴스에도 있다

    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))

    def hello(self):
        print('안녕')
        print(self.__my)

    @staticmethod   # 독립적으로 수행 / 어디서든 자유롭게 불러올 수 있다
    def kbs(tel):
        print('kbs_static method(클래스 소속) : ', tel)



print(Person.say, Person.nai)
# Person.printInfo()    self를 만족 시킬 수 없기 때문에 에러
p = Person('25')
print(p.say, p.nai)
p.printInfo()   # 객체 변수 p가 인수로 담겨서 파라미터로 넘어감

p.hello()
p.kbs('111-1234')


print('***' * 20)
class Employee(Person):
    subject = '근로자'

    def __init__(self):
        print('Employee 생성자')

    def printInfo(self):    # method overriding / 오버라이딩이 있어야 다형성을 구사할 수 있음
        print('Employee의 오버라이딩된 printInfo')

    def eprintInfo(self):
        print(self.say, super().say)    # self.say는 Employee 클래스부터 찾아가면서 없으면 위로 올라가고 super()은 처음부터 위에서 찾아가면서 내려 옴
        self.hello()
        self.printInfo()    # 오버라이딩된 printInfo가 없으면 부모 클래스의 printInfo를 가지고 옴
        super().printInfo()     # 얜 바로 가지고 옴

e = Employee()      # employee 생성자를 지우면 에러가 뜨는데 그 이유는 자식 클래스의 생성자가 없으면 부모 클래스의 생성자를 부르는데 부모 클래스의 생성자는 nai를 받아야하기 때문
print(e.say, e.subject)
e.eprintInfo()


print('***' * 20)
class Worker(Person):
    say = 'Worker의 say'

    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)   # Bound method call / self와 nai가 같이 넘어 감 / 자바와 파이썬의 차이 : 자바와 달리 파이썬은 생성자 호출을 나중에 적어줘도 됨

    def printInfo(self):
        print('Worker에 선언된 printInfo')

    def wprintInfo(self):
        self.printInfo()
        super().printInfo()


w = Worker('30')
print(w.say, w.nai)  # 나이30은 Person이 가지고 있는게 아니라 Worker 인스턴스가 가지고 있음(say도 마찬가지) / 자식이 가지고 있으면 부모는 은닉화
#w.printInfo()   이것도 마찬가지로 Worker의 인스턴스 say와 nai를 가지고 Person의 printInfo로 감 / 만약 Worker(자식)가 가지고 있지 않다면 부모껄로 가지고 옴
w.wprintInfo()


print('***' * 20)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai)     # Bound method call
        Worker.__init__(self, nai)  # UnBound method call

    def pprintInfo(self):
        self.wprintInfo()

    def hello2(self):
        print('안녕')
        # print(self.__my)  error : private 멤버 이므로 안됨


pr = Programmer('33')
print(pr.say, pr.nai)
pr.pprintInfo()

pr.hello2()
pr.kbs('111-1234')
Programmer.kbs('111-1234')


print('\n클래스 타입 확인----------')
print(type(1.2))
print(type(pr))
print(Programmer.__bases__)     # 자식 클래스의 부모를 볼 수가 있음 / (<class '__main__.Worker'>,) -> 집합형인거 보니깐 다중상속이 가능하다
print(Worker.__bases__)
print(Person.__bases__)
