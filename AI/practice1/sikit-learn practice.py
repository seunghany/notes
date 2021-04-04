from sklearn.datasets import load_breast_cancer

# The breast cancer dataset is a classic and very easy binary classification dataset.

# return_X_ybool, default=False
# If True, returns (data, target) instead of a Bunch object.
# as_framebool, default=False
# If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric).
#  The target is a pandas DataFrame or Series depending on the number of target columns.
#  If return_X_y is True, then (data, target) will be pandas DataFrames or Series as described below.
#
data = load_breast_cancer()
print(data.target[[10, 50, 85]])
print(list(data.target_names))

# X, y = load_breast_cancer(as_frame=True)
# print("X: ", X)
# print("y: ", y)

