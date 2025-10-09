# How to locate a specific row in pandas DataFrame

import pandas as pd

# Create a Python Dictionary
_my_data_set = {
                  'cars': ["BMW", "Volvo", "Ford"],
                  'passings': [3, 7, 2]
                }

# Create a DataFrame by passing the dictionary to pd.DataFrame
_my_df = pd.DataFrame(_my_data_set)

# print the dataframe
print(f"Existing DataFrame is: \n{_my_df}")
print()
print('-------------------------------------------------------------------------------')
print()
# Locating Specific row by its index
# Note: Their is single square bracket
print(f"Specific Row in Dataframe: \n{_my_df.loc[1]}")
print()
print('-------------------------------------------------------------------------------')
print()
# Locating Specific row(s) by using index ranges
# Note: Their are double square brackets
print(f"Specific Row in Dataframe: \n{_my_df.loc[[1,2]]}")


# Output

'''
Existing DataFrame is: 
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2

-------------------------------------------------------------------------------

Specific Row in Dataframe: 
cars        Volvo
passings        7
Name: 1, dtype: object

-------------------------------------------------------------------------------

Specific Row in Dataframe: 
    cars  passings
1  Volvo         7
2   Ford         2

'''