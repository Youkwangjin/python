# pandas로 파일 읽기
import pandas as pd

# df = pd.read_csv('../testdata/ex1.csv')

# 웹을 통해서 읽어오기
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex1.csv')
print(df, type(df))  # <class 'pandas.core.frame.DataFrame'> 파일에서 읽으면 DataFrame
print(df.info())
print('===============================================')
df = pd.read_table('../testdata/ex1.csv', sep=',')
print(df.info())
print('===============================================')
df = pd.read_csv('../testdata/ex2.csv', header=None)
print(df)
print('===============================================')
df = pd.read_csv('../testdata/ex2.csv', header=None, names=['co1', 'col2'])
print(df)
print('===============================================')
# msg가 컬럼이 아닌 index로 들어간다.
df = pd.read_csv('../testdata/ex2.csv', header=None, names=['a', 'b', 'c', 'g', 'msg'], index_col='msg')
print(df)
print('===============================================')
# df = pd.read_csv('../testdata/ex3.txt')

# \s : space 를 표현하는것으로 공백문자를 의미한다.
# \S : non space를 표현하며 공백 문자가 아닌 것을 의미한다.
df = pd.read_table('../testdata/ex3.txt', sep='\s+')  # sep=' '
print(df)
print(df.info())  # 하나의 문자열
print(df.describe())
print('===============================================')
df = pd.read_table('../testdata/ex3.txt', sep='\s+', skiprows=(1, 3))  # skiprows은 특정 행을 제거
print(df)
df = pd.read_fwf('../testdata/data_fwt.txt', widths=(10, 3, 5), header=None, names=('date', 'name', 'price'),encoding='utf-8')
print(df)
print('===============================================')
# 대용량의 자료를 chunk(묶음) 단위로 할당해서 처리 가능
test = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3)
print(test)  # .TextFileReader object (텍스트 파서 각채)

for p in test:
    print(p.sort_values(by=2, ascending=True))  # ascending=True는 오름차순
print('===============================================')
print('\nDataFrame 저장')
items = {'apple': {'count': 10, 'price': 1500}, 'orange': {'count': 5, 'price': 4500}}
df = pd.DataFrame(items)
print(df)
print('===============================================')
# print(df.to_html())
# print((df.to_clipboard()))
# print(df.to_csv())
df.to_csv('test1.csv', sep=',')
df.to_csv('test2.csv', sep=',', index=False)
df.to_csv('test3.csv', sep=',', index=False, header=False)


# pandas 문제 4)
