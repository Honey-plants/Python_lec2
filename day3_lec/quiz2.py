import pandas as pd

data = {
    '이름':['철수', '영희','민수'],
    '수학':[90, 60, 100],
    '영어':[80,75,95],
    '과학':[70,85,90]
}

df = pd.DataFrame(data)

#학생별 총점
print(df)
print()
df["총점"] = df.apply(lambda row: row[["수학", '영어','과학']].sum(), axis=1)


#과목별 평균
subject_mean = df[['수학','영어','과학']].apply(lambda col: col.mean(), axis=0)

print(df)
print("\n[과목별 평균]\n",
      subject_mean, sep='')

