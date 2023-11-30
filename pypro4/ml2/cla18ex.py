# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다.
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다.
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오.
# 임의의 값을 넣어 분류 결과를 확인하시오.

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='malgun gothic')

df = pd.read_csv('../testdata/Heart.csv')
df = df.drop(['Unnamed: 0'], axis=1)
print(df.head(3), df.shape)  # (303, 15)
print(df.info())
df.fillna({'Ca': float(df['Ca'].mean())}, inplace=True)

df_x = df.drop(columns=['ChestPain', 'Thal', 'AHD'])
df_y = df['AHD']

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (242, 12) (61, 12) (242,) (61,)

print()

# model
model = svm.SVC(C=1).fit(x_train, y_train)

pred = model.predict(x_test)
print('예측값 :', pred[:10])
print('실제값 :', y_test[:10].values)

acc = metrics.accuracy_score(y_test, pred)
print('acc :', acc)  # 0.6721311475409836

print() 
# 교차 검증
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, x_test, y_test, cv = 5)
print('각각의 검증 정확도 :', cross_vali)
print('평균 검증 정확도 :', cross_vali.mean())

# 새 값으로 예측
new_data = pd.DataFrame({'Age': [60, 65], 'Sex': [1, 0], 'RestBP': [145, 160], 'Chol': [250, 245], 'Fbs': [2, 0], 'RestECG': [1, 2], 'MaxHR': [150, 125], 'ExAng': [0, 1], 'Oldpeak': [2.3, 1.7], 'Slope': [3, 2], 'Ca': [3, 2]})
new_pred = model.predict(new_data)
print('새로운 예측값 :', new_pred)
