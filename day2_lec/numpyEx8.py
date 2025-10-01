import numpy as np

arr = np.arange(8)
print(arr)
print()

arr2 = arr.reshape([4,2])
print(arr)
print(arr2)
print()

print(arr2.T)       # 열이 행으로 바뀜 transpose 약자
print()

ldata = [10,20,30,40,50,60]
arr3 = np.reshape(ldata, [3,2])
print(arr3)