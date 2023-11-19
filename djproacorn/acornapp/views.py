from django.shortcuts import render
from acornapp.models import Jikwon
from django.http.response import HttpResponseRedirect

# Create your views here.

def MainFunc(request):
    return render(request, 'index.html')

def LoginOk(request):
    return render(request, 'show.html')

def LoginProcess(request):
    if request.method == 'POST':
        jikwon_no = request.POST.get('jikwon_no')
        jikwon_name = request.POST.get('jikwon_name')
        
        try:
            jikwon = Jikwon.objects.get(jikwon_no=jikwon_no)
            print(f'사번: {jikwon.jikwon_no}, 이름: {jikwon.jikwon_name}')
            
            if jikwon_name == jikwon.jikwon_name:
                return HttpResponseRedirect("/loginOk")
            else:
                error_message = "이름이 일치하지 않습니다."
        
        except Exception as e:
            print('오류 발생 : ', e)
        
        return render(request, 'loginfail.html', {'error_message': error_message})
    