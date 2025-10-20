# How to create a pandas 'Series' with custom index labels

import pandas as pd

# Create a Python List
a = [1, 7, 2]
_index = ['x', 'y', 'z']

# Create a Series, by passing the list to pd.Series
# Use the optional argument - 'index' and use the values from _index
_my_pds = pd.Series(a, index = _index)

print(f"Pandas Series with custom index labels:- \n{_my_pds}")

# Output
'''
Pandas Series with custom index labels:- 
x    1
y    7
z    2
dtype: int64
'''