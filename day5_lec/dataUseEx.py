import numpy as np
import pandas as pd

fec = pd.read_csv('data/P00000001-ALL.csv')
# print(fec.head())       # 오바마 시절 후원자 목록
fec.info()
print()
print(fec.iloc[7])
print()

print('=====\'후보자 이름 가져오기\'=====')
print(fec.cand_nm.unique())

parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt':'Republican',
           'Huntsman, Jon':'Republican',
           'Johnson, Gary Earl':'Republican',
           'McCotter, Thaddeus G':'Republican',
           'Obama, Barack':'Democrat',
           'Paul, Ron':'Republican',
           'Pawlenty, Timothy':'Republican',
           'Perry, Rick':'Republican',
           "Roemer, Charles E. 'Buddy' III":'Republican',
           'Romney, Mitt':'Republican',
           'Santorum, Rick':'Republican'}

print()

print('=====기존 파일에 정당 붙이기=====')
fec['party'] = fec.cand_nm.map(parties)
#fec['party'] = fec.cand_nm.map(lambda x : parties[x)
print(fec.head())

print('=====정당 기준으로 분류하기=====')
print(fec['party'].value_counts())
print()

print('=====환급한 사람들 제외시키기=====')
fec = fec[fec.contb_receipt_amt > 0]
fec.info()
print()

print(fec.contbr_occupation.value_counts()[:10])

occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
    'C.E.O':'CEO',
    'C.E.O.':'CEO'
}

cf = lambda x : occ_mapping.get(x, x)
fec.contbr_occupation = fec.contbr_occupation.map(cf)
print(fec.contbr_occupation.value_counts()[:10])
print()
by_occupation = fec.pivot_table(values='contb_receipt_amt',
                                index='contbr_occupation',
                                columns='party',
                                aggfunc='sum')
print(by_occupation)

print('=====각 직업별로 기부금합이 2,000,000,넘는 애들만 가져와=====')
over_2mm = by_occupation[by_occupation.sum(axis=1) > 2000000]
print(over_2mm)

# import matplotlib.pyplot as plt
# over_2mm.plot(kind='barh')
# plt.show()
print('=====2명의 유력 후보자 데이터 가져오기=====')
fec_mrbo =fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
fec_mrbo.info()
print()
print('=====후보자별로 그룹화하여 가장 많이 기부한 직업들=====')
print(fec_mrbo.cand_nm.unique())

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]

grouped = fec_mrbo.groupby('cand_nm')
print(grouped.apply(get_top_amounts, key='contbr_occupation', n=7))
print()
print('=====기부한 금액을 구간별로 나누기 =====')

bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
print(labels)
print()

grouped = fec_mrbo.groupby(['cand_nm', labels])
bucket_sums = grouped.contb_receipt_amt.sum().unstack(level=0)
print(bucket_sums)
print()

normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
print(normed_sums)
print()

import matplotlib.pyplot as plt
normed_sums[:-2].plot(kind='barh')
plt.show()
