# 이원카이제곱 검정
import pandas as pd
import scipy.stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/home_task.txt",\
                   sep='\t')
print(data.head(2))

# 귀무 (영가설, HO) : 집안일과 종류와 일하는 사람은 관계가 없다. (독립적이다)
# 귀무 (연구가설, 대안 가설, H1) : 집안일과 종류와 일하는 사람은 관계가 없다. (독립적이지 않다.)

chi2, pvalue, _, _ = scipy.stats.chi2_contingency(data)
print('chi2:{}, pvalue"{},'.format(chi2))