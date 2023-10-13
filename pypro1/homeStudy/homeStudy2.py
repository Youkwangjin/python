# 튜플 자료형
a1 = ()
print(a1)

a2 = (1,)
print(a2)

a3 = (1, 2, 3)
print(a3)

a4 = 1, 2, 3
print(a4)

a5 = ('a', 'b', ('ab', 'cd'))
print(a5)
print("=" * 50)

# 딕셔너리 자료형 (key:value) 
dic = {'name':'유광진', 'phone': '010-1234-5678', "birth":"1118"}
print(dic)
print("=" * 50)

# 딕셔너리 자료형 삭제하기
dic_a = {'name':'유광진', 'phone': '010-1234-5678', "birth":"1118"}
del dic_a['name']
print(dic_a)
print("=" * 50)

