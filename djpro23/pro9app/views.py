from django.shortcuts import render
from pro9app.models import Friend

# Create your views here.

def Main(request):
    return render(request, 'index.html')

def DbShow(request):
    datas = Friend.objects.all() # 전체 자료 읽기
    return render(request, 'list.html', {'datas':datas})
