# Thread 클래스 상속

import threading, time, sys

class MyThread(threading.Thread): # 클래스내에서 상속받아 메소드로 처리
    def run(self):
        for i in range(1,11):
            print('id={}-->{}'.format(self.getName(),i))
            time.sleep(0.1)
            
ths = []
for i in range(2):
    th = MyThread()
    th.start()
    ths.append(th)
    
for t in ths:
    t.join()
    