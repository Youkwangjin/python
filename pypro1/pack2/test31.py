# 다중 상속 연습

class Animal:
    def move(self):
        pass
    
    
class Dog(Animal):
    name = '구름이'
    
    def move(self):
        print('구름이는 두 달에 한 번씩 미용실에 간다.')
        
    
class Cat(Animal):
    name = '야옹이'
    
    def move(self):
        print('야옹이는 한 달에 한 번씩 pc방에 간다.')
        print('밤에 눈빛이 빛난다.')

class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('난 여우라고 해')
    
    def foxMethod(self):
        print('여우 고유 메서드')
    
dog = Dog()
print(dog.name)
dog.move()
print("=" * 50)

cat = Cat()
print(cat.name)
cat.move()
print("=" * 50)    

wolf = Wolf()
print(wolf.name)
wolf.move()
print("=" * 50)

fox = Fox()
print(fox.name)
fox.move()
fox.foxMethod()
print("=" * 50)

print(Wolf.__mro__) # 클래스 탐색 순서 : (<class '__main__.Wolf'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
print(Fox.__mro__)
print("=" * 50)

sbs = wolf
sbs.move()
print("=" * 50)

sbs = fox
sbs.move()
print("=" * 50)

animals = (dog, cat, wolf, fox)
for a in animals:
    a.move()
    print()






    
