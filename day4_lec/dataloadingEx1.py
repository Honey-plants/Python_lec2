import pandas as pd

frame1 = pd.read_csv('data/ex1.csv')
print(frame1)
print(type(frame1))
print()
#== 기존 데이터 첫번째를 헤더로 인식해 버리기 때문에 None 을써서 일반 데이터로 만들기==
frame2 = pd.read_csv('data/ex2.csv', header=None)
print(frame2)
print()

frame3 = pd.read_csv('data/ex2.csv',
                     names=['one','two','three','four','msg'])
print(frame3)
print()

frame3 = pd.read_csv('data/ex2.csv',
                     names=['one','two','three','four','msg'],
                     index_col='msg')       #index_col = 인덱스로 사용할 열 지정
print(frame3)
print()

frame3 = pd.read_csv('data/ex2.csv',
                     names=['one','two','three','four','msg'],
                     index_col=4)               #인덱스로도 지정 가능
print(frame3)
print()
print()

#==주석처리된 것 안보이게 출력==
frame4 = pd.read_csv('data/ex4.csv', skiprows=[0,2,3])   # skiprow = 주석처리된 행 삭제
print(frame4)
