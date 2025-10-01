import pandas as pd
import numpy as np

myindex = ['김구','이봉창','안중근','윤봉길']
mycolumns = ['강남구','은평구','마포구','용산구']
mylist = list(10 * onedata for onedata in range(1, 17))

frame = pd.DataFrame(np.reshape(mylist, (4,4)),
                     index=myindex,
                     columns=mycolumns)
print(frame)
print()
print(frame.iloc[[0]])          #데이타 프레임 형식으로 출력
print(frame.iloc[0])            #시리즈 형식으로 출력
print()
print(frame.iloc[[1, 3]])
print()
print(frame.loc[['윤봉길']])
print()
print(frame.loc[['이봉창','윤봉길']])
print()
print(frame.loc[['윤봉길'],['은평구']])
print()
print(frame.loc[['김구','이봉창'],['용산구','은평구']])
print()
print(frame.loc[frame['은평구']<= 100])
print()
print(frame.loc[frame['은평구'] == 100])
print()
frame.loc['김구':'안중근', ['용산구']] = 80
print(frame)
