import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(1000,3),
                     columns=['first','second','third'])
print(frame)
frame.iloc[:4,[1,2]] = np.nan
print()
print(frame)
print()

print(frame.sum())
print()
print(frame.sum(skipna=False))
print()
print(frame.mean())
print()
print(frame.std())          #스탠다드함수
print()
print(frame.describe())
print()
frame.info()                #어떤 특성으로부터 무엇을 가지고 있는지 확인을 할 수 있음
print()

print(frame.head(15))       #앞에 있는거 () 가져와 작성하지 않으면 5개가 디폴트
print()
print(frame.tail(10))       #역순