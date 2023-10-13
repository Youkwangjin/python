import pack2.test21singer

def process():
    jungkuk = pack2.test21singer.Singer() # 객체(인스턴스) 생성
    print('타이틀 송 :', jungkuk.title_song)
    jungkuk.sing()
    jungkuk.title_song = '정국 찬양가'
    jungkuk.co = 'Hive'
    print('소속사가 ' + jungkuk.co + "인 가수의 노래" + jungkuk.title_song)
    
    print("=" * 50)
    
    iu = pack2.test21singer.Singer()
    print('타이틀 송 :', iu.title_song)
    iu.sing()
    # print('소속사가 ' + iu.co + "인 가수의 노래" + iu.title_song)
    print(id(pack2.test21singer.Singer), id(iu))     # 1500098319088 1500097104336
    
    print("=" * 50)
    
    bp = pack2.test21singer.Singer
    print(id(pack2.test21singer.Singer), id(bp))     # 1500098319088 1500098319088
    # print(bp.sing()) TypeError: Singer.sing() missing 1 required positional argument: 'self'
    print('타이틀 송 :', bp.title_song)
    
    # iu는 Singer 클래스의 객체를 나타내고 객체의 속성과 메서드를 호출할 수 있지만, 
    # bp는 클래스 자체를 나타내며 객체를 생성하지 않고 클래스의 속성과 메서드에 접근하는 데 사용
    
    
if __name__ == '__main__':
    process()