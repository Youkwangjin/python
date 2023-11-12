from django.shortcuts import render
from pro18app.models import Jikwon
from django.http.response import HttpResponse
import json

def MainFunc(requset):
    return render(requset, 'index.html')


def ListFunc(request):
    name = request.GET['name']
    jdata = Jikwon.objects.select_related('buser_num').filter(jikwon_jik=name) # buser_num 관련된 데이터를 매핑
    print(jdata)
    
    datas = []
    
    #<QuerySet []> 타입을 dict 타입으로 저장해 json 형식의 문자열로 클라이언트에 전송 
    for j in jdata:
        dictData = {'jikwon_no':j.jikwon_no, 'jikwon_name':j.jikwon_name, 'buser_name':j.buser_num.buser_name} # 포함관계라 생각하자.
        datas.append(dictData)
        
    
    return HttpResponse(json.dumps(datas), content_type = 'application/json')