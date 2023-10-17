# 에러의 종류
# syntex : 문법 오류
# logic : 프로그램 실행 중에 발생하는 오류로 프로그램이 비정상적으로 종료되는 오류
# expection : 예외란 코드를 실행하는 중에 발생하는 에러. try ~ expect 문 사용


def divide(a, b):
    return a / b

print('뭔가를 하다가...')
'''
c = divide(5, 2)
c = divide(5, 0) #  ZeroDivisionError: division by zero
print(c)
'''

# 양식   try :
#           오류가 발생할 수 있는 구문
#       except Exception as e:
#           오류 발생
#       else:
#           오류가 발생하지 않을 때 만나는 구절
#       finally:
#           무조건 마지막에 실행


try:
    # 에러가 먼저 발생되는 구절이 있으면 밑에 구절에도 에러가 나는 구문이어도 무시가 된다.
    c = divide(5, 2)
    print(c)

    aa = [1, 2]
    print(aa[1])

    f = open(r'c:/work/abc.txt')
    print('계속')
except ZeroDivisionError:
    print('두 번째 숫자는 0을 주지 마세요.')
except IndexError as e:
    print('참조 범위 오류 : ', e)  # e : list index out of range
except Exception as e:
    print('파일을 찾을 수 없습니다. : ', e)  # e : [Errno 2] No such file or directory: 'c:/work/abc.txt'
finally:
    print('에러 유무에 상관없이 반드시 수행된다.')

print('프로그램 종료')