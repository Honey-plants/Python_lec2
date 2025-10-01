import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape(3,4),
                    index=['ohio', 'colorado', 'new york'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

data.index=data.index.map(str.upper)
print(data)
print()
print(data.rename(index=str.title, columns=str.upper))
print(data.rename(index={'OHIO':'INDIANA'},
                  columns={'three':'Third'}))