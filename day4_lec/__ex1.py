import pandas as pd

frame1 = pd.read_csv('data/ex1.csv')
print(frame1)
print(type(frame1))
print()

frame2 = pd.read_csv('data/ex2.csv',header=None)
print(frame2)
print()

fram3 = pd.read_csv('data/ex2.csv',
                    names=['one','two','three','four','msg'])
print(fram3)
print()

fram3 = pd.read_csv('data/ex2.csv',
                    names=['one','two','three','four','msg'],
                    index_col='msg')
print(fram3)
fram3 = pd.read_csv('data/ex2.csv',
                    names=['one','two','three','four','msg'],
                    index_col=4)
print(fram3)
print()

frame4 = pd.read_csv('data/ex4.csv', skiprows=[0,2,3])
print(frame4)
