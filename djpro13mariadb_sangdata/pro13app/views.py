from django.shortcuts import render, redirect
import MySQLdb 
from pro13app.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'seoho123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}


def Main(request):
    return render(request, 'index.html')

def ListFunc(request):
    '''
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()  # SQL문 실행 및 select의 결과 기억
        sql = "select * from sangdata"
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas) # (1, '장갑', 3, 10000), (2, '벙어리장갑', 5, 12000) 튜플 타입
        print(type(datas))
        
        return render(request, 'list.html', {'datas':datas})
    except Exception as err:
        print('에러 : ', err)
        conn.rollback()
        
    finally:
    # 역순으로 닫는다.
        cursor.close()
        conn.close()
    # return render(request, 'list.html')
    '''
    # 페이징 처리를 안한 경우
    '''
    datas = Sangdata.objects.all()   
    scount = datas.count()
    print(datas)   
    print(type(datas))
    return render(request, 'list.html', {'datas':datas, 'scount':scount}) # <QuerySet [<Sangdata: Sangdata object (1)>
    '''
    
    # 페이징 처리를 한 겨웅
    datas = Sangdata.objects.all().order_by('-code') # code descend
    # 한 페이지에 5개씩 출력
    paginator = Paginator(datas, 5)
    # print(paginator) <django.core.paginator.Paginator object at 0x0000023A9294F8D0>
    
    # 페이지를 받는다.
    try:
        # 클라이언트로 부터 페이지 요청을 받은 경우
        page = request.GET.get('page')
    except Exception as e:
        # 클라이언트로 부터 페이지가 넘어오지 않는경우
        page = 1
    try:
        # 페이지 정수 값을 받은 경우
        data = paginator.page(page)
    except PageNotAnInteger:
        # 페이지가 정수가 아닌 값을 받은 경우
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
    
    # 개별 페이지 표시 작업용
    allpage = range(paginator.num_pages + 1)
    # print('allpage : ', allpage) allpage :  range(0, 4)
    return render(request, 'list2.html', {'datas':data, 'allpage':allpage})
    

def InsertFunc(request):
    return render(request, 'insert.html')

# 상품 추가 작업 
def InsertOkFunc(request):
    if request.method == 'POST':
        code = request.POST.get("code")
        # 새 상품 code 유무 검증 후 insert 진행
        try:
            # 사용자가 code 컬럼의 데이터값을 요청했을 때 이미 데이터 값이 있을 경우
            Sangdata.objects.get(code=code)
            return render(request, 'insert.html', {'msg':'이미 등록된 상품번호 입니다.'})
        except Exception as e:
            # 추가 작업(데이터값이 없는 경우)
            Sangdata(
                code = code,
                sang = request.POST.get("sang"),
                su = request.POST.get("su"),
                dan = request.POST.get("dan"),               
            ).save()
            return HttpResponseRedirect("/sangpum/list")


def UpdateFunc(request):
    updata = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'data':updata})

def UpdateOkFunc(request):
    # post 방식으로 form 데이터가 넘어올 때
    
    if request.method == 'POST':
        upRecord = Sangdata.objects.get(code = request.POST.get("code"))
        upRecord.code = request.POST.get("code")
        upRecord.sang = request.POST.get("sang")
        upRecord.su = request.POST.get("su")
        upRecord.dan = request.POST.get("dan")
        upRecord.save() # update가 된다.
        
    return redirect('/sangpum/list')

def DeleteFunc(request):
    delRecord = Sangdata.objects.get(code = request.GET.get("code"))
    delRecord.delete()
    return redirect('/sangpum/list')
        
