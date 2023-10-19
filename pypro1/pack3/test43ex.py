# jikwon 테이블 대상으로 사번과 이름을 입력 (로그인)해 해당 자료가 있다면
# 해당 직원이 근무하는 부서 직원을 직급별 오름차순으로 모두 출력 직급이 같으면 이름별 오름차순 출력
# 출력 형태 : 사번, 이름, 부서명, 직급
#             5  홍길동  대리   남
#             인원수 : *명


# 다음으로 해당 직원이 관리하는 고객자료 출력
# 출력형태 : 고객번호  고객명   고객전화   나이
#             3     신기해  111-1111   23
#             관리 고객수 : *명


import MySQLdb

import pickle
with open(r'mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chubal():
    try:
        conn = MySQLdb.connect(**config)  # 원격 DB 연결 객체
        cursor = conn.cursor()
        jikwon_no = input('사번 : ')
        jikwon_name = input('이름 : ')
        sql = """
            SELECT jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen
            FROM jikwon
            WHERE buser_num = (
                SELECT buser_num
                FROM jikwon
                WHERE jikwon_no = {0} AND jikwon_name = '{1}'
            )
            ORDER BY jikwon_jik ASC, jikwon_name ASC
            """.format(jikwon_no, jikwon_name)

        cursor.execute(sql)
        # print(sql)
        cursor.execute(sql)
        datas = cursor.fetchall()
        # print(datas)
        '''
        print(len(datas))

        if len(datas) == 0:
            print('해당 정보를 찾을 수 없습니다.')
            return
        '''
        
        # 리스트 형태로 바꾸기
        for jikwon_no, jikwon_name, buser_num, jikwon_jik,  jikwon_gen in datas:
            print(jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen)

        print('인원수 : ' + str(len(datas)))

        print()

        sql2 = """
            SELECT gogek_no, gogek_name, gogek_tel, TIMESTAMPDIFF(YEAR, DATE_FORMAT(SUBSTR(gogek_jumin, 1, 6),"%Y%m%d"), NOW()) AS age
            FROM gogek 
            INNER JOIN jikwon ON jikwon.jikwon_no = gogek.gogek_damsano
            WHERE jikwon_no={0} and jikwon_name='{1}'
        """.format(jikwon_no, jikwon_name)

        cursor.execute(sql2)
        # print(sql)
        cursor.execute(sql2)
        datas2 = cursor.fetchall()

        for gogek_no, gogek_name, gogek_tel, age in datas2:
            print(gogek_no, gogek_name, gogek_tel, age)

        print('인원수 : ' + str(len(datas2)))

    except Exception as e:
        print('err : ' + str(e))

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    chubal()