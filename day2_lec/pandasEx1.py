import pandas as pd
import numpy as np

obj1 = pd.Series([4,7,-5,3])
print(obj1)
print(type(obj1))
print()
print(obj1.index)
print(obj1.values)
print(type(obj1.values))
print()

obj2 = pd.Series([4,7,-5,3], index=['a', 'b', 'c', 'a'])
print(obj2)             #인덱스가 겹치게 될 수 있다.
print(obj2['c'])
print(obj2[['c', 'b']])
print(obj2['a'])        #인덱스 값이 겹치게 설정하면 같은 인덱스값들이 다 출력
print()
obj2['c'] = 100
print(obj2)
print()
#======스칼라 연산=====
print(obj2*3)
print()
print(obj2 > 5)
print()
print(obj2[obj2 > 5])
print()
print(np.exp(obj2))
print()

ddata = {'ohio':35000, 'texas':72000, 'oregon':18000, 'utah':5000}
print(ddata)
print()
obj3 = pd.Series(ddata)
print(obj3)
