import numpy as np
import pandas as pd

data = pd.Series([1, -999, 2, -999, -1000, 3])
print(data)

print(data.replace([-999, -1000], np.nan))
print(data.replace({-999:np.nan, -1000:0}))

