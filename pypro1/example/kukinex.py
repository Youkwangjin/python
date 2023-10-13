class Machine:
    def __init__(self, cupCount):
        self.cupCount = cupCount

    def showData(self):
        print('남은 커피 잔수: ', self.cupCount)


class CoinIn:
    def __init__(self, cupCount, coin):
        self.machine = Machine(cupCount)
        self.coin = coin


    def change(self):
        coin_input = int(input('동전을 입력하세요: '))
        price = self.coin * cupCount

        if price == coin_input:
            change_amount = coin_input - price
            print('커피' + str(cupCount) +'잔과 잔돈' + str(price - coin_input) + '원')
        elif price > coin_input:
            print('요금이 부족합니다')
        elif price < coin_input:
            print('커피' + str(cupCount) +'잔과 잔돈' + str(coin_input - price) + '원')

if __name__ == '__main__':
    cupCount = int(input('커피 잔 수를 입력하세요: '))
    coin = 200
    coin_in = CoinIn(cupCount, coin)
    coin_in.change()