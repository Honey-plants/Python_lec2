import numpy as np
import pandas as pd

df = pd.DataFrame({
    '이름': ['철수','영희','민수','길동','미나','수현'],
    '출석1': [20, np.nan, 15, np.nan, 18, np.nan],
    '출석2': [19, np.nan, 14, np.nan, 17, np.nan],
    '중간고사': [80, 90, np.nan, 75, np.nan, 88],
    '기말고사': [np.nan, 85, 88, np.nan, 70, np.nan]
})
print(df)
print()

df = df.dropna(subset=['출석1','출석2'])
print(df)