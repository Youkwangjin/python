from django.shortcuts import render

def MainFunc(request):
    return render(request, 'index.html')

def SelectFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    
    elif request.method == 'POST':
        text = request.POST.get("gender")
        
        if text == "남":
            irum = "요청결과 남"
            img = "/static/images/man.jpg"
        elif text == "여":
            irum = "요청결과 여"  
            img = "/static/images/woman.jpg"
        return render(request, 'show.html', {'irum': irum, 'img':img})