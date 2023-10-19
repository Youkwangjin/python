# Network
# socket : 네트워크를 위한 통신 채널을 지원
# 이 모듈은 네트워크 통신을 지원하는 데 사용
import socket

print(socket.getservbyname('http', 'tcp'))  # 'http' 서비스의 TCP 포트 번호를 반환 80
print(socket.getservbyname('https', 'tcp'))  # 'https' 서비스의 TCP 포트 번호를 반환. HTTPS는 보안된 웹 통신을 위한 프로토콜이며, 일반적으로 443번 포트를 사용
print(socket.getservbyname('telnet', 'tcp'))  # 'telnet' 서비스의 TCP 포트 번호를 반환. Telnet은 원격 로그인을 위한 프로토콜이며, 일반적으로 23번 포트를 사용
print(socket.getservbyname('ftp', 'tcp'))
print(socket.getservbyname('smtp', 'tcp'))  # 메일 송수신 프로토콜
print(socket.getservbyname('pop3', 'tcp'))  # 메일 수신 프로토콜

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# 223.130.200.107 / # 223.130.195.200