str1 = "파이썬"
str2 = "모듈의"
str3 = "멤버"

print('Content-Type:text/html;charset=utf-8\n')  # 브라우저에게 넘기는 데이터 타입 알려주기 (print는 콘솔이 아닌 브라우저에게 넘겨주는것!)
print('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>world</title>
</head>
<body>
<h1>world 문서</h1>
자료 출력 : {0}<br/>
{1} {2}
<hr/>

<img src ='../images/dog.jpg' width='80%' /> <br/>
<a href = '../index.html'>메인으로</a>
</body>
</html>
'''.format(str1, str2, str3))

