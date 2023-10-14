import random

class LottoBall:
    def __init__(self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.ballList = [] # 순서가 필요하므로
        for i in range(1, 46):
            self.ballList.append(LottoBall(i)) # 클래스의 포함관계 45개가 ballList에 들어간다.
        
    
    def selectBall(self):
        # 번호를 섞기 전
        for a in range(45):
            print(self.ballList[a].num, end = ' ')
        print()
        # 번호를 섞기 후
        random.shuffle(self.ballList) # random 함수를 사용해서 숫자들이 랜덤으로 나온다.
        for a in range(45):
            print(self.ballList[a].num, end = ' ')
        print()# 콘솔에 잘      보이게 하기 위해 쓴거임
        print("=" * 50)
        return self.ballList[0:6] # 0번째 부터 5번째 까지 숫자를 출력
    
class LottoUI:
    def __init__(self):
        self.machine = LottoMachine() # 포함관계
    
    def playLotto(self):
        input('로또 볼을 뽑으려면 enter를 눌러주세용') # 아무키나 누르라는 소리.
        selectedBalls = self.machine.selectBall()
        for ball in selectedBalls:
            print("%d"%ball.num)
            
if __name__ == '__main__':
    LottoUI().playLotto()

