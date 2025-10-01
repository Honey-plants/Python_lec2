import numpy as np

np.random.seed(12345)
arr = np.random.randn(5,5)
print(arr)
print()

print(f'평균: {arr.mean()}')
print(f'평균: {np.mean(arr)}')        #평균 구하기
print(f'표준편차: {arr.std()}')
print(f'분산: {arr.var()}')
print(f'합: {arr.sum()}')
print()

print(f'열 평균: {arr.mean(axis=0)}')      #열 = 0 행 = 1 일단은 그렇게 생각하기
print(f'행 평균: {arr.mean(axis=1)}')      #열 = 0 행 = 1 일단은 그렇게 생각하기
print()

arr2 = np.arange(10)
print(arr2)
print(arr2.cumsum())                    #누적된 값을 하나나씩 더해서 출력
print()

arr3 = np.array([[0,1,2],
                [3,4,5],
                [6,7,8]])
print(arr3)
print(f'열 누적합:\n{arr3.cumsum(axis=0)}')
print(f'열 누적곱:\n{arr3.cumprod(axis=0)}')