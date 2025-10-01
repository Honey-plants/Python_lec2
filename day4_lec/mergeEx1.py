import  pandas as pd

#
# frame1 = pd.DataFrame({'kdata':['b','b','a','c','a','a','b'],
#                        'data1':range(7)})
# frame2 = pd.DataFrame({'kdata':['a','b','d'],
#                        'data2':range(3)})
#
# print(frame1)
# print()
# print(frame2)
# print()
#
# print(pd.merge(frame1, frame2, on='kdata'))
# #how = inner : 내부조인, 키가 매칭되지 않으면 제외하겠다 라는것
# print(pd.merge(frame1, frame2, on='kdata', how="outer"))
# #how = 'outer 다 가져오기
# print()
# print(pd.merge(frame1, frame2, on='kdata', how="left"))
# print(pd.merge(frame1, frame2, on='kdata', how="right"))

frame3 = pd.DataFrame({'lkdata':['b','b','a','c','a','a','b'],
                       'data1':range(7)})
frame4 = pd.DataFrame({'rkdata':['a','b','d'],
                       'data2':range(3)})

print(pd.merge(frame3, frame4, left_on='lkdata', right_on='rkdata').drop('rkdata', axis=1))
