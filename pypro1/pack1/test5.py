# 조건 판단문
var = 3
if var >= 5:
    print('크구나')
    print('잠')
else:
    print('거짓')
print('end1')

money = 1000
age = 23

if money >= 500:
    item = 'apple'
    if age <= 30:
        msg = '어리네'
    else:
        msg = '먹었네'
else:
    item = '망고'
    if age >= 20:
        msg = '성인'
    else:
        msg = '아이'
        
print(item, msg)
print('end2')

jumsu = 85
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    print('저조')
print("=" * 50)  

# jum = int(input('점수 입력:'))  기본형은 문자열 타입이기 때문에 int로 형변환 해야한다.
jum = 88
print(jum, type(jum)) 
if 90 <= jum <= 100:
    grade = '우수함'
elif 70 <= jum < 90:
    grade = '보통'
else:
    grade = 'ㅠㅠ'
print('결과' + str(jum) + '점은' + grade)
print("=" * 50)

names = ['홍길동', '김치국', '신기해']
if '홍길동' in names:
    print('내 친구야')
else:
    print('누구니?')
print("=" * 50)

a = 'kbs'
result = 9 if a == 'kbs' else 11
print(result)

a = 11
result2 = 'mbc' if a == 9 else 'kbs'
print(result2)

a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)
print("=" * 50)

print(0 if a < 5 else 1 if a < 10 else 2)
result3 = a * 2 if a > 5 else a + 2
print(result3)



