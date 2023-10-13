class Machine:
    cupCount = 1
    
    def __init__(self):
        pass
            
    def showData(self, coin, cup):
        coin = int(coin) # 동전
        cup = int(cup)   # 커피잔
        
        if (coin - 200 * cup) < 0:
            print('요금이 부족행')
            return 0
        else:
            showData = coin - 200 * cup
            return showData

class CoinIn:
    
    def __init__(self):
        self.machine = Machine() # 클래스의 포함관계
    
               
    def culc(self):
        coin = input('동전을 입력하세요: ')
        cup = input('몇 잔을 원하세요: ')
        showData = self.machine.showData(coin, cup)
        if showData > 0:
            print(f'{cup} 잔의 커피가 나왔습니다. 거스름돈은 {showData}원입니다.')
        else:
            print('거스름돈이 없습니다.')
    

if __name__ == '__main__':
    CoinIn().culc()