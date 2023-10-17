# Network
# socket : 네트워크를 위한 통신 채널을 지원
import socket

print(socket.getservbyname('http', 'tcp'))    # 80
print(socket.getservbyname('https', 'tcp'))   # 443
print(socket.getservbyname('telnet', 'tcp'))
print(socket.getservbyname('ftp', 'tcp'))
print(socket.getservbyname('smtp', 'tcp')) # 메일 송수신 프로토콜
print(socket.getservbyname('pop3', 'tcp')) # 메일 수신 프로토콜

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# 223.130.200.107 / # 223.130.195.200