# 모듈의 멤버 중 클래스
# 클래스는 이름 공간과 클래스가 생성하는 인스턴스 이름 공간을 각각 갖는다.
# 클래스는 새로운 이름 공간을 지원하는 단위로 메서드와 변수라는 멤버를 지닌다.
# 접근지정자(public, private)없다 따라서 메서드 오버로딩도 없다.

class TestClass:  # 클래스의 Header이며 이하 소스는 body 영역이 돈다.
    aa = 1        # body, 멤버변수는 클래스 내에서 전역
    
    def __init__(self): # 메서드는 첫 parameter(파라미터)는 무조건 self 자바에서 this 라고 생각하자.
        print('생성자')   # 초기화 작업
    
    def __del__(self):
        print('소멸자')   # 마무리 작업 (파이썬에서는 소멸자는 잘 사용하지 않는다.)
    
    def printMsg(self): # 멤버 메서드
        name = '한국인'   # 지역변수
        print(name)
        print(self.aa)

test = TestClass()       # 생성자 호출 후 인스턴스(객체)가 만들어진다.
print(test.aa)
test.printMsg()          # 메서드를 call(호출) 방법 1 : Bound method call
TestClass.printMsg(test) # 방법 2 : UnBound method call
print("=" * 50)

print(isinstance(test, TestClass)) # True
print(type(1))
print(type(test))
print(id(test), id(TestClass)) # 1840392734096   1838246302512 인스턴스 주소를 참조

del test # 인스턴스 삭제

