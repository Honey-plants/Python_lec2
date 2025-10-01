import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(4,3),
                     columns = ['서울','부산','인천'],
                     index= ['김가','이가','최가','오가'])
print(frame)

f1 =lambda x : x.max() - x.min()
result1 = frame.apply(f1, axis=0)
print(result1)
print()
result1 = frame.apply(f1, axis=1)
print(result1)
print()

def f2(x):
    return pd.Series([x.mean(),x.std()], index=['mean', 'std'])
result2 = frame.apply(f2, axis=0)
print(result2)
print()

f3 = lambda  x : f'{x:.2f}'
result3 = frame.map(f3)
print(result3)

sd = frame['인천']
print(sd)

print(sd.map(f3))
print(sd.apply(f3))
