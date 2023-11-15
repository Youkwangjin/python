
from django.shortcuts import render, redirect
from pro21app.models import Survey
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.rc('font', family='')

def surveyMain(request):
    return render(request, 'index.html')

def surveyAnalysis(requset):  # 이원카이제곱검정
    rdata = list(Survey.objects.all().values())
    # print(rdata)
    df = pd.DataFrame(rdata)
    df.dropna()
    # print(df)

    # 남여를 1, 2처럼 더미(dummy)화 해도 되고
    # 안하고 그냥 처리도 가능
    ctab = pd.crosstab(index=df['gender'], columns=df['co_survey'])
    
    # chi2 추정 및 검정
    chi, pv, _, _ = stats.chi2_contingency(observed=ctab)
    print('chi:{}, pv:{}'.format(chi, pv))
    
    if pv >= 0.05:
        result = "p값이 {0} > 0.05 이므로 <br> 성별과 커피브랜드의 선호관계가 없다. (귀무채택)".format(pv)
    else:
        result = "p값이 {0} < 0.05 이므로 <br> 성별과 커피브랜드의 선호관계가 있다. (귀무기각)".format(pv)

    count = len(df)
    fig = plt.gcf()
    coffee_group = df.groupby(['co_survey'])['rnum'].count()
    coffee_group.plot.bar(color=['red', 'blue'], width=0.5, rot=0)
    plt.xlabel('커피 브랜드명')
    plt.title('커피 브랜드별 선호 건수')
    plt.grid()
    fig.savefig('C:\work\pysou\djpro21/pro21app/static/images/coffee.png')

    return render(requset, 'list.html', {'ctab': ctab.to_html(), 'result':result, 'count':count})
def surveyProcess(request):
    insertData(request)     # 설문조사 결과를 DB에 저장
    return redirect('/coffee/surveyshow')   # 분석 결과 보기
def surveyView(request):
    return render(request, 'servey.html')

def insertData(requset):
    if requset.method == 'POST':
        '''
        print(requset.POST.get('gender'))
        print(requset.POST.get('age'))
        print(requset.POST.get('co_survey'))
        '''
        Survey(
            gender=requset.POST.get('gender'),
            age=requset.POST.get('age'),
            co_survey=requset.POST.get('co_survey'),
        ).save()
    pass