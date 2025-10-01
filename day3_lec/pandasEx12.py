import pandas as pd
import numpy as np

data = pd.Series([1, np.nan, 3.5, np.nan, 7])
# print(data)
# print()
# print(data.dropna())
# print()
# print(data.notnull())
# print()
# print(data[data.notnull()])
# print()
# print(data.isnull())
# print()
#
#
# np.random.seed(12345)
# frame = pd.DataFrame(np.random.randn(7,3),
#                      columns=['seoul', 'busan','incheon'])
# frame.iloc[:4, 1] = np.nan
# frame.iloc[:2, 2] = np.nan
#
# print(frame)
# print()
#
# print(frame.fillna(0))              #전부 0으로 바꿈
# print()
# print(frame.fillna({'busan':-5, 'incheon':0}))  #각각에 맞게 수 변경
# print()
# print(frame.fillna(pd.Series([-5,0], index=['busan', 'incheon'])))
# print()
# print(frame.mean())
# print()
# print(frame.fillna(frame.mean()))
# print()
# print(frame.bfill())       #백필

data = {'one':np.arange(6),
        'two':np.arange(6,0,-1),
        'three':[1,1,1,2,2,2],
        'four':[0,1,2,0,1,2]}
frame2 = pd.DataFrame(data)
print(frame2)
print()
print(frame2.set_index('three'))
print()
print(frame2.set_index(['two','four']))
print()
