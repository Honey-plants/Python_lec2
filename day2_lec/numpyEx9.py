print('=====리스트 컴프리헨션=====')
import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [x if c else y for x,y,c in zip(xarr, yarr, cond)]
#zip = 여러개의 리스트들을 같은 인덱스끼리 묶음
#삼항 조건연산자

print(result)
print()

# result5 = []
# for x,y,c in zip(xarr, yarr, cond):
#     if c == True:
#         result5.append(x)
#     else:
#         result5.append(y)
# print(result5)


result2 = np.where(cond, xarr, yarr)
print(result2)
print()

np.random.seed(12345)
arr =np.random.randn(4, 4)
print(arr)

print(np.where(arr > 0, 2, -2))
print()
print(np.where(arr >0, 2, arr))
print()

data = np.array([2,3,5,7,8,7,3,7])
print(np.where(data == 7))             #인덱스 위치를 찾을때도 where 사용