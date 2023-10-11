# 묶음형 자료 tuple : list와 유사하거나 읽기 전용 (list 보다 처리 속도가 빠르다, 순서가 있고 수정이 불가하다)
t = ('a', 'b', 'c')
print(t, type(t), len(t))
print(type(tuple()))
print(t[0])
# t[0] = 'k' TypeError: 'tuple' object does not support item assignment
li = list(t) # 형 변환
li[0] = 'k'
t = tuple(li) # 튜플은 속도가 빠르기 때문에 사용하는 목적이 많다. 
print(t, type(t))

print("=" * 50)

p = (1, )
print(p, type(p))
print("=" * 50)

# set 타입
# set type : 순서가 없고 수정이 불가하다   *중복 불가 (제일 중요)*
a = {1, 2, 3}
print(a, type(a))
print(type(set()))
# print(a[0]) TypeError: 'set' object is not subscriptable
# a[0] = 10 (인덱싱이 불가하므로 자연스레 수정도 불가하다)
b = {3, 4}
print(a.union(b)) # union은 합집합
print(a.intersection(b)) # intersection 교집합
print(a - b, a | b, a & b) # 차, 합, 교집합
print("=" * 50)

b.update({6, 7}) # 원소 추가
b.update((8, 9)) # 튜플로 원소 추가
b.update([9, 10]) # 리스트로 원소 추가
print(b)

b.discard(7) # 값에 의한 삭제
b.remove(8)  # 값에 의한 삭제 
b.discard(7) # 값에 의한 삭제 - 해당 값이 없으면 통과
# b.remove(8) 값에 의한 삭제 - 해당 값이 없으면 에러
print(b)

li = ['tom', 'oscar', 'tom']
print(li)
s = set(li)
li = list(s)
print(li)
print("=" * 50)

# 딕셔너리 type : key : value 의 형태로 쌍을 이룬다. 순서가 없고 키를 이용해서 값을 조회
mydic = dict(k1 = 1, k2 = '123', k3 = 3.4)
print(mydic, type(mydic)) # {'k1': 1, 'k2': '123', 'k3': 3.4}
dic = {'파이썬':'뱀이당', '자바':'커피', '스프링':'봄', '숫자':[1,2,3]}
print(dic, type(dic), len(dic))
print(dic['자바'])
# print(dic['커피']) key를 가지고 value를 찾기 때문에 value 형태로는 출력할 수 없다.
dic['자바'] = '프로그래밍 언어' # 해당 key로 value을 수정
print(dic)
dic['오라클'] = '예언자' # 추가
print(dic)
del dic['오라클'] # 삭제
dic.pop('숫자')  # 삭제
print(dic)
print(dic.values()) # value 값만 보기