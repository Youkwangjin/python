# test40su.txt 파일을 한 행 씩 읽어 각 행의 숫자의 합을 출력하시오

try:
    print('파일 읽기')
    f1 = open(r'test40su.txt', mode='r')
    print(f1.read())
    f1.close()

    print("=" * 50)

    print('각 행의 숫자의 합 구하기')
    with open(r'test40su.txt', mode='r', encoding='utf-8') as su:
        line = su.readline()
        while line:
            lines = line.split()
            # lines = line.split(chr(9))
            hap = sum([float(i) for i in line.split()])
            print("각 행의 숫자 합:", hap)
            line = su.readline()
except Exception as e:
    print('파일 처리 에러 : ', e)