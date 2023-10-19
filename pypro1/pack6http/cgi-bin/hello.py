# 파이썬 파일로 html 문서 반환

a = 10
b = 20
jumsu = a + b
ss1 = '파이썬'
ss2 = '만세'


print('Content-Type:text/html;charset=utf-8\n')  # 브라우저에게 넘기는 데이터 타입 알려주기
print('<html><body>')
print('<b> 안녕하세요 </b> 파이썬 파일로 HTML 문서를 작성 <br/>')
print('점수는 : %d'%(jumsu, ))  # 숫자니까 %d
print('<br>%s %s'%(ss1, ss2))
print('</body></html>')
