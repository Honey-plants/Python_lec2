import pandas as pd
#
# frame = pd.read_excel('data/monthly_sales.xlsx')
# print(frame)
# print()
#
# #====head 랑 index  다시 지정해줌
# frame = pd.read_excel('data/monthly_sales.xlsx',
#                       header=1,
#                       index_col=0)
# print(frame)
# print()
#
frame2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name='2학년')
print(frame2)
print()

frame2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name=0)
print(frame2)
print()

data = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name=None)
print(data)
print()
print(data['1학년'])
print()

data2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name=['1학년','2학년'])
print(data2)
# 엑셀은 안쓰는게 베스트 csv 파일로 통일해서 써라, 너무너무 느림

import numpy as np

frame3 = pd.DataFrame(np.random.randn(100,4),
                      columns=['seoul','busan','inchoen', 'suwon'])
print(frame3)
frame3.to_csv('sfile.csv')
frame3.to_csv('sfile2.csv', index=False)
