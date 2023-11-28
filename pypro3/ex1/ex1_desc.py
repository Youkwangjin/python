# 기술 통계 분석

import pandas as pd

frame = pd.read_csv("../testdata/ex_studentlist.csv")
print(frame.head(3))
print(frame['age'].mean())  # 평균
print(frame['age'].var())  # 분산
print(frame['age'].std())  # 표준편차
print(frame.describe())
print(frame['bloodtype'].nunique())
# 평균, 븐산, 빈도수, 변수 간의 상관관계 ... 적당한 해석 달기


# 도수분포표 만들기 : bloodtype
data1 = frame.groupby(['bloodtype'])['bloodtype'].count()
print(data1)  # 혈액형 별 인원 수 확인하기

data2 = pd.crosstab(index=frame['bloodtype'], columns='count')
print(data2)  # 혈액형 별 인원 수 확인하기

data3 = pd.crosstab(index=frame['bloodtype'], columns=frame['sex'])
print(data3)  # 성별, 혈액형 별 인원 수 확인하기

data4 = pd.crosstab(index=frame['bloodtype'], columns=frame['sex'], margins=True)
print(data4)  # 성별, 혈액형 별 인원 수  및 소개

print(data4 / data4.loc['All', 'All'])  # 행, 열 비율 구하기

# 깔끔한 해설, 시각화
