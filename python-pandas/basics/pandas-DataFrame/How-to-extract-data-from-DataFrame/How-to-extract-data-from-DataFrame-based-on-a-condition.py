# Extracting Data from DataFrame based on a condition
import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

print('-------------------------------------------------------------')
print('Original Dataframe: ')
print(_my_df)
print()
print('-------------------------------------------------------------')
print('Extract Data from DataFrame based on condition by value')
print(_my_df.loc[_my_df["Name"] == "Gwen"])
print()
print('-------------------------------------------------------------')
print('Extract Data from DataFrame based on condition by value')
print(_my_df.loc[_my_df["Age"] > 30])
print()
print('-------------------------------------------------------------')
print('Extract Data from DataFrame based on condition by value and print only selected columns')
print(_my_df.loc[_my_df["Age"] > 30][['Name', 'Age', 'Sex']])
print()
print('-------------------------------------------------------------')




# Output
'''

-------------------------------------------------------------
Original Dataframe: 
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

-------------------------------------------------------------
Extract Data from DataFrame based on condition by value
   Name         Sex  Age  Height (in)  Weight (lbs)
6  Gwen         "F"   26           64           121

-------------------------------------------------------------
Extract Data from DataFrame based on condition by value
    Name         Sex  Age  Height (in)  Weight (lbs)
0   Alex         "M"   41           74           170
1   Bert         "M"   42           68           166
2   Carl         "M"   32           70           155
3   Dave         "M"   39           72           167
5   Fran         "F"   33           66           115
8   Ivan         "M"   53           72           175
9   Jake         "M"   32           69           143
10  Kate         "F"   47           69           139
11  Luke         "M"   34           72           163
13  Neil         "M"   36           75           160
14  Omar         "M"   38           70           145
15  Page         "F"   31           67           135

-------------------------------------------------------------
Extract Data from DataFrame based on condition by value and print only selected columns
    Name  Age         Sex
0   Alex   41         "M"
1   Bert   42         "M"
2   Carl   32         "M"
3   Dave   39         "M"
5   Fran   33         "F"
8   Ivan   53         "M"
9   Jake   32         "M"
10  Kate   47         "F"
11  Luke   34         "M"
13  Neil   36         "M"
14  Omar   38         "M"
15  Page   31         "F"

-------------------------------------------------------------

'''