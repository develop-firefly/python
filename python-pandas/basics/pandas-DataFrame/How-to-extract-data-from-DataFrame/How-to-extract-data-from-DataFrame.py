# Extracting Data from DataFrame
import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

# To get only the column names
print('DataFrame has the following columns: ', _my_df.columns)
print()
print('-------------------------------------------------------------')

# To extract data from a specific column in the DataFrame
print(_my_df['Name'])
print(type(_my_df['Name']))
print()
print('-------------------------------------------------------------')

# To extract data from a specific column in the DataFrame and convert the data to a list
print(_my_df['Name'].tolist())
print(type(_my_df['Name'].tolist()))
print()
print('-------------------------------------------------------------')

# Output
'''
DataFrame has the following columns:  Index(['Name', '     "Sex"', ' "Age"', ' "Height (in)"', ' "Weight (lbs)"'], dtype='object')

-------------------------------------------------------------
0     Alex
1     Bert
2     Carl
3     Dave
4     Elly
5     Fran
6     Gwen
7     Hank
8     Ivan
9     Jake
10    Kate
11    Luke
12    Myra
13    Neil
14    Omar
15    Page
16    Quin
17    Ruth
Name: Name, dtype: object
<class 'pandas.core.series.Series'>

-------------------------------------------------------------
['Alex', 'Bert', 'Carl', 'Dave', 'Elly', 'Fran', 'Gwen', 'Hank', 'Ivan', 'Jake', 'Kate', 'Luke', 'Myra', 'Neil', 'Omar', 'Page', 'Quin', 'Ruth']
<class 'list'>

-------------------------------------------------------------

'''