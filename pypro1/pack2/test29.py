# 다중 상속
class Tiger:
    data = '호랑이 세상'
    
    def cry(self):
        print('호랑이가 소리를 ...')
        
    def eat(self):
        print('맹수는 고기를 좋아해요')
        
class Lion:
    def cry(self):
        print('사자가 소리를 ...')
        
    def hobby(self):
        print('백수의 왕은 채팅을 즐김')

class Liger1(Tiger, Lion): # Tiger, Lion 다중 상속을 받는다. 먼저 적어준 부모의 멤버가 수행된다. 메서드가 중복일 경우에는
    pass

obj1 = Liger1()
obj1.cry()
obj1.eat()
obj1.hobby()
print(obj1.data)
print("=" * 50)

class Liger2(Lion, Tiger):
    data = '라이거 만세'
    
    def play(self):
        print('라이거 고유 메서드')
        
    def hobby(self):
        print('라이거는 운동을 좋아함')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data + ", " + super().data)  

obj2 = Liger2()
obj2.cry()
obj2.hobby()
obj2.showHobby()
