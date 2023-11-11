from django.shortcuts import render
from pro17app.models import Sangdata
from django.http.response import HttpResponse
import json

def MainFunc(request):
    return render(request, 'index.html')

def ListFunc(request):
    return render(request, 'list.html')

def DBFunc(request):
    sdata = Sangdata.objects.all()
    datas = []
    for s in sdata:
        dic = {'code':s.code, 'sang':s.sang, 'su':s.su, 'dan':s.dan}
        datas.append(dic)
    
    return HttpResponse(json.dumps(datas), content_type = 'application/json')