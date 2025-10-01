import pandas as pd
import numpy as np

states = ['ohio','new york','vermont','florida',
          'oregon','nevada','california','idaho']
data = pd.Series(np.random.randn(8), index=states)
data[['vermont', 'nevada', 'idaho']] = np.nan
print(data)
print()

group_label = ['East'] * 4 + ['West'] * 4
print(group_label)
print()
print(data.groupby(group_label).mean())
print('==============================')

fill_mean = lambda g: g.fillna(g.mean())
print(data.groupby(group_label).apply(fill_mean))
