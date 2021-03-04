import pandas as pd
import numpy as np

L = [1, 2, 3, 4, 5]
df = pd.DataFrame(L)
print(df)
print("-------------" * 20)

# np.random.randint() # 균일 분포의 정수 난수 1개 생성
# np.random.randint(6)  -> 0부터 5 사이 랜던함 숫자 하나 (6 안나옴)
# np.random.randint(1, 20)  -> 1부터 19 사이 랜던함 숫자 하나 (20 안나옴)
# np.random.rand()    # 0 부터 1 사이 균일 분포에서 난수 Matrix array 생성
# np.random.randn()    # 가우시안 표중 정규 분포에서 난수 Matrix array 생성

# 5 columns 4 rows with columns [A, B, C, D]
df = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'))

dates = pd.date_range('20200101', periods=5)
df = df.set_index(dates)

print(df)
print("-------------" * 20)
# -------------------------------------------------------------------------
# 이번 문제에서 생성한 DataFrame은 pandas 기본 콘텐츠 내에서 계속해서 활용될 예정입니다.
# 앞으로는 이 DataFrame을 지칭할 때는 df_B 라고 하겠습니다.
#
#     A   B   C   D
# 0   A0  B0  C0  D0
# 1   A1  B1  C1  D1
# 2
# ..
# 11  A11 B11 C11 D11
columns = ['A', 'B', 'C', 'D']
data = [[character + str(i) for character in columns] for i in range(12)]
df_B = pd.DataFrame(data, columns=columns, index=range(0,12))

# print(df_B.info())
print("-------" * 20)
# ---------------------------------------------------------------------------------
print(df.describe())
#               A         B         C         D
# count  5.000000  5.000000  5.000000  5.000000
# mean  -0.428318  0.886087 -0.204608 -0.132313
# std    0.899493  0.609804  0.858386  0.868005
# min   -1.908747 -0.009909 -1.135709 -0.749144
# 25%   -0.558199  0.752370 -0.974085 -0.609033
# 50%   -0.195133  0.786263 -0.192273 -0.531032
# 75%    0.147997  1.353730  0.461999 -0.139033
# max    0.372494  1.547979  0.817029  1.366676
#
# df_A를 이용해서, column C 기준으로 내림차순 정렬한 결과를 출력하는 코드를 작성해보세요.

print(df.sort_values(by=['C'], ascending=False))
# For more information on sorting refer to this url
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
print("----" * 20)
# df_A를 이용해서, column A(A열)를 출력하는 코드를 작성해보세요.
print(df['A'])



# DataFrame.at
# Access a single value for a row/column label pair.
# DataFrame.iloc
# Access group of rows and columns by integer position(s).
# DataFrame.xs
# Returns a cross-section (row(s) or column(s)) from the Series/DataFrame.
# Series.loc
# Access group of values using labels.
# print(df.loc[:, 'A'])

# # loc
# Object Type
# Indexers
# Series
# s.loc[indexer]
# DataFrame
# df.loc[row_indexer,column_indexer]
#
# df_A를 이용해서,
#
# 3번째 행의 원소들,
print("df.iloc[3]")
print(df.iloc[3])
# index가 2020-01-05에 해당하는 행
# 을 출력하는 코드를 작성해보세요.
print("df.loc['2020-01-05']")
print(df.loc['2020-01-05'])
# print("iloc[4]", df.iloc[4])

print("---" * 30)

# df_A를 이용해서, 2020년 1월 2일부터 2020년 1월 4일까지의
# 데이터중에 column A, B에 해당하는 데이터를 출력하는 코드를 작성해보세요.

print("")
print(df[, ["A","B"]])