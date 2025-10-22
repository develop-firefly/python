# To print first N rows from a pandas DataFrame

import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

# Default behaviour of head() - It prints the top 5 rows of DataFrame
print(_my_df.head())
print()
print('-------------------------------------------------------------')

# We can use an optional argument to limit the number of rows to override the default behavior
print(_my_df.head(n=3))
print()
print('-------------------------------------------------------------')

# Another way to print 'all' rows of the DataFrame
print(_my_df.head(n=len(_my_df)))
print()
print('-------------------------------------------------------------')

# Output

'''
   Name       "Sex"   "Age"   "Height (in)"   "Weight (lbs)"
0  Alex         "M"      41              74              170
1  Bert         "M"      42              68              166
2  Carl         "M"      32              70              155
3  Dave         "M"      39              72              167
4  Elly         "F"      30              66              124

-------------------------------------------------------------
   Name       "Sex"   "Age"   "Height (in)"   "Weight (lbs)"
0  Alex         "M"      41              74              170
1  Bert         "M"      42              68              166
2  Carl         "M"      32              70              155

-------------------------------------------------------------
    Name       "Sex"   "Age"   "Height (in)"   "Weight (lbs)"
0   Alex         "M"      41              74              170
1   Bert         "M"      42              68              166
2   Carl         "M"      32              70              155
3   Dave         "M"      39              72              167
4   Elly         "F"      30              66              124
5   Fran         "F"      33              66              115
6   Gwen         "F"      26              64              121
7   Hank         "M"      30              71              158
8   Ivan         "M"      53              72              175
9   Jake         "M"      32              69              143
10  Kate         "F"      47              69              139
11  Luke         "M"      34              72              163
12  Myra         "F"      23              62               98
13  Neil         "M"      36              75              160
14  Omar         "M"      38              70              145
15  Page         "F"      31              67              135
16  Quin         "M"      29              71              176
17  Ruth         "F"      28              65              131

-------------------------------------------------------------
'''