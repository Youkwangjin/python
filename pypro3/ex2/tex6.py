# 일원분산분석
# 강남구에 있는 GS 편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 있는가?
import matplotlib.pyplot as plt
# 귀무 : GS 편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 없다.
# 대립 : GS 편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import urllib.request

from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import urllib.request


url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt'
#  = pd.read_csv(url, header=None)
# data = data.dropna()
# print(data.head(3), data.shape)  # (22, 2)

data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
print(data, type(data))  # <class 'numpy.ndarray'>
print(data.shape)  # (22, 2)

gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]

print(gr1, ' ', np.mean(gr1))  # 316.625
print(gr2, ' ', np.mean(gr2))  # 256.4
print(gr3, ' ', np.mean(gr3))  # 278.0

# 정규성
print(stats.shapiro(gr1).pvalue)
print(stats.shapiro(gr2).pvalue)
print(stats.shapiro(gr3).pvalue)

# 등분산성
print(stats.levene(gr1, gr2, gr3).pvalue)    # 0.0458
print(stats.bartlett(gr1, gr2, gr3).pvalue)  # 표본의 갯수가 많지 않기 때문에 0.3508

# 데이터 산포도(시각화)
plt.boxplot([gr1, gr2, gr3], showmeans=True)
plt.show()

# 일원분산분석 처리 방법1
df = pd.DataFrame(data, columns=['pay', 'group'])
print(df)
lmodel = ols('pay ~ C(group)', data=df).fit()  # C(독립변수) : 변수가 변주형임을 표시
print(anova_lm(lmodel, typ=1))  # 0.043589 < 0.05 이므로 귀무가설 기각

print()

# 일원분산분석 처리 방법2
f_statistic, p_value = stats.f_oneway(gr1, gr2, gr3)
print('f_statistic:{}, p_value{}'.format(f_statistic, p_value))
# GS 편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 있다.

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tkResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
print(tkResult)
tkResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
