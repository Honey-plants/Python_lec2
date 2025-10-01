import numpy as np
import pandas as pd

# obj1 = pd.Series(np.arange(4), index=list('dabc'))
# print(obj1)
# print()
# print(obj1.sort_index())
# print()
# print()
#
# frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
#                       index=['three', 'one'],
#                       columns=list('dabc'))
# print(frame1)
# print(frame1.sort_index())
# print()
# print(frame1.sort_index(axis=1))
# print(frame1.sort_index(axis=1, ascending=False)) #오름차순
# print()

obj2 = pd.Series([4,7,-5,3])
print(obj2)
print()
print(obj2.sort_values())
print()

data = {'second':[4,7,-3,2], 'first':[0,1,0,1]}
frame2 = pd.DataFrame(data)
print(frame2)
print()
print(frame2.sort_values(by='second'))
print()
print(frame2.sort_values(by=['first', 'second']))   #쏘팅한 애들중에 같은값이 잇으면 또 소팅해라
print()
print(frame2.sort_values(by=['first', 'second'], ascending=[False, True]))
print()

