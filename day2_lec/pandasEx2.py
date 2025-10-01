import pandas as pd
import numpy as np

# np.random.seed(12345)

# frame1 = pd.DataFrame([[10,20,30], [50,60,70]])
# print(frame1)
# print()
#
# frame2 = pd.DataFrame([[10,20,30], [50,60,70]],
#                       index=['one', 'two'],
#                       columns=['first', 'second', 'third'])
# print(frame2)
# print()
# print(frame2.index)
# print(frame2.columns)
# print(frame2.values)
# print()
#
# ldata = [('김가',180,90), ('이가',160,50), ('최가',170,65), ('오가',165,60)]
# frame2 = pd.DataFrame(ldata,
#                       columns=['이름','키','몸무게'],
#                       index=[11,12,21,22])
# print(frame2)

ddata = {'state': ['ohio','ohio','nevada','nevada'],
         'year': [2020, 2021, 2022, 2023],
         'pop2': [1.5, 1.7, 3.6, 2.4]}

print(ddata)
print()

frame4 = pd.DataFrame(ddata)
print(frame4)
print()

frame5 = pd.DataFrame(ddata,
                      columns=['year','pop2','state'],
                      index=['one','two','three','four'])
print(frame5)
print()


print(frame5['state'])  # 시리즈 객체
print()
print(frame5.state)
print()
print(frame5.loc['two'])
print()

print(frame5['pop2']['two'])
print()
print(frame5.loc['two']['pop2'])
print()
print(frame5.loc['two'].pop2)

print(frame5)
print()
frame5['area'] = pd.Series([32.32,32.32,534.53,534.33])
print(frame5)
print()
frame5['area'] = [32.32, 32.32, 534.53, 534.53]
print(frame5)
print()

# frame5.loc['five'] = pd.Series([2020,3.3, 'utah',32.32],
#                                index=['year','tot2','state','area'])
# frame5.loc['five'] = pd.Series([2020,3.3, 'utah',32.32],
#                                index=frame5.columns)
frame5.loc['five'] = [2020, 3.3, 'utah', 32.32]
print(frame5)
print()

frame5.index.name = 'id'
frame5.columns.name = 'info'
print(frame5)