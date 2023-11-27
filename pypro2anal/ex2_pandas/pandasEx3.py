# pandas 문제 1)
# a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오.
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df1 = pd.DataFrame(np.random.randn(9, 4))
print(df1)

print()

# b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
df1.columns = ['NO1', 'NO2', 'NO3', 'NO4']
print(df1)
print()

# c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
print(df1.mean(axis=0))
print()

# pandas 문제 2)
# a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.
data = {
    'numbers': [10, 20, 30, 40],
}

index = ['a', 'b', 'c', 'd']

df = pd.DataFrame(data, index=index)  # 데이터프레임을 생성할 때 색인을 지정합니다.
print(df)
print()

# b) c row의 값을 가져오시오.
row = df.loc['c']
print(row)
print()

# c) a, d row들의 값을 가져오시오.
rows = df.loc[['a', 'd']]
print(rows)
print()

# d) numbers의 합을 구하시오.
numbers_sum = df['numbers'].sum()
print(numbers_sum)
print()

# e) numbers의 값들을 각각 제곱하시오.
df['numbers'] = df['numbers'] ** 2
print(df)

# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5
df['floats'] = [1.5, 2.5, 3.5, 4.5]
print(df)

# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.

names_data = pd.Series(['길동', '오정', '팔계', '오공'], index=index, name='names')
df['names'] = names_data
print(df)
