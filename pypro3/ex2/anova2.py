
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.

kind = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
quantity = [64, 72, 68, 77, 56, 0, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]

df1 = pd.DataFrame(kind)
df2 = pd.DataFrame(quantity)
df2.iloc[5, 0] = np.nan

df = pd.concat([df1, df2], axis = 1)
df.columns = ['기름종류', '흡수량']
df['흡수량'] = df['흡수량'].fillna(df['흡수량'].mean())
df = df.astype('int')
print(df)

result = df[['기름종류', '흡수량']]
m1 = result[result['기름종류'] == 1]
m2 = result[result['기름종류'] == 2]
m3 = result[result['기름종류'] == 3]
m4 = result[result['기름종류'] == 4]

gr1 = m1['흡수량']
gr2 = m2['흡수량']
gr3 = m3['흡수량']
gr4 = m4['흡수량']

# 한 개의 표본이 같은 분포를 따르는지 정규성 확인
print(stats.shapiro(gr1).pvalue)  # 0.8671070337295532 > 0.05 이르로 정규성 만족
print(stats.shapiro(gr2).pvalue)  # 0.5923926830291748 > 0.05 이르로 정규성 만족
print(stats.shapiro(gr3).pvalue)  # 0.48601073026657104 > 0.05 이르로 정규성 만족
print(stats.shapiro(gr4).pvalue)  # 0.4162167012691498 > 0.05 이르로 정규성 만족

print()
# 두 개의 표본이 같은 분포를 따르는지 정규성 확인
print(stats.ks_2samp(gr1, gr2).pvalue)  # 0.9307359307359307 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr1, gr3).pvalue)  # 0.9238095238095237 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr1, gr4).pvalue)  # 0.5523809523809524 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr2, gr3).pvalue)  # 0.9238095238095237 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr2, gr4).pvalue)  # 0.5523809523809524 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr3, gr4).pvalue)  # 0.7714285714285716 > 0.05 이므로 정규성 만족

print()
# 등분산성 : 만족하지 않으면 welchi_anova test 사용
print(stats.bartlett(gr1, gr2, gr3, gr4).pvalue)  # 0.1938 > 0.05 이므로 등분산성 만족

# 일원분산분석 방법 : f_oneway()
f_sta, pvalue = stats.f_oneway(gr1, gr2, gr3, gr4)
print('f통계량 : ', f_sta)   # 0.27241
print('유의확률 : ', pvalue)  # 0.84438 > 0.05이므로 귀무 가설 기각 실패
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이는 없다.




# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

# 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 없다.
# 대립 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있다.

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
    select buser_name, jikwon_pay from jikwon
    JOIN buser ON buser_num = buser_no
    """
    cursor.execute(sql)
    datas = pd.read_sql(sql, conn)

    df = pd.DataFrame(datas)
    df.columns = '부서명', '연봉'
    df.index = range(1, 31)
    # print(df.head(2))
    # print("부서멸 연봉의 합 : ", df.groupby(['부서명'])['연봉'].sum())
    print("부서별 연봉의 합 : ", df.groupby(['부서명'])['연봉'].mean())

    a = df[df['부서명'] == '총무부']
    a_pay_mean = a.loc[:, '연봉']
    print(a_pay_mean)
    b = df[df['부서명'] == '영업부']
    b_pay_mean = b.loc[:, '연봉']
    print(b_pay_mean)

    print(stats.shapiro(a_pay_mean))  # pvalue=0.02604 < 0.05 이므로 정규성 불만족
    print(stats.shapiro(b_pay_mean))  # pvalue=0.02560 < 0.05 이므로 정규성 불만족

    print(stats.mannwhitneyu(a_pay_mean, b_pay_mean))  # 정규성 만족이 안 될 때 이 방법을 사용한다.
    # statistic=51.0, pvalue=0.47213346080125185


except Exception as e:
    print('err :', e)
finally:
    cursor.close()
    conn.close()

# 해석 : pvalue=0.47213 > 0.05 이므로 귀무 채택. 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.