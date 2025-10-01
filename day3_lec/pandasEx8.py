import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12).reshape(3,4),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape(4,5),
                   columns=list('abcde'))

print(df1)
print()
print(df2)
print()

print(df1 + df2)
print()

print(df1.add(df2, fill_value=0))
print()

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     columns=list('bde'),
                     index=['one', 'two', 'three', 'four'])
print(frame)
sdata = frame.iloc[0]
print()
print(sdata)
print()
print(frame - sdata)
