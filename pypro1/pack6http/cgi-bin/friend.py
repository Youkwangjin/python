# 클라이언트가 전송한 정보 받기 (POST 방식)

import cgi

form = cgi.FieldStorage()  # dict 형식으로 결과를 받는다. [key, value]

name = form["name"].value
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')  # 브라우저에게 넘기는 데이터 타입 알려주기
print('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>my</title>
</head>
<body>
친구 이름은 {0}, 전화번호는 {1}, 성별은 {2}
</body>
</html>
'''.format(name, phone, gen))