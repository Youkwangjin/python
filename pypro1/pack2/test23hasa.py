# 클래스의 포함관계 : 구긴이네 냉장고(객체)에 음식(객체) 넣기

class Fridge:
    isOpened = False  # 냉장고 문 개방, 폐쇄 여부
    foods = []        # 음식물 담기용 리스트
    
    def open(self):
        self.isOpened = True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing) # 포함관계
            print('냉장고 속에 음식 담기 완료')
            self.list()
        else:
            print('냉장고 문이 닫혀서 음식을 꺼낼수 없어요')
    
    def close(self):
        self.isOpened = False
        print('냉장고 문 꼭 닫기')
    
    def list(self):
        for f in self.foods:
            print('-', f.name, f.expiry_date)
        # print()
    
    
# 냉장고에 담기는 음식물 클래스
class FoodData:
    def __init__(self, name, expiry_date):    # 음식이름, 유통기한
        self.name = name
        self.expiry_date = expiry_date
        
# 실행
fr = Fridge()
apple = FoodData('사과', '2023-11-05')
fr.put(apple) 

print("=" * 50)

fr.open()
fr.put(apple)
fr.close()

print("=" * 50)

cola = FoodData('콜라', '2025-10-05')        
fr.open()
fr.put(cola)
fr.close()        
        
        
        
        
        
        
        
        
        

