import pandas as pd
import numpy as np

data = {
    '번호' : [1,2,3,4,5,1,2,3,4,5],
    '반' : ['a','a','a','a','a','b','b','b','b','b'],
    '영어': [100,90,100, 80,70,90,100,70,80,90],
    '국어': [90, 80,90, 70, 100, 80, 90, 100, 70, 80],
    '수학': [80, 100, 80, 90, 80, 100, 70, 80, 90, 100]}

frame = pd.DataFrame(data, 
                     columns=['반', '번호', '국어', '영어', '수학'])

print(frame)
print()
frame.drop(['반','번호'],
           axis=1,
           inplace=True)

frame.loc['평균'] = frame.mean(axis=1)
print(frame)
frame.loc['평균'] = frame.mean(axis=0)
print(frame)
