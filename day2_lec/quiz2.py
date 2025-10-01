import numpy as np

names = []
scores = []

while True:
    name = input('이름을 입력하세요:')
    names.append(name)
    score = list(map(int, input('국어 영어 수학 점수를 입력하세요:').split()))
    scores += [score]

    conti = (input('입력을 계속 진행 하시겠습니까?(y/n)'))
    if conti == 'n'.lower():
        break

ar_names = np.array(names)
ar_scores = np.array(scores)
print(ar_scores)

print(f'국어 총점{ar_scores.sum(axis=0)[0]}, 영어 총점{ar_scores.sum(axis=0)[1]}, 수학 총점{ar_scores.sum(axis=0)[2]}')

iarr_name = input('성적을 출력할 학생의 이름 입력')

print(ar_scores[ar_scores[:,2].argsort()])

