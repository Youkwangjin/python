from django.shortcuts import render, redirect
from pro11app.models import Family
from django.db.models import Avg


# Create your views here.

def MainFunc(request):
    return render(request, "index.html")

def ListFunc(request):
    fdatas = Family.objects.all()
    total = fdatas.count()
    avg_age = fdatas.aggregate(Avg('age'))['age__avg']

    return render(request, 'show.html', {'fdatas': fdatas, 'total': total, 'avg_age': avg_age})
    


def InserForm(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        Family(
            name = request.POST.get('name'),
            age = request.POST.get('age'),
            tel = request.POST.get('tel'),
            gen = request.POST.get('gen'),
            
        ).save()
        
    
    return redirect("/select") # 추가 후 목록 보기