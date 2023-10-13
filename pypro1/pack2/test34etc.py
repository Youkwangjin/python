from abc import abstractmethod, ABCMeta

# 추상 클래스
class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
        
        
    @abstractmethod
    def pay(self):
        pass
    
    
    @abstractmethod
    def data_print(self):
        pass
    
    
    def irumnai_print(self):
        print("이름 : " + self.irum + ", 나이 : {}".format(self.nai), end=" ")