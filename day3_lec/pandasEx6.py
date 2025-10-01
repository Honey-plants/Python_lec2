import pandas as pd
import numpy as np

sd1 = pd.Series(np.arange(5), index=list('abcde'))
print(sd1)
print()

print(sd1.drop(['c','e']))              #원본은 그대로임
print()
print(sd1)

sd1.drop(['c','e'], inplace=True)       #True 를 하면 리턴을 안하고 원본자체를 바꿈
print(sd1)
print()

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=list('abcd'),
                     columns=['one', 'two', 'three', 'four'])
print(frame)
print()
print(frame.drop('a'))
print()
print(frame.drop('two', axis=1))
print()
print(frame.drop('two', axis='columns'))
print()
print(frame.drop(index='a', columns='one'))