# 단순 웹 서버(GET, HEAD 처리) 구축

from http.server import SimpleHTTPRequestHandler, HTTPServer

# 네트워크에선 특수한 IP 주소로 127.0.0.1이라는 IP 주소가 있다.
# 이는 루프백(loopback) 혹은 로컬호스트 주소(localhost)라고도 불린다.

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', 7777), handler)
print('웹 서버 서비스 시작')
serv.serve_forever()  # 서버 활성화


