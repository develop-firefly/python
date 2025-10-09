# To get the number of rows and columns in the pandas DataFrame

import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish//jupyter-notebook//Training//python-modules//pandas//biostats.csv')
print(_my_df.shape)

# Output
'''
(18, 5)
'''
# 18 is the number of rows (including Header)
# 5 is the number of columns (excluding index)