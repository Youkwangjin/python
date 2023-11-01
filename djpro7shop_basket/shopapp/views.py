from django.shortcuts import render

# Controller

def MainFunc(request):
    return render(request, 'index.html')

def Page1Func(request):
    return render(request, 'page1.html')

def Page2Func(request):
    return render(request, 'page2.html')

def CartFunc(request):
    name = request.POST["name"]
    price = request.POST["price"]
    # print(name, price)
    product = {'name':name, 'price':price}
    
    # 주문상품 장바구니 추후 세션에 넣어준다.
    productList = []  
    
    # session에 shop 값이 있을 경우
    if "shop" in request.session:
        productList = request.session['shop']
        productList.append(product)
        request.session['shop'] = productList
    
    # 처음 장바구니에 상품을 넣었을 경우 
    else:
        productList.append(product)
        request.session['shop'] = productList
    
    print(productList)
    
    context = {}
    context['products'] = request.session['shop']
    return render(request, 'cart.html', context)
        

def BuyFunc(request):
    # 세션이 있을 때
    if "shop" in request.session:
        productList = request.session['shop']
        
        # 가격 구하기
        total = 0
        for p in productList:
            total += int(p['price'])
        print(total)
        
        del request.session['shop'] # 특정 세션을 제거한다.
        # request.session.clear()     세션 모두 제거한다.
        
    return render(request, 'buy.html', {'total':total})
