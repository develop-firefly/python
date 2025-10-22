# How to combine two pandas Series

import pandas as pd

# Create two pandas series, using python lists
pd_s1 = pd.Series([10, 20, 30, 40, 50], ['p1', 'p2', 'p3', 'p4', 'p6'])
pd_s2 = pd.Series([5,15,25,35, 45], ['p1', 'p2', 'p4', 'p5', 'p7'])

print('pd_s1 :', pd_s1)
print()
print('pd_s2 :', pd_s2)
print('-------------------------------------------------------------------')
print()

pd_combine = pd_s1.combine_first(pd_s2)
print('pd_combine :', pd_combine)

# combine_first() takes all the values from the caller, and uses only those values, if they are not in the caller Series

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

pd_combine : p1    10.0
p2    20.0
p3    30.0
p4    40.0
p5    35.0
p6    50.0
p7    45.0
dtype: float64
'''

#-------------------------------------------------------------------------------------------------------------------------
# How to combine two pandas Series based on condition

import pandas as pd

# Create two pandas series, using python lists
pd_s1 = pd.Series([10, 20, 30, 40, 50], ['p1', 'p2', 'p3', 'p4', 'p5'])
pd_s2 = pd.Series([5,15,25,35, 690], ['p1', 'p2', 'p3', 'p4', 'p5'])

print('pd_s1 :', pd_s1)
print()
print('pd_s2 :', pd_s2)
print('-------------------------------------------------------------------')
print()
pd_combine = pd_s1.combine(pd_s2, (lambda x1, x2:max(x1, x2)))
print('pd_combine: ')
print(pd_combine)


# Output:
'''
pd_s1 : p1    10
p2    20
p3    30
p4    40
p5    50
dtype: int64

pd_s2 : p1      5
p2     15
p3     25
p4     35
p5    690
dtype: int64
-------------------------------------------------------------------

pd_combine: 
p1     10
p2     20
p3     30
p4     40
p5    690
dtype: int64
​
'''

#-------------------------------------------------------------------------------------------------------------------------
# How to combine two pandas Series based on condition - Along with fill-value

import pandas as pd

# Create two pandas series, using python lists
pd_s1 = pd.Series([10, 20, 30, 40, 50], ['p1', 'p2', 'p3', 'p4', 'p5'])
pd_s2 = pd.Series([5,15,25,35, 690], ['p1', 'p2', 'p4', 'p5', 'p7'])

print('pd_s1 :', pd_s1)
print()
print('pd_s2 :', pd_s2)
print('-------------------------------------------------------------------')
print()
pd_combine = pd_s1.combine(pd_s2, (lambda x1, x2:max(x1, x2)), fill_value=0)
print('pd_combine: ')
print(pd_combine)

# Output:
'''
pd_s1 : p1    10
p2    20
p3    30
p4    40
p5    50
dtype: int64

pd_s2 : p1      5
p2     15
p4     25
p5     35
p7    690
dtype: int64
-------------------------------------------------------------------

pd_combine: 
p1     10
p2     20
p3     30
p4     40
p5     50
p7    690
dtype: int64
'''
