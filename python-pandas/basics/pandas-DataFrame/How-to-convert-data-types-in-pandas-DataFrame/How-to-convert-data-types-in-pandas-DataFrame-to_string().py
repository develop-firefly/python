# Read a CSV using Pandas and convert the data to string
import pandas as pd

# Create a Dataframe by reading the csv file
_my_df = pd.read_csv('C:\\Users\\Ashish\\jupyter-notebook\\Training\\python-modules\\pandas\\biostats.csv')
# print(complete dataframe)
print("Here's the complete CSV")
print(_my_df)
print()
print("DataType of DataFrame is:")
print(type(_my_df))
print()
print('-------------------------------------------------------------------------------')
print()

# Selecting only one column in the output and showing its datatype
print(f"Age: \n{_my_df['Age']}")
print()
print('-------------------------------------------------------------------------------')
print()

# Converting the values in the 'Age' column to 'String'
print(f"Age: \n{_my_df['Age'].to_string()}")
print(f"DataType of converting Values is: {type(_my_df['Age'].to_string())}")

# Output:
'''
Here's the complete CSV
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

DataType of DataFrame is:
<class 'pandas.core.frame.DataFrame'>

-------------------------------------------------------------------------------

Age: 
0     41
1     42
2     32
3     39
4     30
5     33
6     26
7     30
8     53
9     32
10    47
11    34
12    23
13    36
14    38
15    31
16    29
17    28
Name: Age, dtype: int64

-------------------------------------------------------------------------------

Age: 
0     41
1     42
2     32
3     39
4     30
5     33
6     26
7     30
8     53
9     32
10    47
11    34
12    23
13    36
14    38
15    31
16    29
17    28
DataType of converting Values is: <class 'str'>

'''