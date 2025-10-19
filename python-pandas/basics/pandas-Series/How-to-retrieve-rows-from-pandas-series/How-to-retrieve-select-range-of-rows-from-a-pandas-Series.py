# Retrieve select range of rows from a pandas Series

import pandas as pd

# Creating the 'Series' by directly adding python dictionary to the 'Series' constructor
# Creating a python dictionary
_my_dict = {'Win':'MS', 'RHEL':'Red Hat', 'Android': 'Google', 'Mac':'Apple'}
pd_var_via_dict = pd.Series(_my_dict)
print('pd_var_via_dict: ')
print(pd_var_via_dict)
print()
print('pd_var_via_dict_data_type: ', type(pd_var_via_dict))
print('-------------------------------------------------------------------')
print()

# Retrieve select number of rows
print(pd_var_via_dict[1:3])
print('-------------------------------------------------------------------')
print()
print(pd_var_via_dict[2:])

# Output

'''
pd_var_via_dict: 
Win             MS
RHEL       Red Hat
Android     Google
Mac          Apple
dtype: object

pd_var_via_dict_data_type:  <class 'pandas.core.series.Series'>
-------------------------------------------------------------------

RHEL       Red Hat
Android     Google
dtype: object
-------------------------------------------------------------------

Android    Google
Mac         Apple
dtype: object
'''