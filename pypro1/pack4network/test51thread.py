# thread의 활성화, 비활성화
import threading

bread_plate = 0 # 빵 접시 : 공유 자원
lock = threading.Condition()  # Lock을 위한 조건변수

class Maker(threading.Thread):
    def run(self):
        global  bread_plate
        for _ in range(30):
            lock.acquire()
            while bread_plate >= 10:
                print('빵 생산 초과로 대기')
                lock.wait()  # 스레드의 비활성화

            bread_plate += 1
            print('빵 생산 수 : ', bread_plate)
            lock.notify()  # 스레드의 활성화
            lock.release()

class Consumer(threading.Thread):
    def run(self):
        global  bread_plate
        for _ in range(30):
            lock.acquire()
            while bread_plate < 1:
                print('빵 기다리는 중')
                lock.wait()  # 스레드의 비활성화

            bread_plate -= 1
            print('빵 소비 후 남은 빵 : ', bread_plate)
            lock.notify()  # 스레드의 활성화
            lock.release()

mak = []; con = []
for i in range(5):
    mak.append(Maker()) # 메이커 생성자 호출 

for i in range(5):
    mak.append(Consumer()) # 컨슈머 생성자 호출

for th1 in mak:
    th1.start()

for th2 in con:
    th2.start()

for th1 in mak:
    th1.join()

for th2 in mak:
    th2.join()

print('프로그램 종료')