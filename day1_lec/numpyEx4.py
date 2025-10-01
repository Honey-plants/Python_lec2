import numpy as np

#=========1차원==========
arr1 = np.array([9,5,7,1,2,4,6,8])
print(arr1[0])
print(arr1[-1])         #역순도 가능
print(arr1[2:5])        #지역을 지정 할 수 있음
print()

#=========2차원==========
arr2 = np.array([[2,3,6,8],
                 [3,5,9,7],
                 [0,10,20,30]])
print(arr2)
print()
print(arr2[1,0])            #[행,열
print(arr2[1:,2:])