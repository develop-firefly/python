# Adding an element to an existing pandas 'Series'

import pandas as pd

# Creating the 'Series' by directly adding python dictionary to the 'Series' constructor
# Creating a python dictionary
_my_dict = {'Win':'MS', 'RHEL':'Red Hat', 'Android': 'Google'}
pd_var_via_dict = pd.Series(_my_dict)
print('pd_var_via_dict: ')
print(pd_var_via_dict)
print()
print('pd_var_via_dict_data_type: ', type(pd_var_via_dict))
print('-------------------------------------------------------------------')
print()

# Accessing Individual Values from Keys in the pandas 'Series'
print('Win---->', pd_var_via_dict['Win'])
print('RHEL--->', pd_var_via_dict['RHEL'])
print('-------------------------------------------------------------------')
print()

# Adding an element to an existing pandas 'Series'
# It follows similar convension of - Adding new key-Value pairs to a dictionary
pd_var_via_dict['Mac'] = 'Apple'
print('pd_var_via_dict: ')
print(pd_var_via_dict)
print()


# Output

'''
pd_var_via_dict: 
Win             MS
RHEL       Red Hat
Android     Google
dtype: object

pd_var_via_dict_data_type:  <class 'pandas.core.series.Series'>
-------------------------------------------------------------------

Win----> MS
RHEL---> Red Hat
-------------------------------------------------------------------

pd_var_via_dict: 
Win             MS
RHEL       Red Hat
Android     Google
Mac          Apple
dtype: object
'''