# 자료형
# int, float, bool, complex : 객체 값 하나를 참조한다. Immutable 객체
# str, list, tuple, set, dict : 묶음형 객체 값 참조한다. Mutable 객체


# str : 문자열 자료형 : 순서가 있지만(인덱싱, 슬라이싱이 가능하다) 변경은 불가능하다.
s = 'sequence'
# 문자열 관련 함수
print(len(s)) # 8글자
print('포함 횟수 :', s.count('e'))
print('검색 위치 :', s.find('e'), s.find('e', 3), s.rfind('e'))
print("=" * 50)

ss = 'mbc'
print('mbc', ss, id(ss))
ss = 'abc'
print('mbc', ss, id(ss)) # 객체 주소를 바꾼것이다. string은 변경x
print("=" * 50)

print(s, s[0], s[-7]) # 인덱싱
# [ : : ] 이상 : 미만 : 간격
print(s, s[0:5], s[-7:-5], s[5:], s[:5], s[::2], s[:7:3]) # 슬라이싱
print(s[0:5] + 'good')
print("=" * 50)

sss = 'mbc kbs sbs '
print(sss)
print(ss.strip())
print(ss.lstrip())
print(ss.rstrip())

ssss = sss.split(sep = ' ')
print(ssss)
s5 = sss.replace('kbs', '공영방송')
print(s5)
print("=" * 50)
# List 자료형 : 배열과 유사 중복 자료 허용, 여러 종류의 값을 기억할 수 있다. 순서가 있고 변경도 가능하다.
print('List 공부하기')
a = [1, 2, 3]
print(a)
b = [10, a, 12.3, 'good', False]
print(b)
c = list()
print(c)
print("=" * 50)
family = ['준수', '예진', '정혜']
family.append('준호') # 추가
family.insert(0, '민규') # 0번째 데이터 값 추가함으로서 기존의 데이터는 밀려난다.
family.extend(['tom', 'oscar'])
family += ['지원', '국인']
family.remove('tom') # 지우기
# family.clear() 다 날리기
print(family, len(family), family[0])
print("=" * 50)

aa = [1,2,3,['a','b','kbs'],4,5] # 중첩 리스트
print(aa)
print(aa[0])
print(aa[0:3])
print(aa[3])
print(aa[3][2])

aa.remove(2) # 값에 의한 삭제
del aa[3]    # 순서에 의한 삭제
print(aa) 
print("=" * 50)

bb = aa # 주소 치환 : 같은 객체를 참조, 얕은 복사
print(aa, ' ', bb, ' ', id(aa), id(bb))
bb[0] = 'nice'
print(aa, ' ', bb)

import copy
cc = copy.deepcopy(aa) # 주소를 치환 : 새로운 공간이 확보 깊은 복사
print(aa, ' ', cc, ' ', id(aa), id(cc))
print(aa == cc, aa is cc) # True False
cc[0] = '쉬고 할까'
print(aa, ' ', cc )

print('자료구조 : stack, queue')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop() # stack 구조로 LiFO 처리 
print(sbs)
sbs.pop()
print(sbs)
print('\n')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop(0) # queue 구조로 LiFO 처리 
print(sbs)
sbs.pop(0)
print(sbs)