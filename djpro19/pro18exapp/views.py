from django.shortcuts import render
from pro18exapp.models import Producttab
import json
from django.http.response import HttpResponse, HttpResponseRedirect
import MySQLdb


config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'seoho123',
    'database': 'productdb',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

def MainFunc(request):
    return render(request, 'main.html')

def BugerFunc(request):
    # 'category'가 1인 데이터만 필터링
    bdata = Producttab.objects.filter(category=1)
    datas = []
    
    for b in bdata:
        dic = {
            'id': b.id,
            'category': b.category,
            'pname': b.pname,
            'price': b.price,
            'stock': b.stock,
            'description': b.description

        }
        datas.append(dic)
    
    return HttpResponse(json.dumps(datas), content_type='application/json')
    

def DrinkFunc(request):
    # 'category'가 2인 데이터만 필터링
    ddata = Producttab.objects.filter(category=2)
    datas = []
    
    for d in ddata:
        dic = {
            'id': d.id,
            'category': d.category,
            'pname': d.pname,
            'price': d.price,
            'stock': d.stock,
            'description': d.description

        }
        datas.append(dic)
    
    return HttpResponse(json.dumps(datas), content_type='application/json')
    

def AdminFunc(request):
    return render(request, 'admin.html')
    
def ListshowFunc(request):
    bdata = Producttab.objects.all()
    datas = []
    
    for b in bdata:
        dic = {
            'id': b.id,
            'category': b.category,
            'pname': b.pname,
            'price': b.price,
            'stock': b.stock,
            'description': b.description
        }
        datas.append(dic)
    
    return HttpResponse(json.dumps(datas), content_type='application/json')

def InsertFunc(requset):
    return render(requset, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        pname = request.POST.get("pname")
        category = request.POST.get("category")
        if category == "burger":
            category_value = 1
        elif category == "drink":
            category_value = 2
        try:
            Producttab.objects.get(pname=pname)
            return render(request, 'insert.html', {'msg':'이미 등록된 상품명 입니다.'})
        except Exception as e:
            Producttab(
                category = request.POST.get("category"),
                pname = request.POST.get("pname"),
                price = request.POST.get("price"),
                stock = request.POST.get("stock"),
                description = request.POST.get("description"), 
            ).save()
            return HttpResponseRedirect("admin")
            
   
        
