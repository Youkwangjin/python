from django.shortcuts import render
import json
from django.forms.fields import JSONString
from django.http.response import HttpResponse

# dict data
lan = {
    'id':123,
    'name':'파이썬',
    'history':[
        {'date':'2023-10-25', 'exam':'basic'},
        {'date':'2023-10-26', 'exam':'django'},
    ]
}

def testFunc():
    
    print(type(lan)) # <class 'dict'>
    # Python Object(dict, list, tuple 등)를 문자열로 변환 => JSON encoding
    # Json 모양의 문자열을 Python Object(dict)로 변환 : Json decoding
    JSONString = json.dumps(lan)
    print(JSONString)
    print(type(JSONString))
    JSONString = json.dumps(lan, indent=4)
    print(type(JSONString))
    print()
    dictData = json.loads(JSONString) # json decoding
    print(dictData)
    print(type(dictData))
    print(dictData['name'])
    
    for h in dictData['history']:
        print(h['date'], h['exam'])

def MainFunc(request):
    testFunc()
    return render(request, 'index.html')

def Func1(request):
    msg = request.GET.get('msg')
    msg = 'nice ' + msg
    print(msg)
    context = {'key':msg}
    return HttpResponse(json.dumps(context), content_type='application/json')

def Func2(request):
    mydata = [
        {'irum':'tom1', 'nai':22},
        {'irum':'john', 'nai':23},
        {'irum':'gd', 'nai':24}       
    ]
    return HttpResponse(json.dumps(mydata), content_type='application/json')
def Func3(request):
    mydata = [
        {'irum':'tom1', 'nai':22},
        {'irum':'john', 'nai':23},
        {'irum':'gd', 'nai':24}       
    ]
    return HttpResponse(json.dumps(mydata), content_type='application/json')