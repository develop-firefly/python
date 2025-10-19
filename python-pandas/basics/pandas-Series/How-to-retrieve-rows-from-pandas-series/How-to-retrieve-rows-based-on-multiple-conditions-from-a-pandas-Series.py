# Retrieve rows based on multiple conditions from a pandas 'Series'

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

# Retrieve Values based on multiple conditions : Where scores > 70 and < 90
_close_to_elite = pd_var[(pd_var > 70) & (pd_var < 90)]
print('_close_to_elite: ')
print(_close_to_elite)

# Output

'''
pd_var: 
1038    92
1093    63
1007    73
1000    85
1097    88
1180    68
1143    79
1175    83
1059    57
1131    83
dtype: int32
-------------------------------------------------------------------

_close_to_elite: 
1007    73
1000    85
1097    88
1143    79
1175    83
1131    83
dtype: int32
'''