# How to create a pandas dataframe from a Python dictionary

import pandas as pd

# Create a Python Dictionary
_my_data_set = {
                  'cars': ["BMW", "Volvo", "Ford"],
                  'passings': [3, 7, 2]
                }

# Create a DataFrame by passing the dictionary to pd.DataFrame
_my_df = pd.DataFrame(_my_data_set)

# print the dataframe
print(_my_df)

# Output
'''
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2

'''