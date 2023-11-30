# tv,radio,newspaper 간의 상관관계를 파악하시오.
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family='malgun gothic')

df=pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv')
print(df)

lamb1 = lambda p:df['tv'].corr(df['radio'])
r1 = lamb1(df)
print('r1 = ',r1)

lamb2 = lambda p:df['tv'].corr(df['newspaper'])
r2 = lamb2(df)
print('r2 = ',r2)

lamb3 = lambda p:df['radio'].corr(df['newspaper'])
r3 = lamb3(df)
print('r3 = ',r3)

print('-----------'*5)
df1 = pd.DataFrame(df, columns=('tv','radio','newspaper'))
print(df1)
print(df1.corr())
sns.heatmap(df1.corr())
plt.show()


