# Change value for a specific key in pandas 'Series'

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

# Changing one value based on its key in pandas 'Series'
pd_var_via_dict['Win'] = "Microsoft"
print('pd_var_via_dict after chaging the value: ')
print(pd_var_via_dict)

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

pd_var_via_dict after chaging the value: 
Win        Microsoft
RHEL         Red Hat
Android       Google
Mac            Apple
dtype: object
'''