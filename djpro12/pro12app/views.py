from django.shortcuts import render
from pro12app.models import Maker, Product
from django.db.models.aggregates import Count, Sum, Avg, StdDev



# Create your views here.

def Main(request):
    return render(request, 'index.html')

def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)
    
    # ORM 함수 연습
    print(products)
    print(products.values_list()) # 튜플형식으로 풀려서 보인다.
    print(Product.objects.all().count()) # 건수 5
    print(products.aggregate(Count('pprice'))) # {'pprice__count': 5}
    print(products.aggregate(Sum('pprice'))) # 합 구하기 {'pprice__sum': 937000}
    # {'pprice__sum': 937000} 에서 937000만 원할 때(value 만 원할 때)
    imsi = products.aggregate(Sum('pprice'))['pprice__sum']
    print(imsi) # 937000
    
    print(products.aggregate(Avg('pprice'))) # 평균 구하기 {'pprice__avg': 187400.0}
    print(products.aggregate(StdDev('pprice'))) # {'pprice__stddev': 118143.3028}
    
    # 중복 값 출력 filter
    aa = products.filter(pname = "런닝화")
    print(aa)
    
    for a in aa.values_list():
        print(a)
    
    print(aa)
    
    # 특정 데이터값 제외하고 출력하기 exclude
    aa = products.exclude(pname = "런닝화")
    print(aa)
    
    for a in aa.values_list():
        print(a)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    products = Product.objects.filter(pmaker_name=mid)
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})
    


