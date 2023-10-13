# 클래스의 상속, 파이썬은 다중상속이 가능하고 인터페이스가 없다

class Animal:   
    # 생성자
    def __init__(self):
        print('Animal 생성자')
           
    def move(self):
        print('움직이는 생물')
    
class Dog(Animal): # 상속을 받을 때 클래스에 ()를 부여한다.  Dog 클래스는 Animal 클래스를 상속받는다.
    # 생성자
    def __init__(self):
        print('댕댕이 생성자')
    def my(self):
        print('난 댕댕이야')

dog1 = Dog()
dog1.my()
dog1.move()
print("=" * 50)

class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()











