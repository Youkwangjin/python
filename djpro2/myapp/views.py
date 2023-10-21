from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('초기 요청 처리')

def helloFunc(request):
    msg = "창고 만세"
    ss = "<html><body>장고 프로젝트 구현 %s</body></html>"%msg
    return HttpResponse(ss)

def worldFunc(requset):
    msg = "장고 처리 구조 이해" # {key, value} dict 타입으로 준다.
    return render(requset, 'show.html', {'msg': msg})  # templates 안에 들어가서 찾는다. forward 방식이 기본이다.


