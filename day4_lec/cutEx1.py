import pandas as pd

ages = [20, 22, 25, 27, 21, 37, 31, 62, 45, 41, 70, 32]
bins = [18, 25, 35, 60, 100]
cdata = pd.cut(ages, bins)
print(cdata)
print(cdata.value_counts())
print()
cdata = pd.cut(ages, bins, right=False, labels=['Youth','YoungAdult','MiddleAged','Senior'])
print(cdata)
print(cdata.value_counts())
print()