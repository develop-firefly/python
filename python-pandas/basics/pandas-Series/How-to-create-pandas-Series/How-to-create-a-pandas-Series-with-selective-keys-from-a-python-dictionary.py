# How to create a pandas 'Series' with only selective keys from a Python Dictionary

import pandas as pd

# Create a python dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}

# Create a pandas Series only with first two keys of the dictionary
_my_selective_pds = pd.Series(calories, index=["day1", "day2"])

print(f"Pandas Series with selective indexs:- \n{_my_selective_pds}")


# Output
'''
Pandas Series with selective indexs:- 
day1    420
day2    380
dtype: int64
'''