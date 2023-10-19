# 1.답 : 1) list, 2) tuple

# 2.답 : 지금 현재 set type으로 지정했기 때문에 set type은 순서가 없고 수정이 불가하다. 또한 중복이 불가능하다.

# 3.답 :
# 반복문 for를 사용 : 1 ~ 100 사이의 숫자 중 3의 배수 또는 4의 배수 이고 7의 배수가 아닌 수를 출력하고 건수와 합도 출력하는 코드를 작성하시오.
'''
cont = 0
rs = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 7 != 0:
        cont += 1
        rs += i
    elif i % 4 == 0 and i % 7 != 0:
        cont += 1
        rs += i

print("조건에 맞는 숫자의 건수:", cont)
print("조건에 맞는 숫자의 합:", rs)
'''
# 4번 답: if 조건문, while 반복문, for 반복문, range()함수 이용, format()

# 5번 답: /은 나누기로 나온 결과값을 소수점까지 출력한다. //은 정수 나눗셈을 하는 연산자로 소수점 아래를 버리고 정수값만 보여준다. %는 나눗셈의 나머지를 반환한다.

# 6번 답: global c, nonlocal b

# 7번 답: * 연산자의 기능은 리스트나 튜플 등에서 언패킹(Unpacking)을 수행할 때 사용됩니다. 예를 들어, * 연산자를 사용하여 리스트 또는 튜플의 요소를 개별 변수에 할당할 수 있습니다.
'''
*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1)
print(v2)
print(v3)
'''
# 8번 답: Hap = lambda m, n: m + n * 5

# 9번 답: 간격 (step): 2 이 파라미터는 숫자들 사이의 간격을 말한다. 2로 설정되어 있으므로, 생성된 숫자들 간의 간격이 2 따라서 결과적으로 1부터 6 직전까지의 숫자 중에서 2씩 증가하는 숫자들이 출력된다.

# 10번 답:
'''
try:
    aa = int(input('숫자를 입력하세요'))
    bb = 10 // aa
    print(bb)
except Exception as e:
    if aa == 0:
        print('0 이 아닌 다른 숫자를 입력하세요 : ', e)
finally:
    pass
'''
# 11번 답:

'''
i = 10
while i > 0:
    j = '*'  *  i
    print("{:>10}".format(j))
    i = i - 1
'''

# 12번 답:
'''
i = int(input("연도 입력: "))

if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
    print('{0}년은 윤년'.format(i))
else:
    print('{0}년은 평년'.format(i))
'''
# 13번 답:
'''
i = 0

while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 101:
        break
    print(i, end=' ')
    i += 1
'''

