import pandas as pd

# X.isnull().sum()

# # 1) 결측치 : column 별 평균값으로 대체
# X.fillna(X.mean())

# # 2) 결측치 : 직전 행 값으로 대체
# X.fillna(method='ffill')

# # 3) 결측치 : 바로 다음 행 값으로 대체
# X.fillna(method='bfill')

# # 4) 결측치 : 삭제
# X.dropna(axis=0)
# eg

df = pd.read_excel('missing_data1.xlsx')
print(df)
print("df.isnull().sum(): ")
print(df.isnull().sum()) # NaN 갯수 세기

# # 1) 결측치 : column 별 평균값으로 대체
df_A =  df.fillna(X.mean())
print(df_A)
