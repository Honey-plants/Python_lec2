import numpy as np

arr1 = np.arange(0, 10, 1)
print(arr1)
print(type(arr1))
print()

arr1 = np.arange(0, 10)
print(arr1)
print(type(arr1))
print()

arr1 = np.arange(10)
print(arr1)
print(type(arr1))
print()

#결과는 다 같음

arr4 = np.linspace(-3, 3, 5)
print(arr4)
print(type(arr4))

arr5 = np.ones([3,4]) # 안에 리스트 써도 되고 튜플 써도 됨, 크기를 구분한다
print(arr5)

arr6 = np.zeros([3,4])
print(arr6)

arr7 = np.empty([3,4])  #가장 최근에 할당된 값을 가져옴 / 권장하지 않음
print(arr6)

arr8 = np.full([2,3], 100)      #특정값을 써서 초기화하고 싶을때
print(arr8)

arr9 = np.ones_like(arr8)           #형태를 가져온다
print(arr9)

arr10 = np.zeros_like(arr8)
print(arr10)

arr11 = np.full_like(arr8, 50)
print(arr11)
