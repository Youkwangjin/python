# 세 개 이상의 모집단에 대한 가설검정 – 분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인
# 에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
import matplotlib.pyplot as plt
# f값 = 그룹 간 분산 (Between Varience) / 그룹 내 분산 (Between Varience)
# 분자 부분의 분산을 비교 대상인 분모 부분의 분산과 비교하여 비율로써 나타낸 값 f-value
# 독립변수는 범주형, 종속변수는 연속형




# 서로 독립인 세 집단의 평균 차이 검정 - 일원분산분석(one-way anova)
# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv
# 귀무 : 교육방법에 따른 시험 점수에 차이가 없다/
# 대립 : 교육방법에 따른 시험 점수에 차이가 있다.
import numpy as np
import pandas as pd
import scipy.stats as stats
import urllib.request

from statsmodels.formula.api import ols

url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/three_sample.csv'
data = pd.read_csv(urllib.request.urlopen(url), delimiter=',', na_values=' ')
data = data.dropna()
print(data.head(3), data.shape)  # (80, 4)

# plt.boxplot(data.score)
# plt.show()  # 이상치가 발견

data = data.query('score <= 100')
print(data.shape)
# plt.hist(data.score)
# plt.show()

# 분산분석의 전제조건 : 3가지를 충족할 때 의미있다.
# 독립설 : 각 집단은 서로 독립이어야 한다.(상관관계로 확인)
# 정규성 : 각 집단은 서로 정규분포를 떠라야한다. shapiro, stats.k2_2samp
# 불편설(등분산성) : 각 집단은 서로 분산이 일정해야 한다.


print(data['method'].unique())  # [1 3 2]
result = data[['method', 'score']]
m1 = result[result['method'] == 1]
m2 = result[result['method'] == 2]
m3 = result[result['method'] == 3]

print(m1[:3])
print(m2[:3])
print(m3[:3])

score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print(np.mean(score1), np.mean(score2), np.mean(score3))  # 67.38, 67.38, 68.87



# 정규성 검정 :
print(stats.shapiro(score1).pvalue)  # 0.1746 > 0.05 이므로 정규성 만족
print(stats.shapiro(score2).pvalue)  # 0.3318
print(stats.shapiro(score3).pvalue)  # 0.1155

print(stats.ks_2samp(score1, score2).pvalue)
print(stats.ks_2samp(score1, score3).pvalue)
print(stats.ks_2samp(score2, score3).pvalue)

print('등분상성 검정 : 만족하면 anova, 만족하지 않으면 welch-anova')
print(stats.levene(score1, score2, score3).pvalue)  # 모수 검정 0.1132 > 0.05 이므로 등분산성 만족
print(stats.bartlett(score1, score2, score3).pvalue)  # 비모수 검정
# 참고 : 등분산성을 만족하지 않은 경우 대처 방안
# 데이터를 normalization 으로 처리, standardization(표준화)로 처리, transformation 경우에 따라 지연 log 를 붙임


# 교차표 : 교육방법별 건수
ctab1 = pd.crosstab(index=data['method'], columns='count')
print(ctab1)
# 교차표 : 교육방법별 만족여부 건수
ctab2 = pd.crosstab(data.method, data.survey)
ctab2.index = ['방법1', '방법3', '방법2']
ctab2.columns = ['만족', '불만족']
print(ctab2)


# anova_lm은 f통계량을 위해 회귀분석 결과를 사용
import statsmodels.api as sm

reg = ols('score ~ method', data).fit()
# reg = ols('data["score"] ~ data["method"]', data=data).fit()
table = sm.stats.anova_lm(reg, typ=1)
print(table)
# 해석 : p-value : 0.727597 > 0.05이므로 귀무가설 기각 실패. 교육방법에 따른 시험 점수에 차이가 없다.

# 사후 분석 : ANOVA 검증 결과 유의미하다는 결론을 얻었을 때, 구체적으로 어떤 수준에서 평균 차이가 나는지를 검증하는 방법

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tkResult = pairwise_tukeyhsd(endog=data.score, groups=data.method)
print(tkResult)
tkResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
