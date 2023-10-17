# 서버 서비스 유지

import socket
import sys
HOST = '127.0.0.1'   # HOST를 안적어주면 내 컴퓨터의 IP ADDRESS를 잡아줌
PORT = 6666

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    serversock.listen(5)
    print('서버 서비스 진행 중')
    
    while True:
        conn, addr = serversock.accept()  # 여기서 conn은 소켓을 만들어준다고?
        print('client info : ', addr[0], addr[1])
        # 메세지 수신 후 출력
        print(conn.recv(1024).decode())  # decode는 이진데이터를 메세지로 출력해줌 (암호해독?)
        
        # 메세지 송신
        conn.send(('from server : ' + str(addr[1]) + ' 서버에서 전송함').encode('utf-8'))  # 암호화(바이트코드화)시켜줌

except socket.error as err:
    print('err : ', err)
    sys.exit()
    
finally:
    pass
    
conn.close() # client와 통신하는 socket
serversock.close()