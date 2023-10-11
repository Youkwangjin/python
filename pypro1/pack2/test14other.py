# 독립적인 실행 보다는 다른 모듈에서 호출된 사용자 정의 모듈
score = 90 # 모듈의 멤버

def listHap(*ar):
    print(ar)
    if __name__=='__main__':
        print("메인 모듈이다.")
    
def kbs():
    print('공영방송')
    
def Mbc():
    print('만나면 좋은 친구 11')

