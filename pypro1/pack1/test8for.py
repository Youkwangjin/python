# 반복문 for
# for target in object: ...

for i in [1,2,3,4,5]: # list 타입
    print(i, end = ' ')

print()

for i in {1,2,3,4,5}: # set 타입(순서가 없다)
    print(i, end = ' ')
    
print()

for i in 1,2,3,4,5: # 튜플 타입 소괄호 생략 가능
    print(i, end = ' ')
    
print()

soft = {'java':'웹용 언어', 'python':'만능 언어', 'js':'웹용스크립트'}
for i in soft.items():
    # print(i) # ('java', '웹용 언어')
    
    print(i[0] + '^^;' + i[1])

for k, v in soft.items():
    print(k)
    print(v)
    print()
    
for bb in soft.keys():
    print(bb, end = ' ')
print()

# numbers = [1,3,5,7,9]
numbers = [-3,4,5,7,12] # 합과 평균은 같지만, 표쥰편차는 다르다.
tot = 0
for a in numbers:
    tot += a
print('합은' + str(tot) + ', 평균은 ' + str((tot / len(numbers))))
print()

li = ['a', 'b', 'c']
for k, d in enumerate(li): # enumerate은 내장 함수
    print(k, d)
print()

# 다중 for문
for n in [2, 3]:
    print('---{}단--'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n, i, n * i), end = ' ')
    print()
print()

datas = [1,2,3,4,5]
for i in datas:
    if i == 2: continue
    if i == 4: break
    print(i, end = ' ')
else:
    print('for 정상 종료')
print()

jumsu = [95, 70, 60, 55, 100] # 70점 이상만 합격 처리
num = 0
for jum in jumsu:
    num += 1;
    if jum < 70:continue
    print('%d번째 합격!'%num)    

print('for + 정규 표현식 연습 ----------')
import re
ss = """
경기 부천 원미경찰서는 영아살해 혐의로 40대 여성 A씨를 긴급체포해 조사 중이라고 10일 밝혔다. ##
A씨는 지난 4일 오후 부천시에 있는 모텔 2층에서 갓 태어난 딸 B양을 창문 밖으로 던져 살해한 혐의를 받는다.
사건 발생 닷새 만인 지난 9일 인근에 사는 주민이 모텔 담벼락 주변에서 숨진 B양을 발견해 112에 신고했다. B양은 침대 시트에 감긴 채 종이 쇼핑백 안에 담겨 있었다.
사건 발생 닷새 만인 지난 9일 인근에 사는 주민이 모텔 담벼락 주변에서 숨진 B양을 발견해 112에 신고했다. B양은 침대 시트에 감긴 채 종이 쇼핑백 안에 담겨 있었다.
"""

print(type(ss))
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(" ")
print(ss3) #['정부는', '일', '국무회의에서', ...

cou = {} # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)
print()
for ss in['111-1234', '일이삼-이이이이', '234-6789']:
    if re.match(r'\d{3,4}-\d{4}$', ss):
        print(ss, '전화번호 맞아요')
    else:
        print(ss, '전화번호 아닌 듯')
print()        
# 리스트 컴프리헨션은 직관적으로 리스트를 생성하는 방법입니다. 
# 대괄호 "[", "]"로 감싸고 내부에 for문과 if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다.

a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li) # [2, 4, 6, 8, 10]
print(list(i for i in a if i % 2 == 0)) # [2, 4, 6, 8, 10]

print()
i1 = [3,4,5]
i2 = [0.5, 1, 2]
result = []
for a in i1:
    for b in i2:
        result.append(a + b)
print(result)
print('-----')

datas = [a + b for a in i1 for b in i2]
print(datas)

print('List Comprension 살펴보기 --------')
temp = [1,2,3]
for i in temp:
    print(i, end = " ")
print()
print([i for i in temp])
print([i for i in temp])
print()

datas = [1,2,'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,3,2,1}
imsi = {i * i for i in datas}
print(imsi)

print()
id_name = {1:'tom',2:"oscar"}
print(id_name)
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a + b)

sum([1,2,3])   
print('과일 값 계산 ----')
price = {'사과':5000, '감':500, '배':1000} # 오늘 과일 가격
guest = {'사과':3, '감':2}
bill = sum(price[f] * guest[f] for f in guest)
print('고객이 구매한 과일 총액은 {}원'.format(bill))

print('------ range 함수 ------- ')
print(list(range(1, 11, 2)))
print(list(range(-10, -100, -20)))
print(set(range(1, 11, 2)))
print(tuple(range(1, 11, 2)))
print()

for i in range(6): # 0 이상 6 미만 증가치 1
    print(i, end = ' ') 
print()
tot = 0
for su in range(1, 11):
    tot += su
print('결과 :' + str(tot))
print('내장 함수 :' + str(sum(range(1, 11))))

for _ in range(6):
    print('돌자')

for i in range(1, 10):
    print('{0}*{1}={2}'.format(2, i, 2 * i))
print("=" * 50) 


  
# 문1 : 2 ~ 5 단 출력
for i in range(2, 6):  
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print()
print("=" * 50)
    
# 문2 : 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합을 출력
result = 0
for i in range(1, 100):
    if i % 3 == 0:
        result += i
    if i % 5 == 0:
        result += i
print(result)
print("=" * 50)
# 문3 : 주사위 두 번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# 1 3
# 2 6
# ...
result = 0
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) % 4 == 0:
            print(str(i) +','+ str(j))       