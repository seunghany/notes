from sklearn.datasets import load_breast_cancer
import pandas as pd
import matplotlib.pyplot as plt
# The breast cancer dataset is a classic and very easy binary classification dataset.

# return_X_ybool, default=False
# If True, returns (data, target) instead of a Bunch object.
# as_framebool, default=False
# If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric).
#  The target is a pandas DataFrame or Series depending on the number of target columns.
#  If return_X_y is True, then (data, target) will be pandas DataFrames or Series as described below.
#
dataset = load_breast_cancer()
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
# X, y = dataset.data, dataset.target
print(X.columns)
df = pd.DataFrame(X, columns = dataset.feature_names)

df.mean().plot.bar()
# plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, stratify=y, random_state=34)

# Decision Tree 분류기 불러오기
clf = DecisionTreeClassifier()

# Decision Tree 학습을 위해 parameter 채우기
clf.fit(X_train, y_train)

# Decision Tree 테스트를 위해 parameter 채우기
pred = clf.predict(X_test)

# accuracy 계산
acc = accuracy_score(pred, y_test)
print("DecisionTree")
print("Accuracy : %.3f" % acc)

# ----------------------------------------------------------------------------------------------------------------
# Random Forest가 Decision Tree보다 성능이 더 좋을거로 예상
#   - Decision Tree가 가지고 있는 단점들을 Ensenble 모델로 보안 가능
#   - 구체적으로는 OverFitting 해결 가능
# Random Forest - > 많은 Tree 모델
#     i.	Decision Tree에 있던 단점들을 , 여러개 트리를 활용함으로 써 극복 해 낸 모델
#     ii.	구체적으로는 overfitting 문제를 해결 할 수 있는 알고리즘
#     iii.	중요한 이유
#         1.	활용 범주가 넓음
#             a.	연속형 변수, Yes or no, 다중 Classification 등
#         2.	 앙상블 모델의 기본 알고리즘이기 때문
#             a.	여러개의 모델을 합쳐 하나의 앙상블을 만들어 내 좋은 결과 만들기.
#         3.	예측 능력이 좋다 **
#             a.	앞서 말한 세가지 (Linear Regression, Logistic Regression, Decision Tree) 보다 나은 예측 능력을 보여줌
#             b.	어느정도 실무 문제는 다 할 수 있음
# Random Forest 불러오기
from sklearn.ensemble import RandomForestClassifier
 # accuracy 계산을 위해서 numpy load
import numpy as np

# Random Forest 분류기 불러오기
clf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)

# Random Forest 학습을 위해 parameter 채우기
clf.fit(X_train, y_train)
# Random Forest 테스트를 위해 parameter 채우기
pred = clf.predict(X_test)

# accuracy 계산
acc = accuracy_score(pred, y_test)
print("RandomForestClassifier")
print("Accuracy : %.3f" % acc)

# Decision Tree Classifier와 Random Forest Classifier의 성능 차이가 크게 발생합니다.
#
# Random Forest Classifier의 성능이 더 좋은 이유:Random Forest는 Decision Tree가 모인 숲(Forest)입니다.
#
# Decision Tree 하나만으로 머신러닝을 할 수 있지만 데이터셋에 대해 Overfitting이 되는 문제가 발생할 수 있습니다. 이 때, 여러 개의 Decision Tree를 통해 문제를 해결할 수 있습니다.
#
# Feature가 30개라고 할 때, Decision Tree의 가지는 꽤나 많아질 것입니다. 이 때 Overfitting 문제가 발생할 수 있습니다.
#
# 30개 중 랜덤의 5개 Feature로 Decision Tree를 생성하고, 다른 5개로 생성하고 총 6개의 Decision Tree를 생성하면 각 Tree마다 예측값이 나옵니다.
#
# 6개의 Decision Tree가 예측한 값들 중에 가장 많이 나온 값을 최종 예측값으로 정하는 것입니다. 그러므로 더 예측값이 더 높게 나올 수 있습니다.

# --------------------------------------------------------------------------------------
# Breast Cancer 데이터 셋을 Random Forest를 이용하여 분류한 뒤,
# Random Forest 모델이 정한 Feature importance를 출력하는 코드를 작성하세요.
fig, ax = plt.subplots(figsize=(12, 20))
feature_importances = clf.feature_importances_
feature_importances = sorted(feature_importances, reverse=True)

y_pos = np.arange(len(feature_importances))

ax.barh(y_pos, feature_importances, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(X.columns)
ax.invert_yaxis()
ax.set_xlabel('Performance')

ax.set_title('Feature Importance of Random Forest Classifier')

plt.show()