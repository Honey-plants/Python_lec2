import pandas as pd
import numpy as np
from numpy.ma.core import reshape

obj1 = pd.Series([4,7,-5,3], index=list('dabc'))
print(obj1)
print()

obj2 = obj1.reindex(list('abcde'))      #복사해서 가져옴
print(obj2)             #NaN 타입은 플로트 타입 그래서 실수로 바뀐것
print()

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0,2,4])
print(obj3)

obj4 = obj3.reindex(np.arange(6),method='ffill') #fornt fill
print(obj4)
print()

frame = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=list('acd'),
                     columns = ['ohio', 'texas', 'califonia'])

print(frame)
print()
print(frame.reindex(index=list('abcd')))
print()
print(frame.reindex(columns=['texas', 'utah', 'califonia']))
print()
print(frame.reindex(index=list('abcd'), columns=['texas', 'utha', 'califonia']))