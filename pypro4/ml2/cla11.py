# 부스팅은 데이터셋 모델이 뒤의 데이터셋을 정해주고 앞의 모델들을 보완해 나가며 학습시켜 나간다. (순차, 직렬 학습)
# 때문에 시간이 보다 오래 걸리고 해석이 어렵다는 단점이 있다.
# 부스팅의 종류 : XGBoost, LightGBM, ...

# breast cancer dataset으로 실습
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# pip install xgboost
# pip install lightgbm
import xgboost
from xgboost import plot_importance
from lightgbm import LGBMClassifier  # xgboost 보다 연산량이 적어 손실을 줄일 수 있다. 대용량 처리가 효율적이다.

dataset = load_breast_cancer()
print(dataset.keys())
x_feature = dataset.data
y_label = dataset.target

cancerDf = pd.DataFrame(data=x_feature, columns=dataset.feature_names)
print(cancerDf.head(3))
print(dataset.target_names)
print(np.sum(y_label == 0))  # malignant : 212 양성
print(np.sum(y_label == 1))  # benign : 357 악성
