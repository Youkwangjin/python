from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def MainFunc(request):
    return render(request, 'index.html')  # forward 방식

def SelectOsFunc(request):
    # print('request.GET : ', request.GET)  request.GET :  <QueryDict: {}>
    
    # "favorite_os"가 request.GET에 있는지 확인하고 있다면 해당 값을 출력하고 세션에 "f_os" 키로 저장
    if "favorite_os" in request.GET:
        print(request.GET["favorite_os"]) # get 방식 요청 출력
        request.session["f_os"] = request.GET["favorite_os"] # 세션에 값 저장(세션 생성)
        return HttpResponseRedirect("/showos") # redirect 방식, "showos" 페이지로 리디렉션을 수행합니다. 
        # return redirect("/showos")
    # 이것은 사용자가 운영 체제를 선택한 후 표시할 페이지로 이동하도록 하는 역할
    
    else:
        return render(request, 'selectos.html')

def ShowOsFunc(request):  # request는 Django에서 제공되는 HTTP 요청 객체
    # print("ShowOsFunc 도착")
    dict_context = {}
    
    if "f_os" in request.session:
        print('유효시간 : ', request.session.get_expiry_age())
        dict_context['sel_os'] = request.session["f_os"]
        dict_context['message'] = "그대가 선택한 운영체제는 %s"%request.session["f_os"]
    
    else:
        dict_context['sel_os'] = None
        dict_context['message'] = "운영체제를 선택하지 않았군요"
        
    # del request.session["f_os"] # 특정 키를 가진 세션
    request.session.set_expiry(5) # 5초 유효시간 (기본값 30분)
    
    return render(request, 'show.html', dict_context)