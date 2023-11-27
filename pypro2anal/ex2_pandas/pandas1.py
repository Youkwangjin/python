# pandas : 고수준의 자려구조(Series, DataFrame)를 지원
# 데이터 관리, 축약 연산, 시계열 처리, 누락 데이터 처리, SQL 실행, SpreadSheet, 시각화, 데이터 재배치 등의 작업 수행 가능.
# data munging, wrangling : 윔 재료를 새로운 형태의 데이터로 전향하는 매핑 작업
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# Series : 일련의 데이터(객체)를 담을 수 있는 1차워 배열과 같은 구조로 색인을 갖는다.  인덱싱된 데이터의 1차원 배열
obj = pd.Series([3, 7, -5, 5])  # list
# obj = pd.Series((3, 7, -5, 5)) tuple
# obj = pd.Series({3, 7, -5, 5}) set
print(obj, type(obj))  # int64 <class 'pandas.core.series.Series'>

obj2 = pd.Series([3, 7, -5, 5], index=['a', 'b', 'c', 'd'])
print(obj2, type(obj2))  # int64 <class 'pandas.core.series.Series'>
print(obj2.sum(), sum(obj2), np.sum(obj2))
print(obj2.values)  # [ 3  7 -5  5]
print(obj2.index)

print()
# 인덱싱/ 슬라이싱
print(obj2['a'])  # 값을 리턴
print(obj2[['a']])  # 인덱스 값을 리턴
print(obj2[['a', 'b']])
print(obj2['a':'c'])

print(obj2[2])
print(obj2[1:4])
print(obj2[[2, 1]])
print(obj2 > 0)
print('a' in obj2)


# dict
print('\ndict type : Series 객체로 처리')
names = {'mouse': 5000, 'keyboard': 25000, 'monitor': 550000}
print(names)
obj3 = Series(names)
print(obj3, type(obj3))
obj3.index = ['마우스', '키보드', '모니터']
print(obj3)
print(obj3[0], ' ', obj3['마우스'])

obj3.name = '상품가격'
print(obj3)
print('\nDataFrame : # 모양 - Series가 여러 개 합쳐진 형태')
df = DataFrame(obj3)
print(df, type(df))

data = {
    'irum': ['홍길동', '공기밥', '깁밥', '주먹밥'],
    'juso': ('역삼동', '신당동', '신사동', '신당동'),
    'nai': [23, 25, 26, 35]
}

print(data, type(data))

df2 = pd.DataFrame(data)
print(df2, type(df2))
print(df2['irum'], type(df2['irum']))
print(df2.irum, type(df2.irum))

print()

print(DataFrame(data, columns=['juso', 'irum', 'nai']))  # columns의 순서를 바꿔준다.

print('data에 없는 값을 주면 NaN으로 채워진다.')
df3 = DataFrame(data, columns=['irum', 'juso', 'nai', 'tel'],\
                index=['a', 'b', 'c', 'd'])

print(df3)

df3['tel'] = '111-1111'
print(df3)

tvalue = Series(['222-2222', '333-3333', '444-4444'], index=['b', 'c', 'd'])
df3['tel'] = tvalue
print(df3)

print('전치')
print(df3.T)

print(df3.values)
print(df3.values[0, 1])  # 인덱싱
print(df3.values[0, 2])  # 슬라이싱

print('행 또는 열 삭제')
df4 = df3.drop(['d'])
# df4 = df3.drop(['d'], index=0) 같은 의미이다. 행 삭제
print(df4)

df4 = df3.drop('tel', axis=1)  # 열 삭제
print(df4)

# 정렬
print(df4.sort_index(axis=0, ascending=False))  # 행 단위 
print()
print(df4.sort_index(axis=1, ascending=True))  # nai juso irum : 내림차순)(False),  irum juso  nai : 오름차순(True)
print()

print(df4.rank(axis=0))  # 사전순 순위를 매긴다.
print()

counts = df4['juso'].value_counts()
print('열 값 갯수 : ', counts)

print('문자열 자르기')
data = {
    'juso': ['강남동', '역삼동', '광진구'],
    'inwon': [23, 35, 57]
}
fr = DataFrame(data)
print(fr)

result1 = Series([x.split()[0] for x in fr.juso])
print(result1)
print(result1.value_counts())
result2 = Series((x.split()[1] for x in fr.juso))
print(result2)


