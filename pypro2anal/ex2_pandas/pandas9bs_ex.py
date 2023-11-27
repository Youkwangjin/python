import urllib.request as req
from bs4 import BeautifulSoup
import statistics

url = "https://www.kyochon.com/menu/chicken.asp"
kyochon = req.urlopen(url)


soup = BeautifulSoup(kyochon, 'html.parser')
data1 = soup.select('dl.txt > dt')
data2 = soup.select('p.money > strong')

names = [i.string for i in data1]
prices = [i.string for i in data2]

# 가격 데이터 정제 (쉼표와 '원' 문자 제거 후 정수로 변환)
numeric_prices = [int(price.replace(',', '').replace('원', '')) for price in prices]

# 출력 상품명 및 가격
for name, price in zip(names, numeric_prices):
    print(f'name: {name}, price: {price}원')

# 가격 데이터를 기반으로 평균과 표준편차 계산
average_price = statistics.mean(numeric_prices)
std_deviation = statistics.stdev(numeric_prices)

print(f'평균 가격: {average_price:.2f}원')
print(f'표준편차: {std_deviation:.2f}')
print()

print('========== adidas 구하기 ==========')
url = "https://www.adidas.co.kr/men-trend_now"
adidas = req.urlopen(url)
print(adidas)

