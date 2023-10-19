# [문항15] 아래 코드가 동작하도록 자전거 클래스(Bicycle class)를 정의하시오.
# 조건1 : 멤버 변수는 name, wheel, price 이다.
# 조건2 : 바퀴 가격은 바퀴수 * 가격이다. (배점:10)
# 출력 결과)
# gildong = Bicycle('길동', 2, 50000)      # name, wheel, price
# gildong.display()

class Bicycle:
    name = ""
    wheel = 0
    price = 0

    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price

    def pay(self):
        rs = self.wheel * self.price
        return rs

    def display(self):
        print(f"{self.name}님의 자전거 바퀴 가격 총액은" + " " + str(self.pay()) + "원 입니다.")


gildong = Bicycle('길동', 2, 50000)
gildong.display()



