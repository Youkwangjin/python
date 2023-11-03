from django.shortcuts import render,redirect
from pro10app.models import Guest
from datetime import datetime
from django.http.response import HttpResponseRedirect
from distributed.http.utils import redirect
from django.db.models import Avg


# Create your views here.


def MainFunc(request):
    return render(request, 'index.html')


def ListFunc(request):
    print(Guest.objects.filter(title__contains='연습')) # 제목에 연습이 포함되어 있으면 출력
    print(Guest.objects.filter(title='연습'))
    print(Guest.objects.get(id=1))
    
    # select * from pro10app_guest
    gdatas = Guest.objects.all()  
    
    # 정렬 방법 1
    # gdatas = Guest.objects.all().order_by('title', '-id') # 정렬 (title : ascend, id : descend)   
    # gdatas = Guest.objects.all().order_by('-id')[0:2]
    return render(request, 'list.html', {'gdatas': gdatas}) # {key, value}


def InsertFunc(request):
    return render(request, 'insert.html')


def InsertOkFunc(request):
    if request.method == 'POST':
        # print(request.POST.get('title'))
        # insert into pro10app_guest(...
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()
            # regdate = timezone.now()       
        ).save()
        
        ''' 수정
        Guest(
            g = Guest.objects.get(id=수정할번호)
            g.title = request.POST.get('title'),
            g.content = request.POST.get('content'),
            regdate = datetime.now()
            # regdate = timezone.now()       
        ).save()
        '''
        
        ''' 삭제
            g = Guest.objects.get(id=삭제할번호)
            g.delete()
       
        '''
    # return HttpResponseRedirect("/guest/select")
    
    # show cut
    return redirect("/guest/select") # 추가 후 목록 보기


