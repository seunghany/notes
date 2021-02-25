# What is pandas?
# Pandas is an abbreviation for (Python Data Analysis Library).
# It is a library that helps you handle dataframe.

# What is DataFrame?
# DataFrame is the most common structured API and simply represents a table of data with rows and columns
# We could call these (Structured Data, tabular Data)

# 0. Importing pandas
import pandas as pd

# 1. Creating DataFrame
L = [1, 2, 3, 4, 5]
df = pd.DataFrame(L)
# print(df)
#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5

# the first Column is index and the second column is the series of data created from the list
L2 = {"id": [1, 2, 3, 4, 5], "name": ["A", "B", "C", "D","E"]}
df2 = pd.DataFrame(L2)
# print(df2)
#    id name
# 0   1    A
# 1   2    B
# 2   3    C
# 3   4    D
# 4   5    E
#
import numpy as np

# np.random.randint() # 균일 분포의 정수 난수 1개 생성
# np.random.randint(6)  -> 0부터 5 사이 랜던함 숫자 하나 (6 안나옴)
# np.random.randint(1, 20)  -> 1부터 19 사이 랜던함 숫자 하나 (20 안나옴)

# np.random.rand()    # 0 부터 1 사이 균일 분포에서 난수 Matrix array 생성
# np.random.randn()    # 가우시안 표중 정규 분포에서 난수 Matrix array 생성

mydict = {"A": [np.random.randint(7) for i in range(5)],
          "B": [np.random.randint(1, 20) for i in range(5)],
          "C": [np.random.rand() for i in range(5)],
          "D": [np.random.randn() for i in range(5)]}


# # date
# df4 = pd.DataFrame({'year': [2020, 2020, 2020, 2020, 2020],
#                     'month': [1, 1, 1, 1, 1],
#                     'day': [1, 2, 3, 4, 5]
#                     })
# df4 = pd.to_datetime(df4, format='%Y%m%d', errors='ignore')
# print(df4)
dates = pd.date_range('2020-01-01', periods = 5)
# df3 = pd.DataFrame(mydict, index=df5)
# 또는
df = pd.DataFrame(mydict)
df = df.set_index(dates)

print(df)

# L = ["A", "B", "C", "D"]
# output_table = []
# for i in range(12):
#     temp = []
#     for alphabet in L:
#         element = alphabet + str(i)
#         # A0 ~ D0
#         temp.append(element)
#     output_table.append(temp)
# df = pd.DataFrame(output_table, columns = L)
# print(df)
# Shorter Version
cols = ['A', 'B', 'C', 'D']
data = [[c+str(i) for i in range(12)] for c in cols]
df_b = pd.DataFrame(np.array(data).T, index=range(0, 12), columns=cols)
print(df_b)

# Printing top 5 rows from the df_b
print(df_b[:5])  # or df_b.head()

# Printing columns of database
print(df_b.columns)
# Printing index of database
print(df_b.index)
# Printing values of database
print(df_b.values)

# Dataframe 요약정보 출력
df_b.info()