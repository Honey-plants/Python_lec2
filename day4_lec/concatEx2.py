import pandas as pd

df1 = pd.DataFrame({
    '매출': [10, 12, 90, 60, 80, 11],
    '비용': [15,13, 12, 90, 99, 95]},
    index=['1월','2월','3월','4월','5월','6월'])
df2 = pd.DataFrame({
    '매출': [13, 14, 17, 15, 16, 16],
    '비용': [11,13, 12, 90, 99, 95]},
    index=['7월','8월','9월','10월','11월','12월'])

df3 =pd.concat([df1, df2])
print()
df3['이익'] = df3['매출'] - df3['비용']
print(df3)
print()

df3.loc['실적'] = df3.sum()
print(df3)