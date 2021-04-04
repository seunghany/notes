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
X, y = dataset.data, dataset.target # Breaset Cancer 데이터를 X, y로 나누어 저장
X = pd.DataFrame(X, columns=dataset.feature_names)

# print("X: ", X)
# print("y: ", y)


