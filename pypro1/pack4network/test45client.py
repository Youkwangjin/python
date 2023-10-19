# 단순 클라이언트 
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888))
clientsock.send('안녕 반가워'.encode(encoding='utf-8', errors='strict'))  # 안녕 반가워는 ? 시퀀스 바이너리 형태로 바뀐다?
clientsock.close()