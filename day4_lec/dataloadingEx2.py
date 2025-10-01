import pandas as pd
import numpy as np

#===chunksize : 한번에 읽을 행의 수를 지정 ===
# chunker = pd.read_csv('data/ex6.csv', chunksize=1000)
# print(chunker)
# print()
# for data in chunker:
#     print(data)

# sdata1 = pd.Series(['a','b','a','c','d','a','c'])
# print(sdata1)
# print()
# print(sdata1.value_counts())            #각 값이 몇개나 있는지 카운트
# 

chunker = pd.read_csv('data/ex6.csv', chunksize=1000)

tot = pd.Series([], dtype=np.float64)

for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

print(tot)
tot.sort_values(ascending=False, inplace=True)
print(tot[:10])


