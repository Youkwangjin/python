# 원격 database(MariaDB)와 연동
# sangpum 자료 출력

import MySQLdb

'''
conn = MySQLdb.connect(host='127.0.0.1', user='root', password='seoho123', database='test')
print(conn)  # <_mysql.connection open to '127.0.0.1' at 000001CD07421990>
conn.close
'''

# 별도의 dict 타입으로 만들었다.
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'seoho123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

try:
    conn = MySQLdb.connect(**config)  # 원격 DB 연결 객체
    print(conn)  # <_mysql.connection open to '127.0.0.1' at 000001CD07421990>
    cursor = conn.cursor()  # SQL문 실행 및 select의 결과 기억

    '''
    # 자료 추가 (Auto Commit 아니다.)
    # sql = "insert into sangdata values (6, '신상1', 5, 5000)"
    sql = "insert into sangdata values (%s, %s, %s, %s)"
    sql_data = (6, '신상1', 5, 5000)
    # sql_data = 6, '신상1', 5, 5000  turple 이니 ( ) 생략이 가능하다.
    cursor.execute(sql, sql_data)  # sql 문장 실행
    # result = cursor.execute(sql, sql_data)
    conn.commit()  # 이거 적어주지 않으면 Auto Commit 이 되지 않는다.
    '''

    # 자료 수정
    '''
    sql = 'update sangdata set sang=%s, su=%s, dan=%s where code=%s'
    sql_data = ('python', 12, 50000, 6)
    result = cursor.execute(sql, sql_data)
    print(result)
    conn.commit()
    '''

    # 자료 삭제
    code = 6
    # sql = "delete from sangdata where code=" + code   이 방법은 권장하지 않는다. : secure coding 가이드라인에 위배된다.
    
    # 권장방법 1
    # sql = "delete from sangdata where code=%s" 
    # count = cursor.execute(sql, code) 

    # 권장방법 2
    sql = "delete from sangdata where code='{0}'".format(code)
    count = cursor.execute(sql)
    if count != 0:
        print('삭제 성공')
        conn.commit()
    else:
        print('삭제 실패')

    # 자료 읽기
    sql = 'select code,sang,su,dan from sangdata'
    cursor.execute(sql)

    # 출력하는 방법 1
    for data in cursor.fetchall():
        print('%s %s %s %s'%data)

    print()

    # 출력하는 방법 2
    for r in cursor:
        # print(r)
        print(r[0], r[1], r[2], r[3])

    print()

    # 출력하는 방법 3
    for (code, sang, su, dan) in cursor:
        print(code, sang, su, dan)

    print()

    # 출력하는 방법 3 - 1
    for a, kbs, su, 단가 in cursor:
        print(a, kbs, su, 단가)

except Exception as err:
    print('에러 : ', err)
    conn.rollback()
finally:
    # 역순으로 닫는다.
    cursor.close()
    conn.close()