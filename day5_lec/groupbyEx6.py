import pandas as pd

tips = pd.read_csv('data/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

print(tips.pivot_table(values=['tip_pct', 'size'],
                       index=['sex', 'smoker'],
                       aggfunc='mean'))
print()
print(tips.pivot_table(values=['tip_pct', 'size'],
                       index=['sex', 'smoker'],
                       aggfunc=['mean', 'std']))
print()
print(tips.pivot_table(values=['tip_pct', 'size'],
                       index='day',
                       columns='sex',
                       aggfunc='sum'))
#즉흥적으로 쓰고싶을때 사용, 관리 하기가 힘들기 때문에 보통은 groupby 쓰기