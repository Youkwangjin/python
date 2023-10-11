# 변수의 생존 범위 : global, local
# Local > Enclosing function > global > Builtin
from dask.array.random import choice


player = '국가대표' # 전역변수(모듈의 어디서든 공유 가능)

def funcSports():
    name = '신기루는' # 지역변수(함수 내에서만 유효하다)
    player = '지역대표'
    print(name, player)

funcSports()
print("=" * 50)

a = 1; b = 2; c = 3
print('출력1 -- a:{}, b:{}, c:{}'.format(a,b,c))
def outerfunc():
    a = 4
    b = 5   
    def innerfunc():
        global c     # 사용빈도가 높다.
        nonlocal b   # 사용빈도가 낮다.
        # c = 6
        print('출력2 -- a:{}, b:{}, c:{}'.format(a,b,c))
        c = 6 # global으로 선언했기 때문에 지금부터 전역변수이다.
        b = 7
    innerfunc()
    print('출력3 -- a:{}, b:{}, c:{}'.format(a,b,c))
    
outerfunc()
print('출력4 -- a:{}, b:{}, c:{}'.format(a,b,c))
print("=" * 50)

# 인수와 매게변수 키워드 매칭 
def ShowGugu(start, end=5): # parameter에 초기치를 줄 수도 있다.
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력', end = " ")
    print()
    
ShowGugu(2, 3) # 위치 매개변수
ShowGugu(2)    # 기본값 매게변수
ShowGugu(start=2, end=3) # 초기치가 5였지만 인수에 선언해주면 파라미터값에 부여한 값은 무시하게된다. (키워드 매게변수)
ShowGugu(end=3, start=2)
ShowGugu(2, end=4)
# ShowGugu(start=2, 3) SyntaxError: positional argument follows keyword argument
# ShowGugu(end=3, 2)   SyntaxError: positional argument follows keyword argument
print("=" * 50)

# 가변 매게변수 : 인수의 갯수가 동적
*a, b = [1,2,3,4,5]
def fu1(*ar): # parameter에 pack연산을 줄 수도 있다.
    print(ar)
    for a in ar:
        print('밥: ' + a)
        
fu1('공기밥', '주먹밥')
fu1('공기밥', '주먹밥', '돈까스')

def fu2(bap, *ar): # parameter에 pack연산을 줄 수도 있다.
# def fu2(*ar, bap): 에러발생
    print(bap)
    print(ar)
    for a in ar:
        print('밥: ' + a)
        
fu2('공기밥', '주먹밥')
fu2('공기밥', '주먹밥', '돈까스')
print("=" * 50)

def selectCalc(choice, *ar):
    if choice == '+':
        imsi = 0
        for i in ar:
            imsi += i
        return imsi
    elif choice == '*':
        imsi = 1
        for i in ar:
            imsi *= i
        return imsi 
print(selectCalc('+', 1,2,3,4,5)) # tuple 자료를 넘긴다.
print(selectCalc('*', 1,2,3,4,5))
print("=" * 50)

# dict를 인수로 전달
def fu3(w, h, **etc):
    print('몸무게:{}, 키:{}'.format(w, h))
    print(etc)
    
fu3(66, 177, name = '홍길동')
fu3(77, 178, name = '고길동', age = 22)
print("=" * 50)

def fuFinal(a,b,*c,**d):
    print(a, ' ', b) # 1   2
    print(c)         # ()
    print(d)         # {}
    
fuFinal(1, 2)                            
fuFinal(1, 2, 3, 4, 5)                   
fuFinal(1, 2, 3, 4, 5, m = 6, n = 7)    
                                                   





