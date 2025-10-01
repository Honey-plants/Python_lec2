import numpy as np

ldata1 = [10,20,30,40]
print(ldata1)
print(type(ldata1))
print()

arr1 = np.array(ldata1)
print(arr1)
print(type(arr1))
print()

ldata2 = [[1,2,3,4], [5,6,7,8]]     #리스트객체 2개가 들어가 있는것 뿐
print(ldata2)
arr2 = np.array(ldata2)
print(arr2)
print(arr2.shape)
print(arr2.dtype)
print()

ldata3 = [10.4, 23, 5233.12, 11]
print(ldata3)
arr3 = np.array(ldata3, dtype=np.int32)
print(arr3)                         #다 실수로 바뀜 why? 같은타입이여야 해서
print(arr3.dtype)
print()

ldata4 = ['1.23', 33.23, 431]
print(ldata4)
arr4 = np.array(ldata4, dtype=np.float64)
print(arr4)
