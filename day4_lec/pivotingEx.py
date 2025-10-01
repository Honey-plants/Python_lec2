import numpy as np
import pandas as pd

data= pd.DataFrame(np.arange(6).reshape(2,3),
                   index=pd.Index(['ohio','colorado'], name='state'),
                   columns=pd.Index(['one','two','three'], name='number'))
print(data)
print()

result = data.stack()
print(result)
print()

print(result.unstack())         #항상 맨 오른쪽께 돌아감
print()
print(result.unstack(level=0))
print()
print(result.unstack('state'))

s1 = pd.Series([0,1,2,3], index=list('abcd'))
s2 = pd.Series([4,5,6], index=list('cde'))
print(s1)
print()
print(s2)
print()
data2 = pd.concat([s1, s2], axis=0, keys=['one','two'])
print(data2)
print()
print(data2.unstack())
print()
print(data2.unstack(level=0))