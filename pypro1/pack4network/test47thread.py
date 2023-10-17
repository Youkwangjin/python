# process 실행
from subprocess import *

# Popen('calc.exe') # 응용 프로그램 실행
# call('calc.exe')
# print('계속')
# print('종료')

# Thread(light weight process라고도 함) 처리
# 스레드간 자원 공유? 멀티태스크 가능하게 함
# 시작, 실행, 종료의 세 단계로 구성됨
import threading, time

def run(id):
    for i in range(1, 11):
        print('id:{}---->{}'.format(id, i))
        time.sleep(0.5)
# 사용자 정의 thread를 사용하지 않은 경우 : 순차적으로 실행 됨
   
# run(1)
# run(2)
# print('프로그램 종료(메인 모듈은 메인 스레드에 의해 실행')

# 사용자 정의 thread를 사용한 경우 : 비 순차적으로 실행 됨
th1 = threading.Thread(target=run, args=('일'))  # 스레딩 모듈의 스레드 클래스를 사용 > 자바에서는 추상메소드 런을 갖고있지만 파이썬은 타게팅..
th2 = threading.Thread(target=run, args=('이'))
th1.start()
th2.start()

th1.join()  # 해당 스레드가 진행 되는 동안 메인 스레드는 대기 요청
th2.join()
print('프로그램 종료(메인 모듈은 자동으로 지원된 메인 스레드에 의해 실행')