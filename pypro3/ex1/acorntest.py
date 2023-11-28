import numpy as np
import pandas as pd
print('------------문제 1 -----------------')
data = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])


print(data[::-1, ::-1])
print('------------문제 2 -----------------')
# [문항2] titanic dataset으로 성별(sex)과 좌석등급(class) 별 생존율을 출력하기 위한 pivot_table 함수를 사용하시오.
# 출력결과는 아래와 같다. (배점:5)[문항2] titanic dataset으로 성별(sex)과 좌석등급(class) 별 생존율을 출력하기 위한 pivot_table 함수를 사용하시오.
# 출력결과는 아래와 같다. (배점:5)

import seaborn as sns

titanic = sns.load_dataset('titanic')

result = titanic.pivot_table(index='sex', columns='class', values='survived', aggfunc='mean')

print(result)
print('------------문제 3 -----------------')
# [문항3] sqlite DB를 사용하여 DataFrame의 자료를 db에 저장하려 한다.
# 아래의 빈칸에 알맞은 코드를 적으시오.
#
# 조건 : index는 저장에서 제외한다. (배점:5)
# data = {
#     'product':['아메리카노','카페라떼','카페모카'],
#     'maker':['스벅','이디아','엔젤리너스'],
#     'price':[5000,5500,6000]
# }
#
# df = pd.DataFrame(data)
# df.①__________('test', conn, if_exists='append', ②________________)

data = {
    'product': ['아메리카노', '카페라떼', '카페모카'],
    'maker': ['스벅', '이디아', '엔젤리너스'],
    'price': [5000, 5500, 6000]
    }

df = pd.DataFrame(data)
print(df)
print('------------문제 4 -----------------')
# [문항4] DataFrame의 결과가 아래와 같이 출력 되었다. 밑줄과 [ ] 안에 필요한 코드를 작성하시오.
#
# 강남 강북 서초
# 1월 0 1 2
# 2월 3 4 5
# 3월 6 7 8
# 4월 9 10 11 (배점:5)
# DataFrame(np.arange(12).reshape((__, __)), _______=[              ],  _______ = [            ])'

data = np.arange(12).reshape((4, 3))
months = ['1월', '2월', '3월', '4월']
columns = ['강남', '강북', '서초']

df = pd.DataFrame(data, columns=columns, index=months)
print(df)



print('------------문제 7 -----------------')

from pandas import DataFrame
frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']},
                  index=['a','b', 'c','d'])

print(frame.T)
frame2 = frame.drop('d')
print(frame2)


print('------------문제 9 -----------------')
data = {
    'juso': ['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon': [23, 25, 15]
}
df = pd.DataFrame(data)

# juso 칼럼 값을 공백을 기준으로 분할하고 0번째 요소를 Series로 가져오기
results = pd.Series([x.split()[0] for x in df['juso']])
print(results)


print('------------문제 10 -----------------')
x = np.array([1, 2, 3, 4, 5])  # 1차원 배열
y = np.array([1, 2, 3]).reshape(3, 1)  # 2차원 배열 (3행 1열)

result = x + y  # 더하기 연산

print(result)

print('------------문제 12 -----------------')
df = pd.DataFrame([[1.4, np.nan], [7, 4.5], [np.NaN, np.NaN], [0.5, -1]])

result = df.dropna()
print(result)




print('------------문제 13 -----------------')
data = {"a": [80, 90, 70, 30], "b": [90, 70, 60, 40], "c": [90, 60, 80, 70]}

# 칼럼(열)의 이름을 순서대로 "국어", "영어", "수학"으로 변경
data2 = {"국어": [80, 90, 70, 30], "영어": [90, 70, 60, 40], "수학": [90, 60, 80, 70]}
df = DataFrame(data2, columns=["국어", "영어", "수학"], index=["학생1", "학생2", "학생3", "학생4"])

print(df)

# 1) 모든 학생의 수학 점수 출력
math_jumsu = df["수학"]
print(" 모든 학생의 수학 점수를 출력하기 ")
print(math_jumsu)
print()

# 2) 모든 학생의 수학 점수의 표준편차 출력
math_student = df["수학"].std()
print("모든 학생의 수학 점수의 표준편차 : ", math_student)
print()

# 3) 모든 학생의 국어와 영어 점수를 DataFrame type으로 출력
korean_english_jumsu = df[["국어", "영어"]]
print(" 모든 학생의 국어와 영어 점수 : ")
print(korean_english_jumsu)
