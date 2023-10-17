# 멀티 채팅 프로그램 : socket, thread 사용
# 서버

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.39', 5555))
ss.listen(5) # 동시 접속자 수
print('채팅 서버 서비스 중...')
users = []

def chatUser(conn):
    name = conn.recv(1024)
    data = '여어 히사시부리이 ' + name.decode('utf-8') + ' 님이 접속했습니다'
    print(data)
    
    try:
        for u in users:
            u.send(data.encode("utf-8"))
            
            # 채팅수행
            while True:
                msg = conn.recv(1024)
                if not msg:continue
                cdata = name.decode('utf-8') + '님의 메세지 : ' + msg.decode('utf-8')
                print('수신 자료 : ', cdata)
                for u in users:
                    u.send(cdata.encode('utf-8'))
    
    except:
        users.remove(conn)
        data = 'ㅠㅠ' + name.decode('utf-8') + ' 님이 퇴장했습니다'
        print(data)
        if users:
            for u in users:
                u.send(data.encode('utf-8'))
        else:
            print('exit')    
    
while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=chatUser, args=(conn,))
    th.start()
