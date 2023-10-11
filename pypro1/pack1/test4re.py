# 정규 표현식
import re

ss = "1234 abc 가나다 abc ABC_123555_6 python is best"
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r'가나', ss))

print(re.findall(r'[1,2,5]', ss))
print(re.findall(r'[1,2,5]+', ss))   # 반복 관련 메타 문자 + : 1회 이상
print(re.findall(r'[0-9]+', ss))     # 숫자 형태의 문자열만 출력한다. 문자 집합 []
print(re.findall(r'\d+', ss))        # 특수문자 \d  \D
print(re.findall(r'[^0-9]{2}', ss))  # 문자 집합[^] 부정
print(re.findall(r'[0-9]{2,3}', ss)) # 공백은 허용되지 않는다. EX) {2, 3} 오류!
print(re.findall(r'[가-힣]+', ss))     
print(re.findall(r'[가-힣,a-z,A-Z]+', ss))
print(re.findall(r'^1234', ss)) # 1234부터 문자열 시작
print(re.findall(r'^만세$', ss)) # 문자열 끝
print("=" * 50)

ss = '''
<a href="abc1.html">abc1</a> # 주석이면서 문자열로 취급한다.
<a href="abc2.html">abc2</a>
<a href="abc3.html">abc3</a>
'''
print(ss)
result = re.findall(r'href="(.*)"', ss)
print(result)
print()
p = re.compile('the', re.IGNORECASE) # flag 사용하기
print(p.findall('The dog the dog'))  # the만 출력이 된다.

s = """My name is kwangjin.
l am happy"""
print(s)
p = re.compile('^.+', re.MULTILINE)  # flag 사용하기
print(p.findall(s))