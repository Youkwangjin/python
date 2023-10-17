# 파일 입출력
# 키보드로 출력할때는 input

import os
print(os.getcwd())  # 현재 모듈의 경로명을 보여준다.  C:\work\git_python\python\pypro1\pack3

try:
   print('파일 읽기')
# mode='r', w, a, t  => read, write, append
# f1 = open(r'C:\work\git_python\python\pypro1\pack3\test37.txt', mode='r', encoding='utf-8')
# f1 = open(os.getcwd() + r'\test37.txt', mode='r', encoding='utf-8')

# 같은 경로에 있을경우
   f1 = open(r'test37.txt', mode='r', encoding='utf-8')
   print(f1)  # 파일 객체 확인
   print(f1.read())
   f1.close() # 꼭 닫아주자

   print('*** 파일 저장 ***')
   f2 = open(r'test37.txt', mode='w', encoding='utf-8')
   f2.write('나의 친구들\n')
   f2.write('홍길동, 한국인\n')
   f2.close()
   print('저장 성공')

   print('*** 파일 추가 ***')
   f2 = open(r'test37.txt', mode='a', encoding='utf-8')
   f2.write('손오공\n')
   f2.write('홍길동\n')
   f2.write('유광진\n')
   f2.close()
   print('추가 성공')

   print('*** 저장된 파일 읽기 ***')
   f3 = open(r'test37.txt', mode='r', encoding='utf-8')
   print(f3.readline())
   print(f3.readline(1), f3.readline(2)) # 한 행의 부분 문자 읽기
   lines = f3.readlines()
   print(lines)  # [', 한국인\n', '손오공\n', '홍길동\n', '유광진\n'] 모든 행을 읽어 list 타입으로 저장
   f3.close()

except Exception as e:
    print('파일 처리 에러 : ', e)
