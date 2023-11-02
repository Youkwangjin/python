from django.shortcuts import render
from pro8app.models import Article

def Main(request):
    return render(request, 'index.html')

def DbShow(request):
    datas = Article.objects.all()
    # print(datas)    <QuerySet [<Article: Article object (1)>]>
    print(datas[0].name)
    return render(request, 'list.html', {'datas':datas})