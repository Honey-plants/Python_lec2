import numpy as np

names = []
scores = []
while True:
    name = input('이름을 입력하세요:')
    names.append(name)
    score = list(map(int, input('성실성, 책임감, 협동성 점수를 입력하세요:').split()))
    scores.append(score)
    again = input('입력을 계속 진행하시겠습니가?(y/n)').lower()
    if again == 'n':
        break
arr_names = np.array(names)
arr_scores = np.array(scores)

info = input('정보를 조회할 직원 이름을 입력하세요:')
# if info == arr_names:
#     print(arr_scores)
print(arr_scores[info == arr_names])
print('평균점수:', arr_scores.mean())

# print(arr_names)
# print(arr_scores)
