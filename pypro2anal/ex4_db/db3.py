# MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글 처리때 음수가 깨지는 것을 방지하기 위해 사용
import seaborn as sns
import sys
try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)

except Exception as e:
    print('연결 오류 :', e)
    sys.exit()

# 사번, 이름, 부서명, 연봉, 직급을 읽어 DataFrame을 작성

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik
        from jikwon j join 
        buser b on b.buser_no=j.buser_num
    """
    cursor.execute(sql)

    # 출력1 : console
    for a, b, c, d, e in cursor:
        print(a, b, c, d, e)
    print()

    # DataFrame 의 자료를 파일로 저장
    df = pd.DataFrame(cursor.fetchall(),
                        columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_pay', 'jikwon_jik'])
    print(df.head(3))
    print()

    # 부서명별 연봉의 합, 연봉의 최대/최소값을 출력

    sql2 = """
        SELECT buser_name AS 부서명, SUM(jikwon_pay) AS 연봉의합, MAX(jikwon_pay) AS 연봉의최대값, MIN(jikwon_pay) AS 연봉의최소값
        FROM jikwon j JOIN buser b ON b.buser_no = j.buser_num GROUP BY buser_name;
    """
    cursor.execute(sql2)
    for a, b, c, d in cursor:
        print(a, b, c, d)
    print()

    # 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
    df3 = pd.read_sql(sql, conn)
    df3.columns = ['사번', '이름', '부서명', '연봉', '직급']
    # print(df3.head(3))
    print()

    # 교차표
    ctab = pd.crosstab(df3['부서명'], df3['직급'], margins=True)
    print(ctab)
    print()

    # 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    sql3 = """
       SELECT jikwon_no, jikwon_name, gogek_tel, COALESCE(gogek_no, '담당 고객 X'),
              COALESCE(gogek_name, '담당 고객 X'), COALESCE(gogek_tel, '담당 고객 X') FROM jikwon j
              LEFT JOIN gogek g ON j.jikwon_no = g.gogek_damsano;
    """
    cursor.execute(sql3)

    for result in cursor:
        jikwon_no, jikwon_name, gogek_tel, gogek_no, gogek_name, gogek_tel = result
        print(jikwon_no, jikwon_name, gogek_tel, gogek_no, gogek_name, gogek_tel)

    # 부서명별 연봉의 평균으로 가로 막대 그래프를 작성

    jik_ypay = df.groupby(['부서명'])['연봉'].mean()
    plt.bar(jik_ypay.index, jik_ypay)
    plt.title('부서명별 연봉의 평균')
    plt.xlabel('부서명')
    plt.ylabel('평균 연봉')
    plt.show()


except Exception as e:
    print("처리 오류 : ", e)


# 문제 2) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
# pivot_table을 사용하여 성별 연봉의 평균을 출력

# 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프

# 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
