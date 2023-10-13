# class : 멤버로 변수와 메서드를 포함한 집합체. 객체 중심의 독립적인 프로그랭이 가능함 (OOP 객체지향 프로그램 구현)

class Car: 
    handle = 0 # 멤버변수 ( 공유멤버)
    speed = 0
    
    def __init__(self, name, speed): # 생성자
        self.name = name
        self.speed = speed
    
    def showData(self): # self 주소 
        km = '킬로미터'
        msg = '속도 : '+ str(self.speed) + km
        return msg

print(Car.handle)
# Car.showData()

car1 = Car('tom', 80) # self, name, speed
print('car1 :', car1.handle, car1.name, car1.speed) # 0 tom 80
car1.color = '보라색' # car1 새로운 멤버가 들어간다. car1 객체에 color 멤버(변수)가 추가가 된다.
print('car1 :', car1.color)  
print("=" * 50)

car2 = Car('광진', 100)
print('car2 :', car2.handle, car2.name, car2.speed) # 0 광진 100 handle은 원형 클래스의 공유멤버에서 찾는다.
print("=" * 50)

print(Car.handle, car1.handle, car2.handle) # 0 0 0
print(Car.speed, car1.speed, car2.speed)    # 0 80 100
# print(car1.color) 멤버가 없기 때문에 err
# print(car2.color) 멤버가 없기 때문에 err
print(Car, car1, car2)
print(id(Car), id(car1), id(car2)) # 3개의 객체(인스턴스)이기 때문에 당연히 주소도 다르다.
print(car1.__dict__) # 객체의 멤버를 확인한다.
print(car2.__dict__)
print("=" * 50)

# 메서드
print('car1 :', car1.showData()) # Bound method call
print('car2 :', car2.showData()) # Bound method call
print("=" * 50)

car1.speed = 55
car2.speed = 88
print('car1 :', car1.showData()) # Bound method call
print('car2 :', car2.showData()) # Bound method call
print("=" * 50)

Car.handle = 1
print('car1 :', car1.handle, car1.name, car1.speed) # car1 : 1 tom 55
print('car2 :', car2.handle, car2.name, car2.speed) # car2 : 1 광진 88
  




