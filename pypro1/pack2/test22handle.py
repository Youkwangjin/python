# 완성품 부품으로 핸들 클래스를 작성

class PohamHandle:
    quantity = 0 # 회전량 (의미없다. 안적어도 된다.) 
    
    def leftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def rightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    
    #...

class PohamEngine:
    pass