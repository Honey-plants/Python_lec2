import pandas as pd

tips = pd.read_csv('data/tips.csv')
print(tips.head(10))
tips.info()
print()

tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head())
print()

grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.mean())
print()
print(grouped_pct.agg('mean'))              #mean 이랑 같은 방법
print('=====================')
print(grouped_pct.agg(['mean', 'std']))
print()
print(grouped_pct.agg([('gmean', 'mean'), 'std']))      #이름바꾸는방법
print()

print('=====여러 데이터 가져오기=====')
print(grouped.agg({'tip':'max', 'size':'sum'}))
print()

print(grouped.agg({'tip_pct':['min','max'],
                   'size':['sum','mean','std']}))

