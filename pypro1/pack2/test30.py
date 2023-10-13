from pack2.test30etc import ElecProduct

class ElecTv(ElecProduct): # ElecProduct 상속한다
    
    def volumeControl(self, volume): # volumeControl 오버라이드 한다. 왜? 부모에서 쓰기 보다는 자식 함수에서 설정하고 싶어서 
        self.volume += volume
        print('TV 소리 크기는 ' + str(self.volume))

class ElecRadio(ElecProduct):
    
    def showProduct(self):
        print('라디오 고유 메서드')
        
    def volumeControl(self, volume):
        vol = volume
        self.volume += vol
        print('라디오 볼륨은 ' + self.volume)
    
tv = ElecTv()
tv.volumeControl(7)
tv.volumeControl(-3)
print("=" * 100)

radio = ElecTv()
radio.volumeControl(3)
radio.volumeControl(2)
print("=" * 100)

product = tv
product.volumeControl(10)
print("=" * 100)

product = radio
product.volumeControl(10)
