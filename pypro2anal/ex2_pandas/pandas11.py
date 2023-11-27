# 네이버 제공 주식 자료를 읽어 csv 파일로 저장
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page={}"
fname = "pandas11_stock.csv"
# fObj = open(fname, mode='w', encoding='utf-8', newline='')  # ''은 공백 제거
fObj = open(fname, mode='w', encoding='utf-8-sig', newline='')  # 엑셀에서 로딩시 한글 깨짐 방지
writer = csv.writer(fObj)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	  ROE".split()
print(title)
writer.writerow(title)

for page in range(1, 3):  # 2페이지만
    result = requests.get(url.format(str(page)))  # url에 주소에 {}가 있으니까
    result.raise_for_status()  # 200 ok 코드가 아닌 경우 에러 발생
    soup = BeautifulSoup(result.text, 'html.parser')
    # print(soup)
    datas = soup.find("table", attrs={'class': 'type_2'}).find('tbody').find_all('tr')
    # print(datas)
    for row in datas:
        cols = row.findAll('td')
        # print(cols)
        if len(cols) <= 1:continue  # [''] 작업에서 제외
        data = [col.get_text().strip() for col in cols]
        # print(data)
        writer.writerow(data)
fObj.close()

import pandas as pd
df = pd.read_csv(fname)
print(df)





