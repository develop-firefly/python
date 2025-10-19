# Remove an element with specific key from an existing pandas 'Series'
# This approach creates a new Series object or reuses the name of the existing Series object

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

# Accessing Individual Values from Keys in the pandas 'Series'
print('Win---->', pd_var_via_dict['Win'])
print('Mac--->', pd_var_via_dict['Mac'])
print('-------------------------------------------------------------------')
print()

# Deleting an existing pandas 'Series'
# It follows similar convension of - Removing a key-Value pairs from a dictionary
pd_var_via_dict = pd_var_via_dict.drop('Mac')
print('pd_var_via_dict: ')
print(pd_var_via_dict)
print()


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

Win----> MS
Mac---> Apple
-------------------------------------------------------------------

pd_var_via_dict: 
Win             MS
RHEL       Red Hat
Android     Google
dtype: object
'''

# Their is another way, where no new Series object is returned
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
pd_var_via_dict.drop('Mac', inplace=True)                                   # Removes this key and its corresponding value from this Series
print(pd_var_via_dict)
print()
print('pd_var_via_dict_data_type: ', type(pd_var_via_dict))

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

pd_var_via_dict: 
Win             MS
RHEL       Red Hat
Android     Google
dtype: object

'''