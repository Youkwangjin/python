from django.shortcuts import render
import MySQLdb 
from pro13exapp.models import Buser, Jikwon, Gogek


config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'seoho123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

def MainFunc(request):
    return render(request, 'index.html')

def BuserShow(request):
    buserdatas = Buser.objects.all()
    return render(request, 'buserlist.html', {'buserdatas':buserdatas})

def JikwonShow(request):
    buser_no = request.GET.get('buser_no')
    
    # buser_no를 정수로 변환
    buser_no = int(buser_no) 
    # 부서 정보 가져오기
    buser = Buser.objects.get(buser_no=buser_no)   
    # 해당 부서에 근무하는 직원들 필터링
    jikwondatas = Jikwon.objects.filter(buser_num=buser_no)  # buser_no를 사용
    
    for jikwon in jikwondatas:
        jikwon.gogeks = len(Gogek.objects.filter(gogek_damsano=jikwon.jikwon_no))

    
    return render(request, 'jikwonlist.html', {'buser': buser, 'jikwondatas': jikwondatas})



def GogekShow(request):
        jikwon = request.GET.get('jikwon_no')
        gogeks = Gogek.objects.filter(gogek_damsano=jikwon).order_by('gogek_name')
    
        for gogek in gogeks:
            jumin = gogek.gogek_jumin
            last_digit = int(jumin[7])
            if last_digit == 1:
                gogek.gender = '남'
            else:
                gogek.gender = '여'
        
        return render(request, 'gogeklist.html', {'gogeks': gogeks})

