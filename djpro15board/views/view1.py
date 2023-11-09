from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime

# Create your views here.

def MainFunc(request):
    imsi = "<div><h2>메인 화면입니다.</h2></div>" # html 형식의 문서를 전송
    return render(request, 'index.html', {'maintag':imsi})

def ListFunc(request):
    # 페이징 처리를 한 겨웅
    datas_all = BoardTab.objects.all().order_by('-gnum', 'onum') # code descend
    # 한 페이지에 5개씩 출력
    paginator = Paginator(datas_all, 5)
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
        datas = paginator.page(page)
    except PageNotAnInteger:
        # 페이지가 정수가 아닌 값을 받은 경우
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages())
    
    # 개별 페이지 표시 작업용
    # allpage = range(paginator.num_pages + 1)
    # print('allpage : ', allpage) allpage :  range(0, 4)
    return render(request, 'board.html', {'datas':datas})

# 게시판 글 작성하기
def InsertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        # 게시판 정보를 입력하고 요청 받았을 때
        try:
            gbun = 1
            datas = BoardTab.objects.all() # 전체 자료 읽는다.
            if datas.count() != 0: # 자료 있는 경우
                gbun = datas = BoardTab.objects.latest('id').id + 1
                print(gbun)
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'], # request.META.get('REMOTE_ADDR')
                bdate = datetime.now(),
                readcnt=0,
                gnum=gbun,
                onum=0,
                nested=0,      
            ).save()
        except Exception as e:
            print('추가 에러 : ', e)
            return render(request, 'error.html')
        
    return redirect('/board/list')

def SearchFunc(request):
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        # print(s_type, s_value)

        if s_type == 'title':
            # SQL의 like문 : __contains
            datas_search = BoardTab.objects.filter(title__contains = s_value).order_by('-id')
        elif s_type == 'name':
            datas_search = BoardTab.objects.filter(name__contains = s_value).order_by('-id')
        
        # 페이징
        paginator = Paginator(datas_search, 5)  # 페이지 당 5명씩 출력
        try:
            page = request.GET.get('page')
        except:
            page = 1

        try:
            datas = paginator.page(page)
        except PageNotAnInteger:
            datas = paginator.page(1)
        except EmptyPage:
            datas = paginator.page(paginator.num_pages())

        return render(request, 'board.html', {'datas':datas})

def ContentFunc(request):
    page = request.GET.get('page')
    data = BoardTab.objects.get(id=request.GET.get('id'))
    data.readcnt = data.readcnt + 1
    data.save()     # 조회수 갱신
    return render(request, 'content.html', {'data':data, 'page':page})

def UpdateFunc(request):
    if request.method == 'GET':
        try:
            data = BoardTab.objects.get(id=request.GET.get('id'))
            return render(request, 'update.html', {'data':data})
        except Exception as e:
            print('수정 자료 읽기 오류 : ', e)
            return render('error.html')
    elif request.method == 'POST':
        try:
            updata = BoardTab.objects.get(id=request.POST.get('id'))
            # 비번 비교
            if updata.passwd == request.POST.get('up_passwd'):
                updata.name = request.POST.get('name')
                updata.mail = request.POST.get('mail')
                updata.title = request.POST.get('title')
                updata.cont = request.POST.get('cont')
                updata.save()
                return redirect('/board/list')  # 수정 완료 후 목록 보기
            else:
                return render(request, 'update.html', {'data':updata, 'upmsg':"비밀번호 불일치"})
        except Exception as e:
            print('수정 자료 처리 오류 : ', e)
            return render(request, 'error.html')
            


def DeleteFunc(request):
    if request.method == 'GET':
        deldata = BoardTab.objects.get(id=request.GET.get('id'))
        try:
            return render(request, 'delete.html', {'data':deldata})
        except Exception as e:
            print('수정 오류 :', e)
            return render(request, 'error.html')
    elif request.method == 'POST':
        try:
            deldata = BoardTab.objects.get(id=request.POST.get('id'))
            if deldata.passwd == request.POST.get('del_passwd'):
                deldata.delete()
                return redirect('/board/list') # 삭제 후 목록 보기
            else:
                return render(request, 'error.html')
                
        except Exception as e:
            print('수정 오류 :', e)
            return render(request, 'error.html')