# if 조건문
money = 2000
if money >= 3000:
    print("택시를 타고 갑니다.")
else:
    print("걸어 갑니다.")
print("=" * 50)

# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도, 카드도 없으면 걸어가는 조건문 
pocket = ['paper', 'phone']
card = True
if 'money' in pocket:
    print("택시를 타고 갑니다.")
else:
    if card:
        print("택시를 타고 갑니다.")
    else:
        print("걸어 갑니다.")
print("=" * 50)

# 나무를 5번 이상 찍었을 때 넘어갑니다 라는 문구를 출력하는 while 조건문
treeHit = 0
while treeHit < 5:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' %treeHit)
    if treeHit == 5:
        print("나무가 넘어갑니다.")
print("=" * 50)

# 커피 while문
coffee = 10
money = 300
while money: # 파이썬은 숫자가 1보다 크면 True라고 판단한다.
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee - 1
    print('남은 커피의 양은 %d개입니다.'%coffee)
    if coffee == 0:
        print("커피가 품절되었습니다. 판매를 중지합니다.")
        break
print("=" * 50)

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: # 짝수이면 continue 만나서 위로 올라간다.
        continue   # pass 는 그냥 지나간다.
    print(a)
print("=" * 50)

# for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
print("=" * 50)

jumsu = [100, 90, 67, 45, 20]

number = 0 # 학생에게 붙여 줄 번호
for mark in jumsu: # 100, 90, 67, 45, 20을 순서대로 mark에 대입한다.
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)
print("=" * 50)

marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다" %number)
print("=" * 50)

# for문에서 범위 지정하기 (range)
add = 0
for i in range(1, 11): # 1이상 11미만
    add = add + i
print(add)
print("=" * 50)

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i * j, end=" ")
    print('')









