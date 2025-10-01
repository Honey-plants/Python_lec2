import numpy as np

np.random.seed(12345)

values = np.array([5,0,1,3,2])
indexer = values.argsort()              #인덱스 값으로 정렬
print(values)
print(indexer)
print(values[indexer])
print()

arr = np.random.randn(3,5)
arr[0] = values
print(arr)
print()
print(arr[:,arr[0].argsort()])