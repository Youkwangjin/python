print('재귀함수(recursive function) : 함수가 자기자신을 호출 -- 반복처리에 사용')
def countDown(su):
        if su == 0:
            print('완료')
        else:
            print(su,end=' ')
            countDown(su-1) # 재귀
            
countDown(5)

print('1~10 까지의 정수의 합')
def funcHap(n):
    if n == 1:
        print('탈출')
        return True
    return n + funcHap(n-1)

result = funcHap(10)
print('10 까지의 정수의 합 : ',result)

print('계승(factorial) 처리를 위한 함수')
def myFact(a):
    if a ==1: return 1
    print(a)
    return a * myFact(a-1)

print('5!은 ',myFact(5))