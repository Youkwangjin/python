# has a (클래스의 포함관계 : 자원의 재활용이 목적이다. - 약결합)
# 완성차를 조립하기 위해 여러개의 부품(여기서는 핸들로 한정)을 객체로 만들어 불러다가 사용한다.


from pack2.test22handle import PohamHandle

# 클래스
class PohamCar:
    turnShowMessage = '정지'
    
    def __init__(self, ownerName):  # 기본생성자 
        self.ownerName = ownerName
        self.handle = PohamHandle() # 클래스의 포함 PohamHandle 인스턴스를 handle 치환한다.
    
    # turnHandle 함수
    # 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용
    def turnHandle(self, q):
        if q > 0: # 우회전
            self.turnShowMessage = self.handle.rightTurn(q) # 클래스의 포함관계
        elif q < 0: # 좌회전
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직진'
            self.handle.quantity = 0
            
if __name__ =="__main__":
    tom = PohamCar("톰 아저씨")
    tom.turnHandle(20) # tom은 self turnHandle은 q
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + " " + str(tom.handle.quantity))
    tom.turnHandle(0)
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + " " + str(tom.handle.quantity))
    print("=" * 50)
    
    oscar = PohamCar("오스카")
    oscar.turnHandle(-10)
    print(oscar.ownerName + "의 회전량은 " + oscar.turnShowMessage + " " + str(oscar.handle.quantity))


