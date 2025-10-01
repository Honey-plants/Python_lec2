import numpy as np

scores = []
names = []
while True:
    name = input('이름을 입력하세요:')
    names.append(name)
    score = list(map(int, input('국어 영어 수학 점수를 입력하세요:').split()))
    scores += [score]
    # print(name, score)
    # print(names, scores)
    i = input('입력을 계속 진행하시겠습니까?(y/n)').lower()
    if i == 'n':
        break


arr_names = np.array(names)
arr_scores = np.array(scores)
print(arr_scores)
# print(arr_names)
i_name = input('출력할 학생의 이름을 입력하세요:')

print(arr_scores[arr_names == i_name])



# arr_scores = np.array(scores)
# print('국어점수:',arr_scores[0:,0])
# print('영어점수:',arr_scores[0:,1])
# print('수학점수:',arr_scores[0:,2])






