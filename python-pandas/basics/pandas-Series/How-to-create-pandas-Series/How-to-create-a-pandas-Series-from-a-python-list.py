# How to create a pandas 'Series' from a python list

import pandas as pd

# Creating the 'Series' by directly adding elements to the 'Series' constructor
pd_var = pd.Series([10,2000,350,900,625])
print('pd_var: ', pd_var)

print()
print('pd_var_data_type: ', type(pd_var))
print('-------------------------------------------------------------------')

# Creating the 'Series' by passing a python list to the 'Series' constructor
# Create a python list
_my_lst=[10,2000,350,900,625]
pd_var_via_list = pd.Series(_my_lst)
print('pd_var_via_list: ', pd_var_via_list)
print()
print('pd_var_via_list_data_type: ', type(pd_var_via_list))


# Output
'''
pd_var:  0      10
1    2000
2     350
3     900
4     625
dtype: int64

pd_var_data_type:  <class 'pandas.core.series.Series'>
-------------------------------------------------------------------
pd_var_via_list:  0      10
1    2000
2     350
3     900
4     625
dtype: int64

pd_var_via_list_data_type:  <class 'pandas.core.series.Series'>
'''


# How to create a pandas 'Series' from a python list
# 'Series' constructor can optionally take a list of indices as well


# Creating the 'Series' by directly adding elements to the 'Series' constructor
pd_var = pd.Series([10,2000,350,900,625], ['Red', 'Blue', 'Green', 'Yellow', 'White'])
print('pd_var: ')
print(pd_var)

print()
print('pd_var_data_type: ', type(pd_var))

# Output
'''
pd_var: 
Red         10
Blue      2000
Green      350
Yellow     900
White      625
dtype: int64

pd_var_data_type:  <class 'pandas.core.series.Series'>
'''