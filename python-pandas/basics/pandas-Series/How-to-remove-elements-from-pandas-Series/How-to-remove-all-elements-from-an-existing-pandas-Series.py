# Remove all elements from an existing pandas 'Series'

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

# Removing all the elements
pd_var_via_dict.drop(pd_var_via_dict.index[...], inplace=True)
print('pd_var_via_dict after removal of all elements: ', pd_var_via_dict)

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

pd_var_via_dict after removal of all elements:  Series([], dtype: object)

'''