import numpy as np
import pandas as pd

df = pd.DataFrame({
    '이름':['철수','영희','민수'],
    '수학':[90, 85, 75],
    '영어':[88, 92, 67],
    '과학':[95, 80, 85]
})

print(df)
print()
# print(df.set_index('이름').stack())
stacked = df.set_index('이름').stack()
print(stacked)
print()
df_reset = stacked.reset_index()
print(df_reset)
print(df_reset.columns)
df_reset.columns = ['이름','과목','점수']
print()