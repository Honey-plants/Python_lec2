import numpy as np

np.random.seed(12345)           #같은씨앗은 같은 값을 나오게 하기 때문에 값고정을 위해 seed(숫자)를씀
data = np.random.randn(7,4)
print(data)
print()

names = np.array(['bob','joe','will','bob','will','joe','joe'])
# print(names)
# print()
# print(names == 'bob')           #행을 쓸때
# print()
# print(data[names =='bob'])        #1차원배열 불린인덱스는 '행기준'
# print()
# print(data[names =='bob', 2:])
# print()
# print(data[names =='bob', 3])
# print()

print(data<0)
print()
print(data[data<0])
print()

data[data < 0] = 0
print(data)