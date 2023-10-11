# 사용자 정의 모듈 call
print('뭔가를 하다가... 다른 모듈 호출')
# 패키지 안에서만 모듈이 유효하다

import pack2.test14other
print('score : ', pack2.test14other.score)
print(pack2.test14other.__file__) # 파이썬에서 __ 는 키워드이다.  C:\work\git_python\python\pypro1\pack2\test14other.py 경로가 찍힌다.
print(pack2.test14other.__name__) # 모듈명이 찍힌다.
print("=" * 50)

list1 = [1,2]
list2 = [3,4]
pack2.test14other.listHap(list1, list2) # ([1, 2], [3, 4])
print("=" * 50)

# 파이썬은 내가 실행하는 곳이 '메인'이다. 
def abc():
    if __name__=='__main__':
        print("메인 모듈이다.")
abc()

print("=" * 50)

pack2.test14other.kbs()
from pack2.test14other import kbs, Mbc, score
kbs()
Mbc()
print(score)
print("=" * 50)