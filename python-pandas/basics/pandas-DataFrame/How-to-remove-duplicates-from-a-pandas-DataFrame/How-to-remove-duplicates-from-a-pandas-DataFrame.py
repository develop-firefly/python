# Drop Duplicates using drop_duplicates() method
'''
Important argument for drop_duplicates() is keep, which has three possible options:

first: (default) Drop duplicates except for the first occurrence.
last: Drop duplicates except for the last occurrence.
False: Drop all duplicates.

e.g.
dataframe.drop_duplicates(inplace=True, keep=first)
dataframe.drop_duplicates(inplace=True, keep=last)
dataframe.drop_duplicates(inplace=True, keep=False)
'''

import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

print(f'my_df_has_duplicates: \n {_my_df} \n {_my_df.shape}')
print('-------------------------------------------------------------')
print()
print('-------------------------------------------------------------')
print(f'Dropping Duplicates: \n {_my_df.drop_duplicates()} \n {(_my_df.drop_duplicates()).shape}')

# Output
'''
my_df_has_duplicates: 
     Name         Sex  Age  Height (in)  Weight (lbs)
0   Alex         "M"   41           74           170
1   Bert         "M"   42           68           166
2   Carl         "M"   32           70           155
3   Dave         "M"   39           72           167
4   Elly         "F"   30           66           124
5   Fran         "F"   33           66           115
6   Gwen         "F"   26           64           121
7   Hank         "M"   30           71           158
8   Ivan         "M"   53           72           175
9   Jake         "M"   32           69           143
10  Kate         "F"   47           69           139
11  Luke         "M"   34           72           163
12  Myra         "F"   23           62            98
13  Neil         "M"   36           75           160
14  Omar         "M"   38           70           145
15  Page         "F"   31           67           135
16  Quin         "M"   29           71           176
17  Ruth         "F"   28           65           131
18  Page         "F"   31           67           135
19  Quin         "M"   29           71           176
20  Ruth         "F"   28           65           131 
 (21, 5)
-------------------------------------------------------------
-------------------------------------------------------------
Dropping Duplicates: 
     Name         Sex  Age  Height (in)  Weight (lbs)
0   Alex         "M"   41           74           170
1   Bert         "M"   42           68           166
2   Carl         "M"   32           70           155
3   Dave         "M"   39           72           167
4   Elly         "F"   30           66           124
5   Fran         "F"   33           66           115
6   Gwen         "F"   26           64           121
7   Hank         "M"   30           71           158
8   Ivan         "M"   53           72           175
9   Jake         "M"   32           69           143
10  Kate         "F"   47           69           139
11  Luke         "M"   34           72           163
12  Myra         "F"   23           62            98
13  Neil         "M"   36           75           160
14  Omar         "M"   38           70           145
15  Page         "F"   31           67           135
16  Quin         "M"   29           71           176
17  Ruth         "F"   28           65           131 
 (18, 5)

'''


# Drop Duplicates using drop_duplicates() method with inplace=True
# This changes the current dataframe, and avoids the need to either create a new dataframe or reuse the same name

import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

print(f'my_df_has_duplicates: \n {_my_df} \n {_my_df.shape}')
print('-------------------------------------------------------------')
print()
print(f'Dropping Duplicates: \n')
_my_df.drop_duplicates(inplace=True)
print('-------------------------------------------------------------')
print()
print(f'Shape of Existing DataFrame: \n {_my_df.shape}')

# Output
'''
my_df_has_duplicates: 
     Name         Sex  Age  Height (in)  Weight (lbs)
0   Alex         "M"   41           74           170
1   Bert         "M"   42           68           166
2   Carl         "M"   32           70           155
3   Dave         "M"   39           72           167
4   Elly         "F"   30           66           124
5   Fran         "F"   33           66           115
6   Gwen         "F"   26           64           121
7   Hank         "M"   30           71           158
8   Ivan         "M"   53           72           175
9   Jake         "M"   32           69           143
10  Kate         "F"   47           69           139
11  Luke         "M"   34           72           163
12  Myra         "F"   23           62            98
13  Neil         "M"   36           75           160
14  Omar         "M"   38           70           145
15  Page         "F"   31           67           135
16  Quin         "M"   29           71           176
17  Ruth         "F"   28           65           131
18  Page         "F"   31           67           135
19  Quin         "M"   29           71           176
20  Ruth         "F"   28           65           131 
 (21, 5)
-------------------------------------------------------------
Dropping Duplicates: 

-------------------------------------------------------------

Shape of Existing DataFrame: 
 (18, 5)
'''

