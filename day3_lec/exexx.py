import pandas as pd
#
# a = pd.Series([10, 20, 30], index=['철수', '영희','민수'])
# print(a)
#
# print(a[0:2])
# print(a['영희'])

data = {
    '국어':[100, 80, 70],
    '영어':[70, 90, 85],
    '수학':[80, 70, 90]
}

df = pd.DataFrame(data, index=['철수','다은','민수'])
print(df)
print(df.loc[['민수']])
print()
# print(df[['국어','수학']])
# print(df.loc[['철수', '민수']])

print(df[df['수학'] >= 80])

df['총점'] = df['국어'] + df['수학'] + df['영어']

print(df)