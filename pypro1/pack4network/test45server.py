# 단순 서버 : 접속 상태 확인용으로 1개의 접속만 처리

from socket import *
serversock = socket(AF_INET, SOCK_STREAM)  # scoket(소켓종류, 소켓유형)
# AF_INET : 네트워크상에 뭘 찾는 역할?
# SOCK_STREAM : TCP 소켓 통신 유형
serversock.bind(('127.0.0.1', 8888))  # IP주소는 전화번호의 지역번호개념, 포트번호는 나머지 번호 개념?
serversock.listen(1)  # 클라이언트와 동시 연결 정보수 (1 ~ 5)
print('서버 서비스 중')

conn, addr = serversock.accept()  # 연결 대기(Blocking)
print('client addr : ', addr)
print('from client message : ', conn.recv(1024).decode())  # 1kbyte 기본
conn.close()  # client와 통신하는 socket
serversock.close()