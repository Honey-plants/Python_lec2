import pandas as pd

tips = pd.read_csv('data/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

def g_func(gdata, n=5, column='tip_pct'):
    return gdata.sort_values(by=column, ascending=False)[:n]

print(tips.groupby('smoker').apply(g_func))         #tip_pct 기준으로 n개씩 불러옴
print()
print(tips.groupby(['smoker','day']).apply(g_func, n=3, column='total_bill'))