import numpy as np

np.random.seed(12345)

arr = np.random.randn(100)
print((arr>0).sum())
print()

bools = np.array([[False, False, True, False],
                  [False, False, True, True]])
print(bools.sum())
print()
print(bools.any())
print(bools.any(axis=1))        #True 가 하나라도 있을때
print(bools.any(axis=0))
print(bools.all(axis=0))        #and 와 같은거라고 보면됨
print()

data = np.random.randn(10, 4) * 4
print(data)
print()

print(data[(data > 3).any(axis=1)])
print()
print(data[:,(data > 5).any(axis=0)])