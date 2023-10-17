from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 6666))
clientsock.send('안녕 반가워'.encode(encoding='utf-8'))  # 안녕반가워는 ? 시퀀스 바이너리 형태로 바뀐다?
re_msg=clientsock.recv(1024).decode()
print('수신 자료 : ' + re_msg)
clientsock.close()