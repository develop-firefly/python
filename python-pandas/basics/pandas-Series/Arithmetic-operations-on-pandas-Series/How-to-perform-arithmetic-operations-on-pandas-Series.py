# Arithmetic Operations on Pandas Series

import pandas as pd

# Create two pandas series, using python lists
pd_s1 = pd.Series([10, 20, 30, 40, 50])
pd_s2 = pd.Series([5,15,25,35, 45])

# Addition operation on pandas Series
pd_sum = pd_s1 + pd_s2
print('pd_sum: ', pd_sum)
print('-------------------------------------------------------------------')
print()

# Subraction operation on pandas Series
pd_sub = pd_s1 - pd_s2
print('pd_sub: ', pd_sub)
print('-------------------------------------------------------------------')
print()

# Multiplication operation on pandas Series
pd_mul = pd_s1 * pd_s2
print('pd_mul: ', pd_mul)
print('-------------------------------------------------------------------')
print()

# Division operation on pandas Series
pd_div = pd_s1 / pd_s2
print('pd_div: ', pd_div)


# Output
'''
pd_sum:  0    15
1    35
2    55
3    75
4    95
dtype: int64
-------------------------------------------------------------------

pd_sub:  0    5
1    5
2    5
3    5
4    5
dtype: int64
-------------------------------------------------------------------

pd_mul:  0      50
1     300
2     750
3    1400
4    2250
dtype: int64
-------------------------------------------------------------------

pd_div:  0    2.000000
1    1.333333
2    1.200000
3    1.142857
4    1.111111
dtype: float64
'''

# Arithmetic Operations on Pandas Series with index


import pandas as pd

# Create two pandas series, using python lists
pd_s1 = pd.Series([10, 20, 30, 40, 50], ['p1', 'p2', 'p3', 'p4', 'p6'])
pd_s2 = pd.Series([5,15,25,35, 45], ['p1', 'p2', 'p4', 'p5', 'p7'])

print('pd_s1 :', pd_s1)
print('pd_s2 :', pd_s2)
print('-------------------------------------------------------------------')
print()

# Addition operation on pandas Series
pd_sum = pd_s1 + pd_s2
print('pd_sum_without_fill_value: ', pd_sum)
print('-------------------------------------------------------------------')
print()

# Addition operation on pandas Series using pd.Series.add
pd_sum = pd.Series.add(pd_s1, pd_s2, fill_value=0)
print('pd_sum_with_pd_series_add_and_Fill_value: ', pd_sum)
print('-------------------------------------------------------------------')
print()


# Output
'''
pd_s1 : p1    10
p2    20
p3    30
p4    40
p6    50
dtype: int64
pd_s2 : p1     5
p2    15
p4    25
p5    35
p7    45
dtype: int64
-------------------------------------------------------------------

pd_sum_without_fill_value:  p1    15.0
p2    35.0
p3     NaN
p4    65.0
p5     NaN
p6     NaN
p7     NaN
dtype: float64
-------------------------------------------------------------------

pd_sum_with_pd_series_add_and_Fill_value:  p1    15.0
p2    35.0
p3    30.0
p4    65.0
p5    35.0
p6    50.0
p7    45.0
dtype: float64
-------------------------------------------------------------------
'''