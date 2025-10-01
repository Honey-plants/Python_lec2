import numpy as np

# x = np.array([[1,2,3],[4,5,6]])
# y = np.array([[2,4], [-1,7], [8,9]])
# print(np.dot(x, y))

np.random.seed(12345)
data = np.random.randn(5,2)
print(data)
print()

data2 = np.random.normal(loc=10, scale=5, size=[100,3])
print(data2)
print(data2.mean())
print(data2.std())
print()

data4 = np.random.randint(low=1, high=10, size=[10,3])
print(data4)
print()

data4 = np.arange(10)
print(data4)
np.random.shuffle(data4)            #랜덤으로 섞기
print(data4)
print()

data5 = np.arange(10)
print(data5)
print(np.random.permutation(data5))     #원본을 참조해서 섞음
print(data5)
