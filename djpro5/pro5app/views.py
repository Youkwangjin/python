from django.shortcuts import render


# Spring으로 치면 Controller 역할

def MainFunc(request):
    return render(request, 'index.html')

def Herit1Func(request):
    return render(request, 'kbs1.html')

def Herit2Func(request):
    return render(request, 'kbs2.html')