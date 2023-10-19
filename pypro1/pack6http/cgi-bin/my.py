# 클라이언트가 전송한 정보 받기 (GET 방식)

import cgi

# GET 방식
form = cgi.FieldStorage()
irum = form['name'].value + '님'
nai = form['age'].value + '살'

print('Content-Type:text/html;charset=utf-8\n')  # 브라우저에게 넘기는 데이터 타입 알려주기
print('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>my</title>
</head>
<body>
이름은 {0}, 나이는 {1}
</body>
</html>
'''.format(irum, nai))