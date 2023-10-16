# 파이썬의 예외처리 : 오류가 발생하면 어떻게 처리할 것인가에 대한 정의이다.

# 양식   try :
#           오류가 발생할 수 있는 구문
#       except Exception as e:
#           오류 발생
#       else:
#           오류가 발생하지 않을 때 만나는 구절
#       finally:
#           무조건 마지막에 실행

try:
    4 / 0
except ZeroDivisionError as e:
    print('에러 발생')
    
#  try_else 예제

try:
    age = int(input('나이를 입력하세요. '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다!')