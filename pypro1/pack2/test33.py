# 추상

from abc import ABCMeta, abstractmethod

# 추상 클래스
class Friend(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod    
    def hobby(self):
        pass
    
    def printName(self):
        print('이름은 ' + self.name)
        

# 일반 클래스
class John(Friend): # 추상 클래스인 Friend 상속
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr 
            
    def hobby(self):
        print(self.addr + ' 거리를 산책함')
        
    def printAddr(self):
        print('주소는 ' + self.addr)
        

class Chris(Friend):
    def __init__(self, name, addr):
        super().__init__(name)
        self.addr = addr
            
    def hobby(self):
        print(self.addr + ' 동네를 어슬렁 거림')
        print(self.addr + '에 오래 전부터 살고 있다.')


# 클래스 실행
john = John('미스터 존', '역삼1동')
john.printName()
john.printAddr()
john.hobby()   
print("=" * 50)

chris = Chris('크리스', '역상2동')
chris.printName()
chris.hobby()
print("=" * 50)

# 다형성
fri = john
fri.hobby()
print("=" * 50)

fri = chris
fri.hobby()  
    