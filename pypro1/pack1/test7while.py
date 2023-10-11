# 반복문 관련
a = 0
while a < 10:
    a += 1
    if a == 5:continue # a 값이 5일 때
    if a == 6:break # 강제 종료는 else 구문을 만나지 않는다.
    print(a)
else:
    print('while 정상 처리')
    
print('while 수행 후 a는 %d'%a)

'''
while 1: # True 
    a = int(input("확인 할 숫자:"))
    if a == 0:
        print('반복수행 종료')
        break
    elif a % 2 == 0:
        print('%d 는 짝수'%a)
    elif a % 2 == 1:
        print('%d 는 홀수'%a)
'''
# 난수 (pseudo random : 의사 난수) - 난수표를 사용
import random
# random.seed(1)
friend =['준수', '예진', '혜정']
print(random.choice(friend))
print(random.sample(friend, k=2))
random.shuffle(friend)
print(friend)

# 컴이 가진 임의의 정수 알아 맞하기
num = random.randint(1, 10)
while True:
    print('1 ~ 10 사이의 컴이 가진 숫자를 예상하세요.')
    su = int(input())
    if num == su:
        print('성공' * 10)
        break
    elif su < num:
        print('더 큰 수를 입력')
    elif su > num:
        print('더 작은 수를 입력')
    
