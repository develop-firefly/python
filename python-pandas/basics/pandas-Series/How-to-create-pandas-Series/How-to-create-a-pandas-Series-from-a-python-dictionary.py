# How to create a pandas 'Series' from a python dictionary

import pandas as pd

# Creating the 'Series' by directly adding key-value pairs to the 'Series' constructor
pd_var = pd.Series({'Win':'MS', 'RHEL':'Red Hat', 'Android': 'Google'})
print('pd_var: ')
print(pd_var)
print()
print('pd_var_data_type: ', type(pd_var))
print('-------------------------------------------------------------------')
print()

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


# Output:
'''
pd_var: 
Win             MS
RHEL       Red Hat
Android     Google
dtype: object

pd_var_data_type:  <class 'pandas.core.series.Series'>
-------------------------------------------------------------------

pd_var_via_dict: 
Win             MS
RHEL       Red Hat
Android     Google
dtype: object

pd_var_via_dict_data_type:  <class 'pandas.core.series.Series'>
-------------------------------------------------------------------

Win----> MS
RHEL---> Red Hat

'''