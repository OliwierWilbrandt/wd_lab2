import pandas as pd
import numpy as np
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
print(s)
data = {'Kraj': ['Belgia','Indie','Brazylia'],
        'Stolica':['Bruksela','New Delhi','Brasilia'],
        'Populacja': [11190846,1303171035,207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
df = pd.read_csv('dane.csv', header=0, sep=";", decimal='.')
print(df)
df.to_csv('plik.csv', index=False)