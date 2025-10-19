# Retrieve rows based on a condition from a pandas 'Series'

import pandas as pd
import numpy as np

# Creating a Series using two lists generated with the help of random method of numpy
_roll = np.random.randint(1000, 1200, size=10)
_score = np.random.randint(50, 100, size=10)
print()

# Creating the pandas Series
pd_var=pd.Series(_score, _roll)
print('pd_var: ')
print(pd_var)
print('-------------------------------------------------------------------')
print()

# Retrieve values based on condition - Where scores if >= 70
# Create a new object
_First_Class = pd_var[pd_var >= 70]
print('_First_Class: ')
print(_First_Class)

# Output
'''
pd_var: 
1016    56
1008    66
1066    96
1143    68
1056    66
1082    69
1002    79
1086    51
1034    60
1013    89
dtype: int32
-------------------------------------------------------------------

_First_Class: 
1066    96
1002    79
1013    89
dtype: int32
'''