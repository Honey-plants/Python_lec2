import numpy as np

arr1 = np.array([[1,2,7], [6,7,9]])
print(arr1)
print()

barr1 = np.array([[True, False, True],
                  [False, False, True]])
print(barr1)
print()

print(arr1[barr1])              #True 에 해당하는 부분을 가져옴
print()                         #arr1 에 특정한 값을 뽑아 오는 거기 때문에 인덱스를 쓰는것과 같이 []

barr2 = np.array([False, True])
print(barr2)
print()
print(arr1[barr2])              #0번행, 1번행 이라고 보면된다.

barr3 = np.array([True, False, True])
print(barr3)
print()
print(arr1[:, barr3])           #,앞에는 행 그 뒤에는 열

