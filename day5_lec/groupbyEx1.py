import numpy as np
import pandas as pd

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})

print(df)
print()

grouped1 = df.groupby('key1')
print(grouped1)
print()

for gd in grouped1:
    print(gd, end='\n\n')
print()

for gname, gdata in grouped1:
    print(gname)
    print(gdata, end='\n\n')
print('==========================')

print(grouped1[['data1','data2']].mean())
print()
print(grouped1[['data2']].sum())
print('-----------------------------')
print()

print(list(grouped1))
print()
print(list(grouped1)[0][1])
print('===============================')

# print(dict(list(grouped1)))
dcdata = dict(list(grouped1))
print(dcdata)
print()

print(dcdata['b'])
print()

grouped2 = df.groupby(['key1', 'key2'])     #하위그룹 만들기
for gd in grouped2:
    print(gd, end='\n\n')
print()

print(grouped2[['data1','data2']].sum())